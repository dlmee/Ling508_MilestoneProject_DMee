from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re

class CollectData:

    def __init__(self):
        pass
    def scrape(self, url):
        try:
            source = urlopen(url)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)
        else:
            bs = BeautifulSoup(source.read(), 'html.parser')
            paragraphs = []
            for paragraph in bs.body.find_all('p', class_=False):
                if len(paragraph.get_text()) > 10:
                    paragraphs.append(paragraph.get_text())
            paragraphs = paragraphs[10:-47]
            sentences = []
            for i, paragraph in enumerate(paragraphs):
                paragraph = re.sub('[\n\"\-\',\[\d\]]', ' ', paragraph)
                sents = re.split('[\.\!\?]', paragraph)
                for s in sents:
                    sentences.append(s)
            return sentences

