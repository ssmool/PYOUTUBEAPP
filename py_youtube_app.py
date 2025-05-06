#by:asytrick
#github:ssmool
import os
import webbrowser
import requests
import json
import urllib
from urllib.parse import quote_plus

#GLOBAL VARIABLES
lst = []

def youtube_search(query, max_results=10):
    # Configure a API key e o serviço da API
    api_service_name = "youtube"
    api_version = "v3"
    #PLEASE FOR USE REGISTER YOUR YouTube Data API v3 Credencial API KEY
    api_key = "API SECRET KEY"
    query = query.replace(' ','_')
    api_uri = str(f'https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q={ query}&key={api_key}')
    results = []
    print(api_uri)
    r = urllib.request.urlopen(str(api_uri))
    data = json.loads(r.read())
    data_list = data["items"]
    for item in data_list:
        r = False
        try:
              video_id = item['id']['videoId']
              r = True
        except:
              r = False
        if(r):
              video_title = item['snippet']['title']
              video_url = f"https://www.youtube.com/watch?v={video_id}"
              results.append({'title': video_title, 'url': video_url})
              r = False
    return results

def GetSearchList(query, max_results=10):
    index = 0
    results = youtube_search(query)
    for idx, video in enumerate(results):
        print(f"{idx + 1}. {video['title']}: {video['url']}")
        lst.append([{idx}, {idx + 1}, {video['title']}, {video['url']}])
    GetChoice()

def GetChoice():
    lst_max = str(len(lst))
    choice = input(f"Choice your video to open[0 - {lst_max} : C - New Search]:")
    if(choice.lower() == 'c' or choice.lower() == 'continue' or choice == '' or type(int(choice)) != type(0) ):
        AppStart()
    else:
        index = int(choice)
        index -= 1
        if(index > 0 or index < int(lst_max)):
            content = lst[index]
            api_addr = str(content[3])
            api_addr = api_addr.replace("{","").replace("'","")
            webbrowser.open(api_addr)
            Continue()


def Continue():
   choice = input("New Search [ 0 - YES, 1 - NO, Q - Exit ]:")
   if(choice == '0' or choice.lower == 'yes' or choice.lower == 'y'):
      AppStart()
   if(choice == '1' or choice.lower == 'no' or choice.lower == 'n'):
      GetChoice()
   if(choice.lower() == 'Q' or choice.lower() == 'QUIT' or choice.lower() == 'EXIT'):
      print('By, PY_YOUTUBE_SEARCH quited!')

def AppStart():
    lst.clear()
    max_results = 20
    query = input("Search by videos(Youtube API):")
    GetSearchList(query, max_results)

AppStart()