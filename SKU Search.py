from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from lxml import html
import os
import time
from datetime import datetime 
import requests
import pandas as pd
import math


def createWebDriver(DownloadPath=os.getcwd()):
    DriverPref = webdriver.FirefoxProfile()
    DriverPref.set_preference("browser.download.folderList",2)# 0 means to download to the desktop, 1 means to download to the default "Downloads" directory, 2 means to use the directory you specify in "browser.download.dir"
    DriverPref.set_preference("browser.download.manager.showWhenStarting",False)
    DriverPref.set_preference('browser.download.dir', DownloadPath)
    DriverPref.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/csv")
    Driver = webdriver.Firefox(firefox_profile=DriverPref)
    return Driver

##Refrigirator
##SKUs=['WRF535SMBM','WRX735SDBM','WRB322DMBM','WRS325FDAM','WRT311FZDW','WRT318FMDW','WRF736SDAM','WRF560SEYM','WRT111SFDW','WRX988SIBM',
##      'WRS325FNAM','WRB119WFBM','WRT519SZDM','WRS571CIDM','WRS322FDAM','WRF757SDEM','WRT318FZDW','WRF540CWBM','WRB329DMBM','WRS576FIDM',
##      'WRS322FNAM','WRF532SMBM','WRF57R18DM','WRT314TFDW','WRT104TFDW','WRS973CIDM','WRS586FIEE','WRF560SMYM','WRT138FZDW','WRT108FZDW',
##      'WRT541SZDM','WRT106TFDW','WRT549SZDW','WRT316SFDM','WRF535SWBM','WRT134TFDW','WRV976FDEM','WRS342FIAM','WRF997SDDM','WRS975SIDM',
##      'WSR57R18DM','WRS970CIDM','WRS335FDDW','WRV986FDEM','WRS331FDDM','WRV996FDEH','WFE515S0ES','WZF79R18DM','WDF520PADM','WSZ57L18DM',
##      'WDT780SAEM','WFC310S0ES','WFG540H0ES','WFE510S0AS','WRF989SDAM','WRT771REYM','WRT3L1SZYB','GSC25C6EYY','WRT111SFAW','WRT359SFYM',
##      'WRT771RWYW','WRS586FIDE','WRT138TFYS','WRS526SIAE','WRT108TFYW','WRS965CIAE','GI0FSAXVY','4378411RB','GI6FARXXY','W5TXEWFWQ',
##      'EL88TRRWS','W4TXNWFWQ','W8RXNGMBD','W6TXNWFWQ','W8TXNGZBB','W5TXEWFWB','W8TXEWFYQ','W8TXNWMBB','W8TXNWFBT','WRT511SZDW']

##Washer
##SKUs=['WTW4815EW','WTW7000DW','WFW72HEDW','WTW5000DW','WTW7300DW','WFW87HEDW','WFW95HEDC','WTW4850BW','WFC7500VW','WTW5800BW',
##      'CAE2743BQ','WTW8500DC','WTW8000DW','CAE2793BQ','CHW9050AW','WFL98HEBU','WFW97HEDC','WFW81HEDW','CHW9060AW','WTW4800BQ',
##      'WTW8500BW','WTW8000BW']


