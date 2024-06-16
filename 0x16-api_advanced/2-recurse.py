#!/usr/bin/env python3

import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively returns a list of titles of all hot articles for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-user-agent'}
    params = {'after': after, 'limit': 100}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None
        
        data = response.json().get('data')
        if not data:
            return None
        
        posts = data.get('children')
        if not posts:
            return None

        for post in posts:
            hot_list.append(post['data']['title'])
        
        after = data.get('after')
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    except Exception as e:
        return None

# Example usage
if __name__ == "__main__":
    subreddit = "python"
    hot_list = recurse(subreddit)
    if hot_list:
        print(f"Total hot articles in r/{subreddit}: {len(hot_list)}")
        for title in hot_list:
            print(title)
    else:
        print(None)
