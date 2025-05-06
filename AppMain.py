#by:asytrick
#github:ssmool
from PY_YOUTUBE_SEARCH_ssmool import GetSearchList

#GLOBAL VARIABLES
lst = []

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
   if(choice.lower() == 'q' or choice.lower() == 'QUIT' or choice.lower() == 'EXIT'):
      print('By, PY_YOUTUBE_SEARCH quited!')

def AppStart():
    lst.clear()
    max_results = 20
    query = input("Search by videos(Youtube API):")
    GetSearchList(query, max_results)

AppStart()
