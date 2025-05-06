from PY_YOUTUBE_SEARCH_ssmool import GetSearchList

def Contiue():
   choice = input("Continue [ 0 - YES, 1 - NO ]:")
   if(choice != '0' or lower(choice) == 'yes' or lower(choice) == 'y'):
      AppStart()
   if(choice == '1' or lower(choice) == 'no' or lower(choice) == 'n'):
      print('By, PY_YOUTUBE_SEARCH quited!')

def AppStart():
    max_results = 20
    query = input("Search by videos(Youtube API):")
    GetSearchList(query, max_results)
    Continue()

AppStart()