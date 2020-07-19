# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:44:23 2020

@author: RDxR10
"""

import time
import urllib.request
import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
def extract_google_dorks(start_n,end_n):
    failed_attempts_counter=0
    log_file_name = "GhdbResults " + str(start_n) + "_" + str(end_n) + ".txt"
    log_file = open(log_file_name,"a")
#def is_downloadable(url):

    #h = requests.head(url, allow_redirects=True)
    #header = h.headers
    #content_type = header.get('content-type')
    #if('text' in content_type.lower()):
        #return False
    #if('html' in content_type.lower()):
        #return False
    #else:
        #return True

    for i in range(start_n,end_n):
        current_url = "http://www.exploit-db.com/ghdb/" + str(i) + "/"
        print("Fetching... exists.." + current_url)
        #if print(is_downloadable(current_url))==True:
        r=requests.get(current_url, allow_redirects=True)
        open('ghdb.txt','wb').write(r.content)
    try:
        item_request=urllib.request.Request(current_url)
        item_request.add_header('user-agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Mobile Safari/537.36')
        item_response = urllib.request.urlopen(item_request, timeout=7)
        item_content = item_response.read()
        parsed_html = BeautifulSoup(item_content, features="lxml")
        table = parsed_html.body.find('table', {'class':'category-list'})
        first_td = table.findChild('td')
        html_parser = HTMLParser.HTMLParser()
        #Extract Google Dorks Data
        item_google_dork_td = first_td.findNext('td')
        item_google_dork = "Google Dork: " + item_google_dork_td.find('a').get('href') + "\n"
        item_date_added_td= item_google_dork_td.findNext('td')
        item_google_dork = "Google Dork: " + item_google_dork_td.find('a').get('href') + "\n"
        item_date_added_td = item_google_dork_td.findNext('td')
        item_date_added = html_parser.unescape(item_date_added_td.text) + "\n"
        item_desc_td = item_date_added_td.findNext('td')
        item_desc = "Description: " + html_parser.unescape(item_desc_td.text) + "\n"

        log_file.write(item_date_added + item_desc + item_google_dork + "\n------")
        item_response.close()
        failed_attempts_counter=1
        print("[+] FINISHED")

    except Exception as e:
        print("Exception" + str(e))
        print("ERROR! Trying in 3 seconds...")
        time.sleep(3)
        failed_attempts_counter+=1

        if failed_attempts_counter==5:
            print("Something is wrong..exiting..")
            log_file.close()
            exit(0)
    log_file.close()
    print("[+] Done")
def main():
    extract_google_dorks(900,906)
if __name__ == '__main__':
    main()
