'''
https://pawelmhm.github.io/asyncio/python/aiohttp/2016/04/22/asyncio-aiohttp.html
'''
import requests


def hello():
    data = requests.get("http://httpbin.org/get")
    print(len(data.content))


hello()
