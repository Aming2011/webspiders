import urllib.request

"""
This is a browser package
"""


class WebSpider:
    def __init__(self, headers=None, ip_address="127.0.0.1", data=None):
        self.headers = headers
        self.ip_address = ip_address
        self.data = data
        self.opener = urllib.request.build_opener(self.ip_address)

    def change_headers(self, new_headers):
        self.headers = new_headers

    def change_ip_address(self, new_ip_address):
        self.ip_address = new_ip_address
        self.opener = urllib.request.build_opener(self.ip_address)

    def brow(self, url):
        requests = urllib.request.Request(url=url, headers=self.headers, data=self.data)
        response = self.opener.open(requests)
        return response.read()
