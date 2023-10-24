#!/usr/bin/python3
"""Gather data from an API and write to CSV."""
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
    with open(user_ID + ".csv", "w") as file:
        for task in todos:
            file.write("\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
                user_ID,
                username,
                task.get("completed"),
                task.get("title")
            ))
