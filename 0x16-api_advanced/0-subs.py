import requests

def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom-User-Agent'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'subscribers' in data['data']:
                return data['data']['subscribers']
            else:
                return 0
        elif response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
            return 0
        else:
            print(f"Error: Status code {response.status_code}")
            return 0
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return 0

