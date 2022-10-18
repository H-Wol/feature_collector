import time
import requests

class VTApi():
    def __init__(self,api_key):
        self.url  = "https://www.virustotal.com/api/v3/"
        self.headers = {"accept": "application/json"}
        self.headers["x-apikey"] = api_key
    def get_hash_info(self,str,rate):
        try:
            request_url = self.url + "files/" + str
            response = requests.get(request_url, headers=self.headers)
            time.sleep(rate)
            return response.json()
        except Exception as e:
            print(e)
            return dict()
        
    def get_url_info(self,str,rate):
        try:
            request_url = self.url + "urls/" + str
            response = requests.get(request_url, headers=self.headers)
            time.sleep(rate)
            return response.json()
        except Exception as e:
            print(e)
            return dict()
    def get_ip_info(self,str,rate):
        try:
            request_url = self.url + "ip_addresses/" + str
            response = requests.get(request_url, headers=self.headers)
            time.sleep(rate)
            return response.json()
        except Exception as e:
            print(e)
            return dict()
    def get_domain_info(self,str,rate):
        try:
            request_url = self.url + "domains/" + str
            response = requests.get(request_url, headers=self.headers)
            time.sleep(rate)
            return response.json()
        except Exception as e:
            print(e)
            return dict()

    

if __name__ == "__main__":
    api_key = "8618692d41eb8f55823e3b219607827dd6d4feb32203c93d818e1cac35ec9362"
    hash = "04a2b775e2d082aa0428b14962eb1a23"
    