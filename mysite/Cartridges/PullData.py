import re
import wikipedia
from bs4 import BeautifulSoup
import sys
import json
import urllib.request, urllib.parse, urllib.error
def PullData(PARSER_TYPE,page):
#    try:
        page = urllib.request.urlopen(page).read()
        soup = BeautifulSoup(page,"lxml")
        soup = soup.findAll("table", {"class": "infobox"})
        for Soup in soup:
            text = Soup.getText()
            pattern = "(.*)"
            matches = re.findall(pattern,text)
            ProcessList(matches)
            Soup = Soup.findAll("a")
            for link in Soup:
                if(str(link) == '<a href="/wiki/Cartridge_(firearms)" title="Cartridge (firearms)">case</a>'):
                    index = Soup.index(link)
                    string = str(Soup[index + 1])
                    pattern = "(href=\")((.*)(\"\s))"
                    if(len(re.findall(pattern,string)) > 0):
                        link = re.findall(pattern,string)[0][2]
                        protocol = "https://"
                        domain = "en.wikipedia.org"
                        link = protocol + domain + link
                        PullData("lxml",link)
                    else:

                        return

#BINARY ARMS
#(c) CRAWLER v 1.0 ALPHA
#IMPLEMENT THREADING, HAVE CRAWLER AS A DAEMON
#We will index all Url's with a description pane, and the name Cartridge
#OPTIMIZE AND INTREGRTE WITH DJANGO
def GetUrls(NUMURLS):
        Urls = []
        List = wikipedia.search("Cartridges",NUMURLS)
        for i in range(len(List) - 1):
                try:
                        All = wikipedia.page(List[i])
                        Urls.append(All.url) 
                except:
                        continue
                                
        return Urls
"""                                           
def Fetch(NUMURLS):
        Urls = GetUrls(NUMURLS)
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
                                URL = Url(href=Urls[i])
                                URL.save()
                
        return Indexable

"""
def ProcessList(matches):
    Seperator = 0
    Data = []
    n=0
    for i in range(len(matches) - 1):
        matches[i] = re.sub('\\u00a0', ' ',matches[i])
        if(len(Data) == 0 and matches[i] != ''):
                Data.append([])
                Data[n].append(matches[i])
        elif(matches[i] == ''):
                Seperator=Seperator+1
        elif(matches[i] != '' and Seperator == 1):
                Data[n].append(matches[i])
                Seperator = 0
        elif(matches[i] != '' and Seperator > 2):
                Data.append([])
                Data[n+1].append(matches[i])
                n=n+1
                Seperator = 0
    return Put(Data)


def Process_Ballistic_Data(Data,BP):
        Length = len(Data)
        for item in Data :
                for items in item:
                        if(items in BP.keys()):
                                Index = Data.index(item)
                        if('Source(s):' in items):
                                Length = Length - 1
                        
        for i in range(Index + 1,Length):
                BP["Bullet mass/type"] = Data[i][0]
                BP["Velocity"] = Data[i][1]
                BP["Energy"] = Data[i][2]
        return BP

                     
def Put(Data):
                #es = Elasticsearch()
                Cartridge_Name = Data[0][0]
                Type = Data[1][0]
                POF = Data[2][0]                
                Service_history = {"Used by" : " ", "In service" : " "}
                Production_history = {"Designer" : " ","Designed" : " ","Manufacturer" : " ","Produced" : " ","Variants" : " "}
                Specifications = {"Parent case": " ","Case type": " ","Bullet diameter" : " ","Neck diameter": " ","Shoulder diameter": " ","Base diameter" : " ","Rim diameter": " ", \
                                        "Rim thickness": " ","Case length": " ","Overall length" : " ","Case capacity": " ","Rifling twist": " ","Primer type": " ","Maximum pressure": " "}
                Ballistic_performance = {"Bullet mass/type" : " ", "Velocity": " ","Energy": " "}
                 
                for items in Data:
                        for i in range(len(items) - 2):
                                if(items[i] in Service_history.keys()):
                                        key = items[i]
                                        item = items[i + 1]
                                        Service_history[key] = item              
                                elif(items[i] in Production_history.keys()):
                                        key = items[i]
                                        item = items[i + 1]
                                        Production_history[key] = item
                                elif(items[i] in Specifications.keys()):
                                        key = items[i]
                                        item = items[i+1]
                                        Specifications[key] = item
                """

                Ballistic_performance = Process_Ballistic_Data(Data,Ballistic_performance)
                Service_History = ServiceHistory(Cartridge_Name=Cartridge_Name,Used_by=Service_history["Used by"],In_Service=Service_history["In service"])
                Production_History = ProductionHistory(Cartridge_Name=Cartridge_Name,Designer=Production_history["Designer"],Designed=Production_history["Designed"],Manufacturer=Production_history["Manufacturer"],Produced=Production_history["Produced"],Variants=Production_history["Variants"])
                Specifications_ = Specs(Cartridge_Name=Cartridge_Name,Parent_case=Specifications["Parent case"],Case_type=Specifications["Case type"],Bullet_diameter=Specifications["Bullet diameter"], \
                                                    Neck_diameter=Specifications["Neck diameter"],Shoulder_diameter=Specifications["Shoulder diameter"],Base_diameter=Specifications["Base diameter"],Rim_diameter=Specifications["Rim diameter"],Rim_thickness=Specifications["Rim thickness"], \
                                                    Case_length=Specifications["Case length"], Overall_length=Specifications["Overall length"],Case_capacity=Specifications["Case capacity"],Rifling_twist=Specifications["Rifling twist"],Primer_type=Specifications["Primer type"],Maximum_pressure=Specifications["Maximum pressure"])
                Ballistic_Performance = BallisticPerformance(Cartridge_Name=Cartridge_Name,Bullet_mass_type=Ballistic_performance["Bullet mass/type"],Velocity=Ballistic_performance["Velocity"],Energy=Ballistic_performance["Energy"])
                Service_History.save()
                Production_History.save()
                Specifications_.save()
                Ballistic_Performance.save()
                """
                """"
                DataPoints = {
                'Name': str(Cartridge_Name),
                'Type': str(Type), 'Place of Origin': str(POF),
                'Service history': Service_history,
                'Production_history': Production_history,
                'Specifications': Specifications,
                        }
                res = es.index(index='entry', doc_type='Cartridge', id=1, body=DataPoints)
                """
PullData("lxml","https://en.wikipedia.org/wiki/.375_H%26H_Magnum")
