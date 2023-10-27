import requests
import sys
import urllib3
from http.client import HTTPConnection
from urllib.parse import urlparse
import asyncio
import aiohttp
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http':'http://127.0.0.1:8082', 'https':'http://127.0.0.1:8082'}

def statuscode(url):
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    fullurl = ''
    for method in ('http', 'https'):
        fullurl = method +'://'+ url
        s = requests.get(fullurl, verify=False, proxies=proxies, allow_redirects=True)
        print("The site {0} status code is {1}".format(fullurl, s.status_code))


#async def site_is_online_async(url, timeout=2):
    #parser = urlparse(url)
    #host = parser.netloc or parser.path.split("/")[0]
    #for scheme in ("http", "https"):
       # target_url = scheme + "://" + host
       # try:
        #    async with aiohttp.ClientSession() as session:
         #       await session.head(target_url, timeout=timeout)
          #      return target_url, session.status
        #except asyncio.exceptions.TimeoutError:
         #       error = Exception("timed out")
        #except Exception as e:
         #       error = e
    #raise error
async def site_is_online_async(url, timeout=2):

    error = Exception("unknown error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for scheme in ("http", "https"):
        target_url = scheme + "://" + host
        async with aiohttp.request('GET',target_url) as resp:
            try:
                 return resp.status
            except asyncio.exceptions.TimeoutError:
                error = Exception("timed out")
            except Exception as e:
                error = e
        raise error