##Dryer
##SKUs=['WED72HEDW','WED4815EW','WED5000DW','8212487RP','WED7000DW','WGD72HEDW','WED7300DW','WGD4815EW','WET4024EW','WET4027EW',
##      'LTG5243DQ','WGT4027EW','WED7500VW','CEM2743BQ','CGM2743BQ','LDR3822PQ','CEM2793BQ','WED8500DC','CED9050AW','WED4850BW',
##      'CGD9050AW','CED9060AW','WGD5000DW','WGD7000DW','WED87HEDW','WED95HEDW','LER3622PQ','WED5800BC','WGD8500DC','WGD95HEDW',
##      'WGT3300XQ','WET3300XQ','WED4800BQ','WED4800XQ','WGD4800BQ','WFW88HEAW','WED9051YW','WFW94HEAC','WFW86HEBC','WFW96HEAW','49971']
SKUs=['CAE2743BQ','CAE2793BQ','CHW9050AW','CHW9060AW','ED5KVEXV[Q]','GI0FSAXV[Y]','GI0FSAXVY','GX5FHDXV[ ]','GX5FHTXV[Q]','WDF520PADM','WDT780SAEM',
'WFC310S0ES','WFC7500VW','WFE510S0AS','WFE515S0ES','WFG540H0ES','WFL98HEBU','WFW72HEDW','WFW81HEDW','WFW8740DW','WFW87HEDW','WFW88HEAW',
'WFW95HEDC','WFW95HEDW','WFW97HEDC','WRB119WFBM','WRB322DMBM','WRB329DMBM','WRF532SMBM','WRF535SMBM','WRF535SWBM','WRF540CWBM','WRF560SEY[M]',
'WRF560SEYM','WRF560SMYM','WRF57R18DM','WRF736SDAM','WRF757SDEM','WRF989SDA[H]','WRF989SDAM','WRF991BOOM','WRF997SDDM','WRL767SIAM',
'WRS321CDBM','WRS322FDAM','WRS322FNAM','WRS325FDAM','WRS325FNAM','WRS331FDDM','WRS335FDDW','WRS342FIAM','WRS571CIDM','WRS576FIDM','WRS586FIEE',
'WRS950SIAM','WRS970CIDM','WRS973CIDM','WRS975SIDM','WRT104TFDW','WRT106TFDW','WRT108FZDW','WRT111SFDW','WRT134TFDW','WRT138FZDW',
'WRT311FZDW','WRT314TFDW','WRT316SFDM','WRT318FMDM','WRT318FMDW','WRT318FZDW','WRT511SZDM','WRT511SZDW','WRT519SZDM','WRT541SZDM',
'WRT549SZDM','WRT549SZDW','WRV976FDEM','WRV986FDEM','WRV996FDEH','WRX735SDBM','WRX988SIBM','WSF26C2EX[W]','WSR57R18DM','WSZ57L18DM',
'WTW4815EW','WTW4850BW','WTW4915EW','WTW5000DW','WTW5500BW','WTW5800BW','WTW7000DW','WTW7040DW','WTW7300DW','WTW7340DW','WTW8000DW',
'WTW8040DW','WTW8500DC','WTW8500DW','WZF79R18DM']

df_ASIN=pd.DataFrame()
Driver=createWebDriver()
Driver.get("http://www.amazon.com")
Driver.find_element_by_id("redir-opt-out-label").click()
Driver.find_element_by_id("redir-stay-at-www").click()
n=1
for SKU in SKUs:
    print str(n)+':'+SKU
    Driver.find_element_by_id("twotabsearchtextbox").clear()
    Driver.find_element_by_id("twotabsearchtextbox").send_keys(SKU)
    time.sleep(5)
    Driver.find_element_by_class_name("nav-input").click()
    time.sleep(5)
    try:
        URL=Driver.find_element_by_id("result_0").find_element_by_css_selector(".a-link-normal.s-access-detail-page.a-text-normal").get_attribute("href")
        if SKU in URL.split('/')[3]:
            df_ASIN=df_ASIN.append({'SKU':SKU,'URL':URL,'Poduct_Name':URL.split('/')[3],'ASIN':URL.split('/')[5]},ignore_index=True)
            print SKU+':Found'
        else:
            df_ASIN=df_ASIN.append({'SKU':SKU,'URL':'','Poduct_Name':'','ASIN':''},ignore_index=True)
    except Exception as e:
        df_ASIN=df_ASIN.append({'SKU':SKU,'URL':'','Poduct_Name':'','ASIN':''},ignore_index=True)
    time.sleep(1)
    n=n+1

Driver.close()
##writer = pd.ExcelWriter(os.getcwd()+'\\Refrigirator.xlsx', engine='xlsxwriter')
##writer = pd.ExcelWriter(os.getcwd()+'\\Washer.xlsx', engine='xlsxwriter')
##writer = pd.ExcelWriter(os.getcwd()+'\\Dryer.xlsx', engine='xlsxwriter')
writer = pd.ExcelWriter(os.getcwd()+'\\skulist.xlsx', engine='xlsxwriter')
print 'here'
df_ASIN.to_excel(writer, sheet_name='Sheet1')
print 'here2'
print df_ASIN

