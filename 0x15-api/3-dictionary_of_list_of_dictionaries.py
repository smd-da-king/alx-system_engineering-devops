#!/usr/bin/python3
"""Gather data from an API and export to JSON."""
import json
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

    username = user.get("username")

    task_arr = []
    for task in todos:
        task_dict = {}
        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = username
        task_arr.append(task_dict)

    res = {user_ID: task_arr}
    res = json.dumps(res)

    with open(user_ID + ".json", "w") as file:
        file.write(res)
