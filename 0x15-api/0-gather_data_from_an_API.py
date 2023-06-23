#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{url}users/{sys.argv[1]}").json()
    todos = requests.get(f"{url}todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print(
        f'Employee {user.get("name")} is done with tasks({len(completed)}/{len(todos)}):'
    )
    [print(f"\t {c}") for c in completed]
