#!/usr/bin/python3
"""
This module contains the function recurse.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data["data"]["children"]
            for post in posts:
                hot_list.append(post["data"]["title"])
            after = data["data"]["after"]
            if after is not None:
                return recurse(subreddit, hot_list, after)
            return hot_list
        except (KeyError, ValueError):
            return None
    else:
        return None
