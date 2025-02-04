from urllib.request import urlopen
from bs4 import BeautifulSoup

def fetch_cricbuzz_scores():
    """
    Fetches live cricket match scores from CricBuzz.
    """
    quote_page = 'http://www.cricbuzz.com/cricket-match/live-scores'
    page = urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    
    updates = []
    for score in soup.find_all('div', attrs={'class': 'cb-col cb-col-100 cb-lvmain'}):
        s = score.text.strip()
        updates.append(s)
    
    return updates

def display_scores(scores):
    """
    Displays fetched cricket match scores.
    """
    print('-' * 70)
    for i, match in enumerate(scores, 1):
        print(f"{i}. {match}")
        print('-' * 70)

if __name__ == "__main__":
    scores = fetch_cricbuzz_scores()
    if scores:
        display_scores(scores)
    else:
        print("No live matches found.")
