#!/usr/bin/env python3

import cfscrape
from lxml import html
import argparse
import os

request = cfscrape.create_scraper(delay=10)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Revwho():
    def __init__(self):
        self.row = dict()
        self.terms = list()

    def setTerms(self, terms):
        self.terms = terms

    def search(self):
        for term in self.terms:
            r = request.get(f"https://viewdns.info/reversewhois/?q={term.replace(' ', '+')}")
            root = html.fromstring(r.text)
            ex = '/html/body/font/table[2]/tr[3]/td/font/table'
            if root.xpath(ex):
                for _ in root.xpath(ex)[0].getchildren()[1:]:
                    domain = _.getchildren()[0].text
                    if _.getchildren()[1].text:
                        date = _.getchildren()[1].text
                    else:
                        date = ""

                    if _.getchildren()[2].text:
                        registrar = _.getchildren()[2].text
                    else:
                        registrar = ""

                    self.row[domain] = [date, registrar]

        self.total = len(self.row)

    def verbose(self):
        header = f'{self.total} domains found for {", ".join(self.terms)}.'
        header += '\nDomain Name              Creation Date    Registrar'
        print(bcolors.OKBLUE + header + bcolors.ENDC)
        if self.total: print(bcolors.FAIL + '='*60 + bcolors.ENDC)

        for domain, (date, registrar) in self.row.items():
            print("{0}{1:25}{2:17}{3}{4}".format(bcolors.OKGREEN, domain, date, registrar, bcolors.ENDC))

def banner():
    os.system('clear')
    print(bcolors.HEADER + '''
  https://twitter/0xc0d   _
 _ __ _____   ____      _| |__   ___
| '__/ _ \ \ / /\ \ /\ / / '_ \ / _ \\
| | |  __/\ V /  \ V  V /| | | | (_) |
|_|  \___| \_/    \_/\_/ |_| |_|\___/
    ''' + bcolors.ENDC)

def main():


    banner()
    print()
    print("Enter Name and/or Email to search for domain")
    terms = list()
    while not len(terms):
        name = input("Name: ")
        if name:
            terms.append(name)
        email = input("Email: ")
        if email:
            terms.append(email)

    query = Revwho()
    query.setTerms(terms)
    query.search()
    query.verbose()

if __name__ == "__main__":
    main()
