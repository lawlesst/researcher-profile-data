import requests
import requests.packages.urllib3

import requests_cache
requests.packages.urllib3.disable_warnings()

requests_cache.install_cache('/tmp/nih')


def get_url(url):
    headers = {
        'User-Agent': 'https://github.com/lawlesst/research-profile-data/',
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception("URL error: " + response.status_code)
    return response.content
