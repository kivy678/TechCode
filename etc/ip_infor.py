import requests

try:
    import simplejson as json
except ImportError:
    import json

from urlparse import urljoin

try:
    r = requests.get(urljoin("http://api.ipstack.com/",
                             "0.0.0.0"), params={'access_key': ""})
    content = json.loads(r.text)

    print(content["region_name"], content["city"], content["zip"])

except Exception as e:
    print(e)
