import requests
from requests.exceptions import ConnectionError, HTTPError, InvalidURL, Timeout

def LinkCheck(link):
    try:
        r = requests.get(link, timeout = 10)
        r.raise_for_status()
        return link, "pass"

    except (ConnectionError, HTTPError, InvalidURL, Timeout):
        return link, "fail"

     

result = LinkCheck("https://futures.nhs.uk/OIforC/view?objectId=25390480")
print(result)