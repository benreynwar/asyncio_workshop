import logging
import asyncio
import re

import aiohttp
from bs4 import BeautifulSoup


'''
Make a web crawler.
It starts from a page, finds all the links in that page, and then loads those pages.
We'll use asyncio to grab the pages so we can do it synchronously.

Use this file as a starting point.  Make any changes you want to get it working.
The final output should by a dictionary that maps urls to list of links in them.
'''


logger = logging.getLogger(__name__)

MAX_REQUESTS = 5

n_requests = 0


class MaxRequestsException(Exception):
    pass


async def get_page(session, url):
    global n_requests
    n_requests += 1
    if n_requests > MAX_REQUESTS:
        logger.warning(f'Hit maximum number ({MAX_REQUESTS}) of requests')
        return None
    response = await session.get(url)
    data = await response.read()
    return data


def get_links(html):
    '''
    This function returns all the links in a webpage that a crawler should follow.
    '''
    if html is None:
        return ['Hit max requests']
    soup = BeautifulSoup(html)
    links = []
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))
    return links


async def crawl(starting_url):
    link_map = {}
    async with aiohttp.ClientSession() as session:
        pass
        '???'
    return link_map


def main():
    # Setup logging
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    # Crawl
    link_map = asyncio.run(crawl('https://www.belatrixsf.com/blog/key-tips-to-test-web-crawlers'))

    # Display the results
    for url, links in link_map.items():
        print(url)
        for link in links:
            print('  ' + link)
    

if __name__ == '__main__':
    main()

'''
If you get it working and you want to improve it you could:
 - Set a maximum depth for the crawler
 - use asyncio.BoundedSemaphore rather than a global variable to limit requests
'''
