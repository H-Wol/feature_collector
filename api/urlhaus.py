import requests


class URLHaus:
    def __init__(self):
        self.url = "https://urlhaus-api.abuse.ch/v1/"

    def get_hash_info(self, str, type):
        try:
            if type == "MD5":
                data = {
                    "md5_hash": str
                }
            elif type == "SHA256":
                data = {
                    "sha256_hash": str
                }
            else:
                return dict()
            response = requests.post(self.url + "payload/", data=data)
            json_response = response.content.decode("utf-8", "ignore")
            return json_response
        except Exception as e:
            print(e)
            return dict()

    def get_hash_info(self, str):
        try:
            data = {
                "url": str
            }
            response = requests.post(self.url + "url/", data=data)
            json_response = response.content.decode("utf-8", "ignore")
            return json_response
        except Exception as e:
            print(e)
            return dict()

    def get_domain_or_ip_info(self, str):
        try:
            data = {
                "host": str
            }
            response = requests.post(self.url + "host/", data=data)
            json_response = response.content.decode("utf-8", "ignore")
            return json_response
        except Exception as e:
            print(e)
            return dict()


if __name__ == "__main__":
    m = URLHaus()
    api_key = "8618692d41eb8f55823e3b219607827dd6d4feb32203c93d818e1cac35ec9362"
    hash = "d5ee3a86821e452c33f178dc080aff7ca5054518a719ef74320909cbb55bb6c5"
    print(m.get_hash_info(hash))
