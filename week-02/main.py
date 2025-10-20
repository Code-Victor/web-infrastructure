#!/usr/bin/python3
"""
Week 2: API Advanced - Reddit API Project

This module contains exercises for working with the Reddit API.
Focus areas:
- API pagination
- Recursive API calls
- JSON parsing
- Sorting dictionaries by value
"""

import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers for a subreddit.

    Args:
        subreddit (str): The name of the subreddit

    Returns:
        int: Number of subscribers, or 0 if invalid subreddit
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Python:APIProject:v1.0 (by /u/student)'}

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
            return subscribers
        else:
            return 0

    except requests.exceptions.RequestException:
        return 0


def top_ten(subreddit):
    """
    Query the Reddit API and print the titles of the first 10 hot posts.

    Args:
        subreddit (str): The name of the subreddit

    Returns:
        None: Prints titles or None if invalid subreddit
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Python:APIProject:v1.0 (by /u/student)'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers,
                                params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            if not posts:
                print(None)
                return

            for post in posts:
                title = post.get('data', {}).get('title', '')
                print(title)
        else:
            print(None)

    except requests.exceptions.RequestException:
        print(None)


def main():
    """
    Main function to demonstrate all exercises.
    """
    print(f"""{'=' * 60}
EXERCISE 0: Number of Subscribers
{'=' * 60}
r/python subscribers: {number_of_subscribers('python')}
r/programming subscribers: {number_of_subscribers('programming')}
Invalid subreddit subscribers: {number_of_subscribers('this_subreddit_does_not_exist_xyz')}

{'=' * 60}
EXERCISE 1: Top Ten Posts
{'=' * 60}
Top 10 hot posts in r/python:
""")
    top_ten('python')

    print(f"""
Invalid subreddit:
""")
    top_ten('this_subreddit_does_not_exist_xyz')

    print(f"""\n{'=' * 60}
EXERCISE 2: Recursive Function
{'=' * 60}
Fetching all hot posts from r/python (this may take a moment)...
""")



if __name__ == "__main__":
    main()
