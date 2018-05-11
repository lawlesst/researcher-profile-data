"""
Harvest divisons/sub-orgs
"""

import json
import sys
import re

from bs4 import BeautifulSoup

from utils import get_url

MATCH = re.compile(".*\(([A-Z]+)\)")


def harvest():
    doc = get_url(
        'https://www.nih.gov/institutes-nih/list-nih-institutes-centers-offices'
    )
    soup = BeautifulSoup(doc, "html.parser")

    d = {}
    for b in soup.select('a.button-link-5em'):
        d[b.attrs['href']] = b.text

    out = []
    for item in soup.select('div.syndicate p'):
        href = item.select('a')[0]
        link = href.attrs['href']
        print(href.text, file=sys.stderr)
        # name = href.text
        # code = d[link]
        code = MATCH.search(item.text).groups()[0]
        overview = item.text.split('\n')[1].strip('\t')
        out.append({
            "otype": item.findPrevious('h2').text.replace('NIH ', '').rstrip('s'),
            "link": link,
            "name": href.text,
            "code": code,
            "overview": overview
        })

    return out


if __name__ == "__main__":
    out = harvest()
    print(json.dumps(out, indent=2))
