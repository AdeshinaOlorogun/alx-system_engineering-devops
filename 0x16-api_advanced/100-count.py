import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively counts occurrences of keywords in hot article titles from a subreddit."""
    if counts is None:
        counts = {}
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-user-agent'}
    params = {'after': after, 'limit': 100}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return
        
        data = response.json().get('data')
        if not data:
            return
        
        posts = data.get('children')
        if not posts:
            return
        
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                keyword = word.lower()
                if keyword in counts:
                    counts[keyword] += title.count(keyword)
                else:
                    counts[keyword] = title.count(keyword)
        
        after = data.get('after')
        if after is None:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for keyword, count in sorted_counts:
                print(f"{keyword}: {count}")
            return
        else:
            return count_words(subreddit, word_list, after, counts)
    
    except Exception as e:
        return

# Example usage
if __name__ == "__main__":
    subreddit = "python"
    word_list = ["python", "java", "javascript", "ruby"]
    count_words(subreddit, word_list)
