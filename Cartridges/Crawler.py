"""
At present, we have a few costly lookups in our loop that take between 2 - 5 mins
to verify and index relevant urls in a sample size of 10,000 Urls
We mitigate this by creating a cron job on our native system.
We will experiment with threading in later revisions, to try to speed up
this process. 
---------------------------------
Instructions for running a daemon
#!bin/sh
crontab -e;
#minute hour day-of-month month day-of-week command /path/to/pythonscript
--------------------------------
"""
#Python Crawler#
import re
from bs4 import BeautifulSoup
from mysql.connector import MySQLConnection, Error
import urllib.request, urllib.parse, urllib.error
import wikipedia
import sys
#BINARY ARMS
#(c) CRAWLER v 1.0 ALPHA
#IMPLEMENT THREADING, HAVE CRAWLER AS A DAEMON
#We will index all Url's with a description pane, and the name Cartridge
#OPTIMIZE AND INTREGRTE WITH DJANGO
def GetUrls():
        Urls = []
        List = wikipedia.search("Cartridges",results=int(sys.argv[1]))
        for i in range(len(List) - 1):
                try:
                        All = wikipedia.page(List[i])
                        Urls.append(All.url) 
                except:
                        continue
                                
        return Urls
                                            
def Fetch():
        Urls = GetUrls()
        Indexable = []
        for i in range(len(Urls) - 1):
                page = urllib.request.urlopen(Urls[i]).read()
                soup = BeautifulSoup(page,"lxml")
                if soup.find("table", {"class": "infobox"}) == None:
                        continue
                else:
                        soup = soup.find("table", {"class": "infobox"})
                        soup = soup.getText()
                        pattern = '(Service history|Production history|Specifications|Ballistic performance)'
                        if len(re.findall(pattern,soup)) > 0:
                                Indexable.append(Urls[i]) 
                
        return Indexable

print(Fetch())
