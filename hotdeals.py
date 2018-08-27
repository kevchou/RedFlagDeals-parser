from bs4 import BeautifulSoup
import urllib.request


URL = "http://forums.redflagdeals.com/hot-deals-f9/"

# Store all thread information 
ts = []

num_pages = 3

for i in range(num_pages):
    request = urllib.request.urlopen(URL + str(i))
    raw = request.read()
    soup = BeautifulSoup(raw, 'html.parser')

    # Get all posts on page into a list
    all_threads = soup.find_all('li', {'class':'row topic'})

    for thread in all_threads:
        
        # Title and link
        thread_title_soup = thread.find('a', {'class':'topic_title_link'})
        thread_title = thread_title_soup.text.strip()
        thread_link = thread_title_soup['href']

        # Score
        thread_score_soup = thread.find('dl', {'class':'post_voting'})
        thread_score = int(thread_score_soup.text.strip()) if thread_score_soup else 0

        # Post time
        thread_posttime_soup = thread.find('span', {'class':'first-post-time'})
        thread_posttime = thread_posttime_soup.text

        # Number of posts and views
        thread_numposts = thread.find('div', {'class': 'posts'}).text
        thread_numviews = thread.find('div', {'class': 'views'}).text

        t = {
            'title': thread_title,
            'link': thread_link,
            'score': thread_score,
            'posttime': thread_posttime,
            'num_posts': thread_numposts,
            'num_views': thread_numviews,
            'page': i
        }

        ts.append(t)

ts.sort(key=lambda x: x['score'])

for t in ts:
    print(t['page'], t['score'], t['title'])