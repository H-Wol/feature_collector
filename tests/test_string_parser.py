import os
import sys

# Add the path to feature_collector for module imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'feature_collector'))

from string_parser import check_str


def test_check_str_sha256():
    sha = 'd5ee3a86821e452c33f178dc080aff7ca5054518a719ef74320909cbb55bb6c5'
    assert check_str(sha) == {"SHA-256": [sha]}


def test_check_str_md5():
    md5 = '0ff2f7ef56717a032d970ff8b78c85e4'
    assert check_str(md5) == {"MD5": [md5]}


def test_check_str_url():
    url = 'http://example.com/'
    assert check_str(url) == {"URLs": [url]}


def test_check_str_invalid():
    assert check_str('not_an_ioc') is None
