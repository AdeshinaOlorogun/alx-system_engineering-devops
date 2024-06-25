#!/usr/bin/python3
'''
    This module contains the function top_ten
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
        Returns the top ten posts for a given subreddit
    '''
    user = {'User-Agent': 'Lizzie'}
    try:
        response = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                                .format(subreddit), headers=user)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        
        posts = data.get('data', {}).get('children', [])
        if not posts:
            print(None)
        else:
            for post in posts:
                print(post.get('data', {}).get('title'))
    except requests.exceptions.RequestException:
        print(None)
    except ValueError:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])

