#!/usr/bin/env python3
import requests

def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-user-agent'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        return 0

# Example usage
if __name__ == "__main__":
    subreddit = "python"
    print(f"The number of subscribers in r/{subreddit} is {number_of_subscribers(subreddit)}")

