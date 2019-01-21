#!/usr/bin/env python3

############################
#  r o b o                 #
#           s c r a p e r  #
############################
# desc: scrapes robots.txt #
# greetz fr0m: #9x,        #
#              substance,  #
#              and ce6     #
############################
#  vers: v1.0 (r0b0n3gr0)  #
############################

import sys
from bs4 import BeautifulSoup
import urllib3
import utils

def connect(url):
  robot_append = "/robots.txt"
  robot_url = url + robot_append
  # will color this message later
  print("[*] trying to connect to: %s" % (robot_url))
  """
  You'll need a PoolManager instance to make requests.
  This object handles all of the details of connection
  pooling and thread safety so that you don't have to.
  """
  # we need to throw and exception if there is an invalid SSL cert
  http = urllib3.PoolManager()
  response = http.request('GET', robot_url, headers={'User-Agent': utils.random_user_agent()})
  soup = BeautifulSoup(response.data, "lxml")
  print(soup)

def open_list(filename):
  try:
    with open(filename) as url_list:
      lines = [x.rstrip("\n") for x in url_list]
      for url in lines:
        connect(url)
  except IOError:
    print(utils.tc.FAIL + "[-]" + utils.tc.RESET + " %s doesn't exist!" % (filename))

def main():
  if len(sys.argv) > 1:
    filename = sys.argv[1]
    open_list(filename)
  else:
    print(utils.tc.FAIL + "[-]" + utils.tc.RESET + " add a filename!")


main()
