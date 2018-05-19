"""
Harvest PIs.
"""

import json
import logging
import sys

from bs4 import BeautifulSoup
import bs4
from nameparser import HumanName

from utils import get_url

BASE_URL = "https://irp.nih.gov"


def process_name(raw):
    # replace two spaces with one
    r2 = raw.replace('  ', ' ')
    chunked = r2.split(',')
    name = chunked[0]
    honors = ", ".join([c.strip() for c in chunked[1:]])
    hn = HumanName(name)
    if hn.middle == "":
        middle = None
    else:
        middle = hn.middle
    return {
        "label": r2,
        "first": hn.first,
        "last": hn.last,
        "middle": middle,
        "honors": honors
    }


def get_people():
    url = BASE_URL + "/our-research/principal-investigators/name"
    doc = get_url(url)
    soup = BeautifulSoup(doc, "html.parser")

    content = soup.select('span.pilist-name a')

    out = []

    for pi in content:
        d = {}
        # name and link
        d['label'] = pi.text
        d['url'] = BASE_URL + pi.attrs['href']
        out.append(d)

    logging.info("Found {} profiles.".format(len(out)))
    return out


def process_title(title):
    # Replace some bad data in titles
    return title.replace(", 73 MT Wayte AvenueSuite 2Framingham, MA 01702", "")


def get_profile(url):
    profile = {}
    profile['url'] = url
    doc = get_url(url)
    if doc is None:
        return profile
    soup = BeautifulSoup(doc, "html.parser")
    profile['name'] = soup.select('h1.pi-name')[0].text
    name = process_name(profile['name'])
    profile.update(name)
    profile['email'] = soup.select('p.pi-email a')[0].text
    title = ", ".join([t.text for t in soup.select('h2.pi-title')[:3]])
    profile['title'] = process_title(title)
    profile['position_title'] = profile['title'].split(',')[0]
    try:
        profile['photo'] = BASE_URL +\
            soup.select('div.pi-photo img')[0].attrs['src']
    except IndexError:
        profile['photo'] = None
    # bio
    bio_spot = soup.find("h2", text="Biography")
    bio_elems = [p for p in bio_spot.findNextSiblings('div')]
    b = []
    for elem in bio_elems:
        for e in elem:
            if isinstance(e, bs4.element.Tag):
                b.append(e.text)
            else:
                b.append(e)

    profile['bio'] = "".join(b)

    # research headings
    profile['research_interests'] = [
        ra.text for ra in soup.find("h2", text="Research Topics")
        .findNextSiblings('div')[0].select('h3')
    ]

    profile['pmids'] = [
        pm.split('/')[-1] for pm in [
            h.attrs['href'] for h in soup.select('ol a')
        ]
    ]

    # website
    try:
        profile['website'] = [
            h.attrs['href'] for h in soup.select('div.buttons a.button')
        ][0]
    except IndexError:
        profile['website'] = None

    return profile


if __name__ == "__main__":
    people = get_people()
    out = []
    for idx, person in enumerate(people):
        print(person['url'], file=sys.stderr)
        meta = get_profile(person['url'])
        out.append(meta)
        if idx > 20:
            break
    print(json.dumps(out, indent=2))
