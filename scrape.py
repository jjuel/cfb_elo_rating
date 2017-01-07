'''This script will scrape the scores for college football'''
from bs4 import BeautifulSoup
import requests

def get_scores(url):
    '''Get scores with BS from given URL'''
    scores = []
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')

    for text in soup.find_all('pre'):
        if text.text is None:
            continue
        content = text.text
        scores.append(content)

    return split_scores[4]

def parse(s):
    '''Parse each game and insert into dictionary'''
    return {
        'Date': s[0:9],
        'Visiting Team': s[9:38].strip(),
        'Visitor Score': s[38:41],
        'Home Team': s[41:69].strip(),
        'Home Score': s[69:72],
        'Location(if neutral)': s[72:].strip()
    }

SCORES_LINK = "http://prwolfe.bol.ucla.edu/cfootball/scores.htm"
full_scores = get_scores(SCORES_LINK)

split_scores = full_scores[0].splitlines()

for i in range(0, 4):
    del split_scores[0]

scores_dict = [{}]

for st in split_scores:
    scores_dict.append(parse(st))

print(scores_dict)
