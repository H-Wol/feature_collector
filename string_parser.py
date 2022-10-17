from hashlib import sha1, sha256
import os
import regexes


def is_file(str):
    return os.path.isfile(str)

def check_str(str):
    return_dict = dict()
    if regexes.sha256_regex.fullmatch(str):
        return {"SHA256": [str]}
    if regexes.md5_regex.fullmatch(str):
        return {"MD5": [str]}
    if regexes.sha1_regex.fullmatch(str):
        return {"SHA1": [str]}
    if regexes.URL_regex.fullmatch(str):
        return {"URLs": [str]}
    if regexes.ipv4_regex.fullmatch(str):
        return {"IPs": [str]}
    if regexes.domain_regex.fullmatch(str):
        return {"Domains": [str]}
    if regexes.ipv6_regex.fullmatch(str):
        return {"IPs6": [str]}
    return None


if __name__ == "__main__":
    print(check_str("d5ee3a86821e452c33f178dc080aff7ca5054518a719ef74320909cbb55bb6c5"))
    print(check_str("322719458bc5dffec99c9ef96b2e84397285cd73"))
    print(check_str("0ff2f7ef56717a032d970ff8b78c85e4"))
    print(check_str("103.224.182.250"))
    print(check_str("2001:0DB8:0000:0000:0000:0000:1428:57ab"))
    print(check_str("mojobiden.com"))
    print(check_str("http://tonyshop312.com/"))
    print(check_str("tagas"))
