#!/usr/bin/env python3

############################
#  r o b o                 #
#           s c r a p e r  #
############################
# desc: scrapes robots.txt #
# greetz fr0m: #9x,        #
#              substance,  #
#              and phaedo  #
############################
#        vers: v2.0        #
############################

import sys
import urllib3
import utils
from bs4 import BeautifulSoup
from http.client import responses
from colorama import Fore
from colorama import Style

# disable annoying HTTPS warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def connect(url):
  robot_append = "/robots.txt"
  robot_url = url + robot_append

  print(f"{Fore.BLUE}[*]{Style.RESET_ALL} Trying to connect to: {Style.BRIGHT}{robot_url}{Style.RESET_ALL}")

  http = urllib3.PoolManager(cert_reqs='CERT_NONE')

  try:
    response = http.request('GET', robot_url, headers={'User-Agent': utils.random_user_agent()})
  except urllib3.exceptions.HTTPError as err:
    print(f"{Fore.RED}[-]{Style.RESET_ALL} Request failed: {err.reason}")

  soup = BeautifulSoup(response.data, "html.parser")
  results = gather_robots_txt(soup, robot_url)
  crawl_robots_txt(results, url, http)

def open_list(filename):
  try:
    with open(filename) as url_list:
      lines = [x.rstrip("\n") for x in url_list]
      for url in lines:
        connect(url)
  except IOError:
    print(f"{Fore.RED}[-]{Style.RESET_ALL} '{filename}' doesn't exist!")

def gather_robots_txt(soup, url):
  results = {"Allowed":[], "Disallowed":[]}
  for line in str(soup).split("\n"):
    if line.startswith("Allow"):
      # if 'Allow' field is empty
      if len(line.split(': ')) < 2:
        print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} Empty 'Allow' field in {url}")
        continue
      results["Allowed"].append(line.split(': ')[1].split(' ')[0])
    if line.startswith("Disallow"):
      # if 'Disallow' field is empty
      if len(line.split(': ')) < 2:
        print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} Empty 'Disallow' field in {url}")
        continue
      results["Disallowed"].append(line.split(': ')[1].split(' ')[0])
  return results

def crawl_robots_txt(results, url, http):
  print_robots_txt(results)
  for x in results["Allowed"]:
    try:
      # don't follow fields with wildcards
      if "*" in x:
        continue
      response = http.request('GET', url + x, headers={'User-Agent': utils.random_user_agent()})
    except urllib3.exceptions.HTTPError as err:
      print(f"{Fore.RED}[-]{Style.RESET_ALL} Request failed: {err.reason}")
    print(f"{Fore.BLUE}[*]{Style.RESET_ALL} {url + x} -> {Fore.YELLOW}{response.status}{Style.RESET_ALL}{Style.BRIGHT} '{responses[response.status]}'{Style.RESET_ALL}")

  for x in results["Disallowed"]:
    try:
      if "*" in x:
        continue
      response = http.request('GET', url + x, headers={'User-Agent': utils.random_user_agent()})
    except urllib3.exceptions.HTTPError as err:
      print(f"{Fore.RED}[-]{Style.RESET_ALL} Request failed: {err.reason}")
    print(f"{Fore.BLUE}[*]{Style.RESET_ALL} {url + x} -> {Fore.YELLOW}{response.status}{Style.RESET_ALL}{Style.BRIGHT} '{responses[response.status]}'{Style.RESET_ALL}")

def print_robots_txt(results):
  for x in results["Allowed"]:
    print(f"{Fore.GREEN}{x}{Style.RESET_ALL}")
  for x in results["Disallowed"]:
    print(f"{Fore.RED}{x}{Style.RESET_ALL}")

def print_usage():
  print(f"python3 {sys.argv[0]} <filename>")

def main():
  if len(sys.argv) > 1:
    filename = sys.argv[1]
    open_list(filename)
  else:
    print_usage()

main()
