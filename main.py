import sys, locale
import os
os.system('cls' if os.name == 'nt' else 'clear')
import locale
import requests
locale.setlocale( locale.LC_ALL, 'en_CA.UTF-8' )
platform = input("PC or Console? ")
reigon = input("NAE, NAW, EU, OCE, BR, ASIA, or ME? ")
epickinda = input("What is their IGN? ")
epic = epickinda.replace(" ", "%20")
url = 'https://api.fortnitetracker.com/v1/powerrankings/' + platform + '/' + reigon + '/' + epic
headers = {"TRN-Api-Key": "634c7595-c781-46af-9ef3-18e65793244c"}
r = requests.get(url, headers=headers)
pr = r.text
pr = pr.split("points")[1]
pr = pr.split(",\r\n  \"cashPrize\"")[0]
pr = pr.split("\": ")[1]
pr = float(pr)
pr = (locale.format("%d", pr, grouping=True))
ce = r.text
ce = ce.split("cashPrize")[1]
ce = ce.split(",\r\n  \"events")[0]
ce = ce.split("\": ")[1]
ce = float(ce)
ce = (locale.currency(ce, grouping=True))
rn = r.text
rn = rn.split("rank")[1]
rn = rn.split(",\r\n  \"percentile\"")[0]
rn = rn.split('\": ')[1]
rn = float(rn)
rn = (locale.format("%d", rn, grouping=True))
ep = r.text
ep = ep.split("events")[1]
ep = ep.split(',\r\n  \"rank\"')[0]
ep = ep.split('\": ')[1]
ep = float(ep)
ep = (locale.format("%d", ep, grouping=True))
os.system('cls' if os.name == 'nt' else 'clear')
print("PR: " + pr)
print("Earnings: " + ce)
print("Rank: " + rn)
print("Events Played: " + ep)
input("Press something to end process       ")
