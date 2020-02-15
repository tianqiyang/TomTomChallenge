# -*- coding: utf-8 -*-
"""Insert Data component.

This module gets lists of Course and Department objects from ReadCourseData.py
and insert those data into desired databse
"""

import os
import datetime
import json
from pymongo import MongoClient
from pymongo import errors as mongoerrors
from pathlib import Path

def get_db():
    """Get MongoDB username and password from config file and returns desired databse.

    Raises:
        pymongo.errors: possibly connection errors or conficuration errors
    Returns:
        The database object

    """
    username, password = "dev2020", "dev2020"
    db_name = "Dev2020"
    client = MongoClient('mongodb+srv://' + username + ':' + password
                         + "@dev2020-k3zss.mongodb.net/test?retryWrites=true&w=majority")
    return client.get_database(db_name)


def check_file_open(filename):
    """Check if the json file exist in the specific directory.

    Args:
        filename: the path to the desired file
    Raises:
        FileNotFoundError: File does not exit
    Returns:
        The database object

    """
    if filename:
        with open(filename, 'r') as f:
            return json.load(f)
    raise FileNotFoundError('File', filename, 'is not found!')


def insert_data(data):
    """Insert data into databse.

    TODO: data type is not yet determined (MUST BE A DICT)

    Args:
        data: data to be inserted
    Raises:
        pymongo.errors: possibly connection errors or conficuration errors
    Returns:
        None
 
    """
    db = get_db()
    collection = db[collection]
    collection.insert_one(data)


def main():
    """Runner of this DBImport program.

    With help of other functions, this main function could read the data from
    json files and put them into desired databses.
    """

if __name__ == "__main__":
    main()
