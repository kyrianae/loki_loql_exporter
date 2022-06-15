import requests
requests.packages.urllib3.disable_warnings()
import urllib
import datetime
import base64

API_VERSION = 1

class loki():

    def __init__(self, url):

        self.url = url
        self.headers = headers = {
            'content-type': 'application/json',
            # "Authorization": authorization
        }

    def get(self,suffix):
        return requests.get(url = self.url+suffix, headers=self.headers, verify=False)

    def query(self,delta,query,limit,step):
        # url = self.u
        now_stamp = datetime.datetime.now().timestamp()
        start = now_stamp - delta
        # full_query=  {
        #     'end': now_stamp * 1000,
        #     'direction': 'BACKWARD',
        #     'start': start * 1000,
        #     'query': query,
        #     'limit': limit
        # }
        # print (full_query)

        cleanquery = query.replace("\\","\\\\\\\\")
        query_new_enc = f'/loki/api/v{API_VERSION}/query_range?end={now_stamp}&start={start}&limit={limit}&step={step}&query={urllib.parse.quote_plus(cleanquery)}'

        return self.get(query_new_enc)

