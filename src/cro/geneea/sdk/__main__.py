# -*- coding: utf-8 -*-

"""
The command line interface.
"""


import argparse
import redis
import json
import time
import os
import sys

from cro.geneea.sdk import Client


def read_args():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i", "--input", required=False, type=str, help="Input filename"
    )

    parser.add_argument(
        "-t", "--type", required=False, type=str, help="The operation type"
    )

    parser.add_argument(
        "-f",
        "--format",
        required=False,
        type=str,
        help="[Optional] type of an output file, allowed types xml, json or csv",
    )

    parser.add_argument(
        "-s",
        "--server",
        required=False,
        action="store_true",
        help="Run geneea SDK in redis server mode.",
    )

    result = parser.parse_args()

    return result


def read_envs():
    return {"GENEEA_API_KEY": os.environ.get("GENEEA_API_KEY")}


def main():

    args = read_args()
    envs = read_envs()

    client = Client(key=envs["GENEEA_API_KEY"])

    # run Geneea API Client as Redis server. Awaiting message as
    # "geneea_input_text": "Some full imput text here"

    if args.server:

        print("Running in redis server mode")

        rs = redis.Redis()

        while True:
            if rs.exists("geneea_input_text"):
                input_text = rs.get("geneea_input_text")

                print(f"Got new query {input_text}")
                analysis = client.get_analysis(input_text)
                # result = client.serialize(analysis,format="json")
                rs.set("geneea_result", json.dumps(analysis.analyzed))
                rs.delete("geneea_input_text")
                print(rs.get("geneea_result"))
            time.sleep(1)

    else:
        with open(args.input, encoding="utf8") as file:
            text = "\n".join(file.readlines())

        print(f"{args.type.upper()}\n{len(args.type) * '-'}")

        match args.format:
            case None:
                format = "xml"
            case "csv" | "xml" | "json":
                format = args.format.lower()
            case _:
                print("The allowed format is ('xml', 'csv').")
                sys.exit(1)

        match args.type:
            case "analysis":
                result = client.get_analysis(text)
                result = client.serialize(result, format)
                print(result)
                # vs write to file with name = f"{args.input[0:args.input.index('.')]}_{args.type.lower()}.xml",

            case "account":
                result = client.get_account()
                print(result)

            case "entities":
                result = client.get_entities(text)
                print(result)

            case "tags":
                result = client.get_tags(text)
                print(result)

            case "sentiment":
                result = client.get_sentiment(text)
                print(result)

            case "relations":
                result = client.get_relations(text)
                print(result)

            case _:
                print(
                    "Choose one of the following type: 'analysis', 'account', 'entities', 'tags', 'sentiment', 'relations'."
                )
