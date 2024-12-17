#!/usr/bin/env python

from argparse import ArgumentParser
from csv import reader as csvreader
from json import loads as jsonloads
from time import sleep

import subprocess


parser = ArgumentParser(
    prog="view_finder",
    description="it parses known ids and tries to find unknown vehicle ids"
)
parser.add_argument('--csv')
parser.add_argument('--curl')
parser.add_argument('--curl-id')

args = parser.parse_args()


def parse_csv(filename: str) -> dict[int, str]:
    try:
        retval = dict()
        with open(filename, 'r') as f:
            reader = csvreader(f, delimiter=",")
            for row in reader:
                if row[0] == "":
                    row[0] = 0
                retval[int(row[0])] = row[1]
        return retval
    except Exception as ex:
        print(ex)
        raise (ex)


def load_curl(filename: str) -> str:
    with open(filename, 'r') as f:
        string = f.read()
    return string


def check_vehicle_id(vehicle_id: int, command: str, replace_id: int) -> bool:
    string = command.replace(str(replace_id), str(vehicle_id))
    completed = subprocess.run(["bash", "-c", string], capture_output=True)
    if completed.returncode == 0:
        response = jsonloads(completed.stdout)
        if response["success"] is True:
            return True
    else:
        print(f"{completed.returncode}={completed.stdout}")
    return False


def search_range(start: int, end: int, known: dict):
    for i in range(start, end):
        if i in known.keys():
            # print(f"{i:04} is known as {known[i]}")
            pass
        else:
            exists = check_vehicle_id(i, COMMAND, REPLACE_ID)
            print(f'{i:04} is {"discovered" if exists else "not available"}')
            sleep(1)


# print(f"{args.csv}{args.curl}{args.curl_id}")

KNOWN = parse_csv(args.csv)

COMMAND = load_curl(args.curl)

REPLACE_ID = args.curl_id


search = (0, 4000)

search_range(search[0], search[1], KNOWN)
