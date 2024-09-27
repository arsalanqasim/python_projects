from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urljoin
from fake_useragent import UserAgent
import time

with open('data.txt', 'w') as f:
    for year in range(2000, 2025):
        url = f"https://www.imdb.com/chart/top/?year={year}%2C{year}"
        f.write(f"Top movies for year: {year}\n")

        user_agent =UserAgent()
        req = Request(url, headers={'User-Agent': user_agent.random})

        try:
            html_doc = urlopen(req).read()
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            continue

        soup = BeautifulSoup(html_doc, 'html.parser')
        ul = soup.find_all(class_='ipc-metadata-list')

        for li in ul:
            title_link_list = li.find_all(class_='ipc-title-link-wrapper')
            for each_title_link in title_link_list[:5]:
                title_text = each_title_link.h3.string
                title_link = urljoin('https://www.imdb.com/', each_title_link['href'])

                f.write(f'\t{title_text}\n\thttps://www.imdb.com/{title_link}\n')
            f.write('\n')

        # time.sleep(2)  # Add delay to avoid overwhelming the server
        break
