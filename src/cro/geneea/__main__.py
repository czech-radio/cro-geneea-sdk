# -*- coding: utf8 -*-

"""
The command line interface.
"""


import argparse
import os

from cro.geneea import Client as GeneeaClient
from cro.geneea import Text as Text


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, type=str, help="The file name")
    parser.add_argument(
        "-t", "--type", required=True, type=str, help="The operation type"
    )

    args = parser.parse_args()

    KEY = os.environ.get("GENEEA_API_KEY")

    client = GeneeaClient(key=KEY)

    phrases = GeneeaClient.read_phrases(args.file)

    if args.type == "analysis":
        # ANALYSIS
        print("\nANALYSIS\n--------")
        result = client.get_analysis(phrases[0])
        text = Text(phrases[0], result)

        print(f"complete JSON: {result}")
        print("\nENTITIES\n--------")
        print(text.entities())
        print("\nTAGS\n--------")
        print(text.tags())
        print("\nRELATIONS\n--------")
        print(text.relations())
        print("\nSENTIMENT\n--------")
        print(text.sentiment())

    elif args.type == "account":
        # ACCOUNT
        print("ACCOUNT\n--------")
        result = client.get_account()
        print(result)
    elif args.type == "entities":
        # ENTITIES
        print("ENTITIES\n--------")
        result = client.get_entities(phrases[0])
        text = Text(phrases[0], result)
        print(text.entities())
    elif args.type == "tags":
        # TAGS
        print("TAGS\n--------")
        result = client.get_tags(phrases[0])
        text = Text(phrases[0], result)
        print(text.tags())
    elif args.type == "sentiment":
        # SENTIMENT
        print("SENTIMENT\n--------")
        result = client.get_sentiment(phrases[0])
        text = Text(phrases[0], result)
        print(text.sentiment())
    elif args.type == "relations":
        # REALATION
        print("RELATIONS\n--------")
        result = client.get_relations(phrases[0])
        text = Text(phrases[0], result)
        print(text.relations())
    else:
        print(
            "Choose one of the following type: 'analysis', 'account', 'entities', 'tags', 'sentiment', 'relations'"
        )
