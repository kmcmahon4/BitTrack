#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 17:10:03 2021
@author: kerrimcmahon
"""

import requests
from bs4 import BeautifulSoup

def priceTracker():
    url = 'https://finance.yahoo.com/quote/BTC-USD/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAFmo-QfIFFy4Oc0Fq-EhRL7Aj2nWkEkJkap_QAaT0PrzY9tuKlswcN3fh28vZrMe9okT0kEBZfwbIZ9W03NugwjwmHf9NEICryUF_M5POHVmpSJgBOxMS5vvC_VO6sovJ9-w9scXRU37QmIUzfJDXYDyazeEknZvlilRi50uIlHK'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    price = soup.find_all('div', {'class':'D(ib) smartphone_Mb(10px) W(70%) W(100%)--mobp smartphone_Mt(6px)'})[0].find('span').text
    return price
 
while True:   
    print('Current price of BTC: $' +priceTracker())