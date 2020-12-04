#! usr/bin/#!/usr/bin/env python3

""" this is a crawler program using beautifulsoup
    for documentation see https://www.crummy.com/software/BeautifulSoup/
    usage scraber.py https://bioinf.nl/~fennaf
"""

__author__ = "Fenna Feenstra"

# needs pip install --upgrade html5lib==1.0b8
import sys
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


def hack_ssl():
    """ ignores the certificate errors"""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


def open_url(url):
    """ reads url file as a big string and cleans the html file to make it
        more readable. input: url, output: soup object
    """
    ctx = hack_ssl()
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def read_hrefs(soup):
    """ get from soup object a list of anchor tags,
        get the href keys and and prints them. Input: soup object
    """
    tags = soup('a')
    for tag in tags:
        print(tag) #get href key or none
    return 0


def main(args = None):
    if len(args) > 1:
        s = open_url(args[1])
        read_hrefs(s)
    return 0


if __name__ == '__main__':
    exitcode = main(sys.argv)
    sys.exit(exitcode)
