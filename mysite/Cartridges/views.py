from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UrlForm
from django.db import models
from .models import Url
from .models import ServiceHistory
from .models import ProductionHistory
from .models import Specs
from .models import BallisticPerformance
import re
import wikipedia
from bs4 import BeautifulSoup
import sys
import json
import urllib.request, urllib.parse, urllib.error
from elasticsearch import Elasticsearch
import random
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def Success(request):
     return HttpResponse("Success! HELL YEEAH")

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
                                Indexable.append(Urls[i])
                
        return Indexable



def Daemon(numOptions,ManualURL):
    Urls = Fetch(numOptions)
    for obj in Url.objects.all():
        if obj.href in Urls:
            Urls.remove(obj.href)          
    for i in range(0,len(Urls)):
        URL = Url(href=str(Urls[i]))
        URL.save()
    for obj in Url.objects.all():
        try:
            if obj.href == ManualURL.href:
                Url.objects.filter(href=ManualURL.href).delete()
            PullData("lxml",str(obj.href))
        except:
            continue


def get_urls(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UrlForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
                URL = Url(href=form.cleaned_data.get('Url'))
                Daemon(100,URL)
                return HttpResponseRedirect('/Cartridges/validate/')


    else:
        form = UrlForm()

    return render(request, 'name.html', {'form': form})

def PullData(PARSER_TYPE,page):
    #try:
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
                       if(len(Data[i]) == 3):
                           BP["Bullet mass/type"] = Data[i][0]
                           BP["Velocity"] = Data[i][1]
                           BP["Energy"] = Data[i][2]
                       elif(len(Data[i]) == 2):
                           BP["Bullet mass/type"] = Data[i][0]
                           BP["Bullet mass/type"] = Data[i][1]
                       else:
                           BP["Bullet mass/type"] = Data[i][0]

    return BP

def CheckDuplicates(Cartridge_Name):
    for obj in ServiceHistory.objects.all():
        if obj.Cartridge_Name == Cartridge_Name:
            obj.delete()
    for obj in ProductionHistory.objects.all():
        if obj.Cartridge_Name == Cartridge_Name:
            obj.delete()
    for obj in Specs.objects.all():
        if obj.Cartridge_Name == Cartridge_Name:
            obj.delete()
    for obj in BallisticPerformance.objects.all():
        if obj.Cartridge_Name == Cartridge_Name:
            obj.delete()
def Put(Data):
                es = Elasticsearch()
                try:
                    Cartridge_Name = Data[0][0]
                except:
                    Cartridge_Name = ""
                #Type = Data[2][1]
                #POF = Data[3][1]
                try:
                    Type = Data[1][1]
                except:
                    Type = ""
                try:
                    POF = Data[2][2]
                except:
                    POF = ""
                Service_history = {"Used by" : " ", "In service" : " "}
                Production_history = {"Designer" : " ","Designed" : " ","Manufacturer" : " ","Produced" : " ","Variants" : " "}
                Specifications = {"Parent case": " ","Case type": " ","Bullet diameter" : " ","Neck diameter": " ","Shoulder diameter": " ","Base diameter" : " ","Rim diameter": " ", \
                                        "Rim thickness": " ","Case length": " ","Overall length" : " ","Case capacity": " ","Rifling twist": " ","Primer type": " ","Maximum pressure": " "}
                Ballistic_performance = {"Bullet mass/type" : " ", "Velocity": " ","Energy": " "}
                 
                for items in Data:
                        for i in range(len(items) - 1):
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

                Ballistic_performance = Process_Ballistic_Data(Data,Ballistic_performance)
                Service_History = ServiceHistory(Cartridge_Name=Cartridge_Name,Used_by=Service_history["Used by"],In_Service=Service_history["In service"])
                Production_History = ProductionHistory(Cartridge_Name=Cartridge_Name,Designer=Production_history["Designer"],Designed=Production_history["Designed"],Manufacturer=Production_history["Manufacturer"],Produced=Production_history["Produced"],Variants=Production_history["Variants"])
                Specifications_ = Specs(Cartridge_Name=Cartridge_Name,Parent_case=Specifications["Parent case"],Case_type=Specifications["Case type"],Bullet_diameter=Specifications["Bullet diameter"], \
                                                    Neck_diameter=Specifications["Neck diameter"],Shoulder_diameter=Specifications["Shoulder diameter"],Base_diameter=Specifications["Base diameter"],Rim_diameter=Specifications["Rim diameter"],Rim_thickness=Specifications["Rim thickness"], \
                                                    Case_length=Specifications["Case length"], Overall_length=Specifications["Overall length"],Case_capacity=Specifications["Case capacity"],Rifling_twist=Specifications["Rifling twist"],Primer_type=Specifications["Primer type"],Maximum_pressure=Specifications["Maximum pressure"])
                Ballistic_Performance = BallisticPerformance(Cartridge_Name=Cartridge_Name,Bullet_mass_type=Ballistic_performance["Bullet mass/type"],Velocity=Ballistic_performance["Velocity"],Energy=Ballistic_performance["Energy"])                    
                CheckDuplicates(Cartridge_Name)
                Service_History.save()
                Production_History.save()
                Specifications_.save()
                Ballistic_Performance.save()
                Spec_Mappings = {
                    
                    }
                Service_Mappings = {

                    }
                Ballistic_Performance_Mappings = {
                    }
            
                DataPoints = {
                'Name': Cartridge_Name,
                'Type': Type, 'Place of Origin': POF,
                'Service history': {
                    'Used by' :Service_history["Used by"],
                    'In service' : Service_history["In service"] } ,
                'Production_history': { 'Designer': Production_history["Designer"],
                                        'Designed' : Production_history["Designed"],
                                        'Manufacturer' : Production_history["Manufacturer"],
                                        'Produced' : Production_history["Produced"],
                                        'Variants' : Production_history["Variants"],
                    },
                'Specifications': { 'Parent case' : Specifications["Parent case"],
                                    'Case type' : Specifications["Case type"],
                                    'Bullet diameter' : Specifications["Bullet diameter"],
                                    'Neck diameter' : Specifications["Neck diameter"],
                                    'Shoulder diameter': Specifications["Shoulder diameter"],
                                    'Base diameter' : Specifications["Base diameter"],
                                    'Rim diameter' : Specifications["Rim diameter"],
                                    'Rim thickness' : Specifications["Rim thickness"],
                                    'Case length' : Specifications["Case length"],
                                    'Overall length' : Specifications["Overall length"],
                                    'Case capacity' : Specifications["Case capacity"],
                                    'Rifling twist' : Specifications["Rifling twist"],
                                    'Primer type' : Specifications["Primer type"],
                                    'Maximum pressure' : Specifications["Maximum pressure"],
                                
                                                                      
                                    
                    },
                'Ballistic_Performance' : {
                                    'Bullet mass/type': Ballistic_Performance["Bullet mass/type"],
                                    'Velocity' : Ballistic_Performance["Velocity"],
                                    'Energy': Ballistic_Performance["Energy"],

                    }}

                """
                Consider bulk indices, potentially better design decision. 
                """
                random.seed(None)
                string = "index" + random.random()
                res = es.index(index=string, doc_type='tweet', id=1, body=DataPoints)
                return
