# Week 2: API Advanced - Working with the Reddit API

This week focuses on practical API usage including making HTTP requests, parsing JSON responses, and handling API-specific requirements like custom headers.

## Learning Objectives

By the end of this project, you should be able to:

- Read API documentation to find the endpoints you need
- Parse JSON results from an API
- Handle API requirements (headers, parameters)
- Work with real-world APIs that require specific configurations

## Reddit API Overview

The Reddit API is a great resource for practicing API skills because:

- No authentication required for many endpoints
- Well-documented and stable
- Returns rich JSON data
- Free to use for learning
- Commonly used in technical interviews

### Key Endpoints We'll Use

| Endpoint | Description | Example |
|---|---|---|
| `/r/{subreddit}/about.json` | Get subreddit information | `/r/python/about.json` |
| `/r/{subreddit}/hot.json` | Get hot posts | `/r/python/hot.json` |

### Important Notes

1. **User-Agent Header**: Reddit requires a custom User-Agent header
2. **Base URL**: `https://www.reddit.com`
3. **Rate Limiting**: Be respectful with requests (don't spam)
4. **HTTPS Only**: Always use `https://` not `http://`

## Understanding Reddit's JSON Response Structure

When you make a request to the Reddit API, it returns nested JSON data. Understanding this structure is crucial.

### Subreddit Information (`/r/{subreddit}/about.json`)

```json
{
    "kind": "t5",
    "data": {
        "display_name": "python",
        "title": "Python",
        "public_description": "News about Python programming...",
        "subscribers": 1404371,
        "accounts_active": 4567,
        "created_utc": 1201242535.0,
        ...
    }
}
```

**Key fields:**

- `data.subscribers` - Number of subscribers
- `data.display_name` - Subreddit name
- `data.title` - Subreddit title
- `data.public_description` - Description

### Hot Posts (`/r/{subreddit}/hot.json`)

```json
{
    "kind": "Listing",
    "data": {
        "children": [
            {
                "kind": "t3",
                "data": {
                    "title": "Post title here",
                    "author": "username",
                    "score": 1234,
                    "num_comments": 56,
                    "url": "https://...",
                    "created_utc": 1697890000.0,
                    ...
                }
            }
        ],
        "after": "t3_abc123",
        "before": null
    }
}
```

**Key fields:**

- `data.children` - Array of posts
- `data.children[].data.title` - Post title
- `data.children[].data.author` - Post author
- `data.children[].data.score` - Upvotes minus downvotes

## Working with the Requests Library

The `requests` library makes HTTP requests simple in Python.

### Basic GET Request Pattern

```python
import requests

url = "https://www.reddit.com/r/python/about.json"
headers = {'User-Agent': 'Python:APIProject:v1.0'}

response = requests.get(url, headers=headers, timeout=10)

# Always check the status code
if response.status_code == 200:
    data = response.json()  # Parse JSON response
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### Key Concepts

1. **Headers**: Metadata sent with your request

   ```python
   headers = {'User-Agent': 'MyApp/1.0'}
   ```

2. **Status Codes**: Tell you if the request succeeded

   - `200` = Success
   - `404` = Not Found
   - `429` = Too Many Requests (rate limited)

3. **Timeout**: Prevent requests from hanging forever

   ```python
   response = requests.get(url, timeout=10)  # 10 seconds max
   ```

4. **JSON Parsing**: Convert JSON string to Python dictionary

   ```python
   data = response.json()
   ```

## Query Strings

Query strings are parameters appended to URLs after a `?` character.

### Format

```text
https://www.reddit.com/r/python/top.json?t=day&limit=10
                                         ^^^^^^^^^^^^^^
                                         Query string
```

### Using Query Parameters with Requests

```python
import requests

# Manual way (not recommended)
url = "https://www.reddit.com/r/python/hot.json?limit=10"

# Better way: use params dict
url = "https://www.reddit.com/r/python/hot.json"
params = {'limit': 10}

response = requests.get(url, params=params)
```

### Common Reddit Query Parameters

| Parameter | Description | Values |
|---|---|---|
| `limit` | Number of posts to return | 1-100 (default: 25) |

## Project Exercises

### Exercise 0: Number of Subscribers

Write a function that queries the Reddit API and returns the number of subscribers for a given subreddit.

**Prototype**: `def number_of_subscribers(subreddit)`

**Requirements**:

- If invalid subreddit, return 0
- Use the `/r/{subreddit}/about.json` endpoint
- Return the subscriber count as an integer
- Include proper User-Agent header
- Handle errors gracefully

**Example**:

```python
>>> number_of_subscribers('python')
1404371
>>> number_of_subscribers('invalid_subreddit_xyz')
0
```

### Exercise 1: Top Ten Posts

Write a function that queries the Reddit API and prints the titles of the first 10 hot posts.

**Prototype**: `def top_ten(subreddit)`

**Requirements**:

- Print titles of first 10 hot posts (one per line)
- If invalid subreddit, print `None`
- Use the `/r/{subreddit}/hot.json` endpoint
- Use the `limit` parameter to get 10 posts
- Include proper User-Agent header

**Example**:

```python
>>> top_ten('python')
Sunday Daily Thread: What's everyone working on this week?
Monday Daily Thread: Project ideas!
I built a tool that tells you how hard a website is to scrape
...
>>> top_ten('invalid_subreddit_xyz')
None
```

## Tips for Success

1. **Read the docs**: Reddit API docs are your friend
2. **Test incrementally**: Start with simple requests, verify they work
3. **Handle errors**: APIs can fail, timeout, or return unexpected data
4. **Use proper headers**: Always include a User-Agent
5. **Respect rate limits**: Don't spam the API
6. **Print debug info**: Use `print()` to see what data looks like
7. **Check status codes**: Always verify the request succeeded

## Common Pitfalls

1. **Forgetting User-Agent**: Reddit returns 429 without it
2. **Not checking status codes**: Always verify `response.status_code == 200`
3. **Typos in subreddit names**: Check spelling carefully
4. **Not handling None/empty data**: Use `.get()` for safe dictionary access
5. **Forgetting timeout**: Requests can hang without a timeout parameter

## Example: Complete Flow

```python
import requests

def get_reddit_data(subreddit):
    """Complete example of fetching Reddit data"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Python:APIProject:v1.0 (by /u/yourusername)'}
    params = {'limit': 10}
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        
        # Check if request was successful
        if response.status_code != 200:
            print(f"Error: Status code {response.status_code}")
            return None
        
        # Parse JSON
        data = response.json()
        
        # Extract posts
        posts = data.get('data', {}).get('children', [])
        
        # Process posts
        for post in posts:
            title = post.get('data', {}).get('title', '')
            score = post.get('data', {}).get('score', 0)
            print(f"{score} - {title}")
        
        return posts
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"JSON parsing error: {e}")
        return None

# Usage
get_reddit_data('python')
```

## Safe Dictionary Access

Use `.get()` method to avoid KeyError:

```python
# Bad - can raise KeyError
subscribers = data['data']['subscribers']

# Good - returns None if key doesn't exist
subscribers = data.get('data', {}).get('subscribers', 0)
```

## Error Handling Best Practices

```python
import requests

try:
    response = requests.get(url, headers=headers, timeout=10)
    
    if response.status_code == 200:
        data = response.json()
        # Process data
    else:
        return 0  # or None, depending on function
        
except requests.exceptions.Timeout:
    print("Request timed out")
    return 0
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
    return 0
```

## Resources

- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [Reddit API Rules](https://github.com/reddit-archive/reddit/wiki/API)
- [Requests Documentation](https://requests.readthedocs.io/)
- [Working with JSON in Python](https://realpython.com/python-json/)

## Practice Challenge

Before looking at the solutions in `main.py`, try to:

1. Fetch the subscriber count for r/python
2. Print titles of top 10 hot posts in r/learnprogramming
3. Modify your code to get 5 posts instead of 10

Good luck! 🚀
