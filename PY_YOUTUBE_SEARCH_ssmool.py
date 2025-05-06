#by:asytrick
#github:ssmool
import os
import webbrowser
import requests
import json
import urllib
from urllib.parse import quote_plus

def youtube_search(query, max_results=10):
    # Configure a API key e o serviço da API
    api_service_name = "youtube"
    api_version = "v3"
    #PLEASE FOR USE REGISTER YOUR YouTube Data API v3 Credencial API KEY
    api_key = "YouTube Data API v3 KEY"
    query = query.replace(' ','_')
    api_uri = str(f'https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q={ query}&key={api_key}')
    results = []
    print(api_uri)
    r = urllib.request.urlopen(str(api_uri))
    data = json.loads(r.read())
    data_list = data["items"]
    for item in data_list:
        video_title = item['snippet']['title']
        try:
              video_id = item['id']['videoId']
        except:
              video_id = item['id']['channelId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        results.append({'title': video_title, 'url': video_url})
    return results

def GetSearchList(query, max_results=10):
    lst = []
    index = 0
    results = youtube_search(query)
    for idx, video in enumerate(results):
        print(f"{idx + 1}. {video['title']}: {video['url']}")
        lst.append([{idx}, {idx + 1}, {video['title']}, {video['url']}])
    choice = input("Choice your video to open:")
    content = lst[int(choice)]
    api_addr = str(content[3])
    api_addr = api_addr.replace("{","").replace("'","")
    webbrowser.open(api_addr)
