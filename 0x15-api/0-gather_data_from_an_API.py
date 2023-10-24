#!/usr/bin/python3
"""Gather data from an API."""
import requests
import sys


if __name__ == "__main__":
    user_ID = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(url, user_ID)
    data_url = "{}/todos?userId={}".format(url, user_ID)

    "Get user's info"
    resp = requests.get(user_url)
    user = resp.json()
    "Get user's todos"
    resp = requests.get(data_url)
    todos = resp.json()

    done = 0
    total = 0

    for task in todos:
        total += 1
        if task.get("completed"):
            done += 1

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), done, total))

    for task in todos:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))
