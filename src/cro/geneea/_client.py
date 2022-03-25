import os
import datetime as dt
from enum import Enum
from typing import Optional, Union

from requests import post,get

__API_KEY__=os.environ.get('GENEEA_API_KEY')
__API_URL__=os.environ.get('GENEEA_API_URL')

class Client:
    """
    Geneea API Client
    """

    __filename__ = ""
    __url__f"{=__API_URL__}"
    __date_format__:f"%Y-%m-%d"
    __text__=""
    __headers__={
        'content-type:', 'application/json',
        'Authorization:', f"user_key {__API_KEY__}"
    }

    def __init__(self,str: _filename):
        self.__filename__=_filename
        self.__text__ = get_txt(__filename__)
        response=callGeenea(__text__)

    @classmethod
    def get_txt(_filename) -> str:
        raw = ""
        print("processing file: %s",_filename)
        with open(_filename,encoding='utf8') as f:
            line = f.readline()
            while line:
                line = f.readline()
                raw = raw + line
                print(line)
        return raw

    @classmethod
    def callGeneea(str: input) -> tuple:

        """
        get response from a server
        """
        __text__=f"{'text': '{raw}'}".format(raw=input)
        data = requests.post(__url__, json=__text__, headers=__headers__).json()["data"]
        return data

