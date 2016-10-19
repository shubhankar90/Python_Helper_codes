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
from random import randint

##Title Page###########################################################################################
def ret_prod_title (soup):
    if soup.find(id="productTitle")!=None:
        return soup.find(id="productTitle").text
    else:
        return ''

def ret_prod_ourprice (soup):
    if soup.find(id="priceblock_ourprice")!=None:
        return float(soup.find(id="priceblock_ourprice").text[1:].replace(',',''))
    else:
        return ''

    
def ret_prod_origprice (soup):
    if soup.find(class_="a-span12 a-color-price a-size-base")!=None:
        return float(soup.find(class_="a-span12 a-color-price a-size-base").text[1:8].replace(',',''))
    else:
        return ret_prod_ourprice(soup)

 

def ret_promotions (soup):
    if soup.find(id="quickPromoBucketContent")!=None:
        return soup.find(id="quickPromoBucketContent").text.replace("\n"," ")
    else:
        return ''

def ret_revcount (soup):
    if soup.find(id="summaryStars")!=None:
        return soup.find(id="summaryStars").text.replace(' ','').replace('\n','')
    else:
        return '0'

def ret_revrating (soup):
    if soup.find(id="avgRating")!=None:
        return soup.find(id="avgRating").text.replace(' ','').replace('\n','')[0:3].strip()
    else:
        return '0'

def ret_rev5percent (soup):
    if soup.find(id="histogramTable")!=None:
        if soup.find(id="histogramTable").find_all(class_="a-histogram-row")[0]!=None:
            if soup.find(id="histogramTable").find_all(class_="a-histogram-row")[0].find_all(class_="a-nowrap")[1]!=None:
                if soup.find(id="histogramTable").find_all(class_="a-histogram-row")[0].find_all(class_="a-nowrap")[1].find(class_="a-link-normal")!=None:
                    return soup.find(id="histogramTable").find_all(class_="a-histogram-row")[0].find_all(class_="a-nowrap")[1].find(class_="a-link-normal").text[:-1]
                else:
                    return ''
            else:
                return ''
        else:
            return ''
    else:
        return ''

def ret_rev4percent (soup):
    if soup.find(id="histogramTable")!=None:
        if soup.find(id="histogramTable").find_all(class_="a-histogram-row")[1]!=None:
            if soup.find(id="histogramTable").find_all(class_="a-histogram-row")[1].find_all(class_="a-nowrap")[1]!=None:
                if soup.find(id="histogramTable").find_all(class_="a-histogram-row")[1].find_all(class_="a-nowrap")[1].find(class_="a-link-normal")!=None:
                    return soup.find(id="histogramTable").find_all(class_="a-histogram-row")[1].find_all(class_="a-nowrap")[1].find(class_="a-link-normal").text[:-1]
                else:
                    return ''
            else:
                return ''
        else:
            return ''
    else:
        return ''

def ret_rev3percent (soup):
    if soup.find(id="histogramTable")!=None:
        if soup.find(id="histogramTable").find_all(class_="a-histogram-row")[2]!=None:
            if soup.find(id="histogramTable").find_all(class_="a-histogram-row")[2].find_all(class_="a-nowrap")[1]!=None:
                if soup.find(id="histogramTable").find_all(class_="a-histogram-row")[2].find_all(class_="a-nowrap")[1].find(class_="a-link-normal")!=None:
                    return soup.find(id="histogramTable").find_all(class_="a-histogram-row")[2].find_all(class_="a-nowrap")[1].find(class_="a-link-normal").text[:-1]
                else:
                    return ''
            else:
                return ''
        else:
            return ''
    else:
        return ''

def ret_rev2percent (soup):
    if soup.find(id="histogramTable")!=None:
        if soup.find(id="histogramTable").find_all(class_="a-histogram-row")[3]!=None:
            if soup.find(id="histogramTable").find_all(class_="a-histogram-row")[3].find_all(class_="a-nowrap")[1]!=None:
                if soup.find(id="histogramTable").find_all(class_="a-histogram-row")[3].find_all(class_="a-nowrap")[1].find(class_="a-link-normal")!=None:
                    return soup.find(id="histogramTable").find_all(class_="a-histogram-row")[3].find_all(class_="a-nowrap")[1].find(class_="a-link-normal").text[:-1]
                else:
                    return ''
            else:
                return ''
        else:
            return ''
    else:
        return ''

def ret_rev1percent (soup):
    if soup.find(id="histogramTable")!=None:
        if soup.find(id="histogramTable").find_all(class_="a-histogram-row")[4]!=None:
            if soup.find(id="histogramTable").find_all(class_="a-histogram-row")[4].find_all(class_="a-nowrap")[1]!=None:
                if soup.find(id="histogramTable").find_all(class_="a-histogram-row")[4].find_all(class_="a-nowrap")[1].find(class_="a-link-normal")!=None:
                    return soup.find(id="histogramTable").find_all(class_="a-histogram-row")[4].find_all(class_="a-nowrap")[1].find(class_="a-link-normal").text[:-1]
                else:
                    return ''
            else:
                return ''
        else:
            return ''
    else:
        return ''

##Title Page || Selenium for Similar product##############################################################
def ret_SelSimProducts(Driver):
    try:
        val=Driver.find_element_by_id("fallbacksession-sims-feature").find_element_by_class_name("a-carousel").find_elements_by_class_name("a-carousel-card")
    except:
        val=None
    return val

def ret_SelSimProductName(Driver):
    try:
        val=Driver.find_element_by_class_name("p13n-sc-truncate").text.strip()
    except:
        val=''
    return val

def ret_SelSimProductRating(Driver):
    try:
        val=Driver.find_element_by_class_name("a-icon-row").find_element_by_class_name("a-link-normal").get_attribute('title')[0:3]
    except:
        val=''
    return val

def ret_SelSimProductPrice(Driver):
    try:
        val=float(Driver.find_element_by_class_name("a-row").find_element_by_class_name("a-size-base").text.replace('$','').replace(',',''))
    except:
        val=''
    return val

def ret_SelSimProductRating_Count(Driver):
    try:
        val=Driver.find_element_by_class_name("a-icon-row").find_element_by_class_name("a-size-small").text
    except:
        val=''
    return val

##Review Page###########################################################################################
def ret_review_pgchecker (soup):
    if soup.find(id="cm_cr-review_list")!=None:
        return soup.find(id="cm_cr-review_list").text[:17]
    else:
        return 'Sorry, no reviews'

def ret_reviewhead (soup):
    if soup.find(class_="a-size-base a-link-normal review-title a-color-base a-text-bold")!=None:
        return soup.find(class_="a-size-base a-link-normal review-title a-color-base a-text-bold").text
    else:
        return ''

def ret_reviewauthor (soup):
    if soup.find(class_="a-size-base a-link-normal author")!=None:
        return soup.find(class_="a-size-base a-link-normal author").text
    else:
        return ''

def ret_reviewdate (soup):
    if soup.find(class_="a-size-base a-color-secondary review-date")!=None:
        return str(datetime.datetime.strptime.(soup.find(class_="a-size-base a-color-secondary review-date").text[3:],"%B %d, %Y").date())
    else:
        return ''

def ret_reviewtext (soup):
    if soup.find(class_="a-size-base review-text")!=None:
        return soup.find(class_="a-size-base review-text").text
    else:
        return ''

def ret_reviewverpurch (soup):
    if soup.find(class_="a-size-mini a-color-state a-text-bold")!=None:
        return 'Yes'
    else:
        return 'No'

def ret_reviewhelpful (soup):
    if soup.find(class_="a-size-small a-color-secondary review-votes")!=None:
        return soup.find(class_="a-size-small a-color-secondary review-votes").text
    else:
        return ''

def ret_reviewstars (soup):
    if soup.find(class_="a-icon-alt")!=None:
        return soup.find(class_="a-icon-alt").text
    else:
        return ''


##QnA Page###########################################################################################
def ret_pg_count(soup):
    if soup.find(id="ask_feature_div")!=None:
        if soup.find(id="ask_feature_div").find(class_="a-size-base")!=None:
            return float(soup.find(id="ask_feature_div").find(class_="a-size-base").text.strip().split(" ")[0])
        else:
            return None
    else:
        return None

def ret_QnAs(soup):
    if soup.find(class_="a-section askTeaserQuestions")!=None:
        if soup.find(class_="a-section askTeaserQuestions").find_all(class_="a-fixed-left-grid")!=None:
            return soup.find(class_="a-section askTeaserQuestions").find_all(class_="a-fixed-left-grid")
        else:
            return None
    else:
        return None
    

def ret_Question(soup):
    if soup.find(class_="a-link-normal askWidgetSeeAll")!=None:
        return soup.find(class_="a-link-normal askWidgetSeeAll").text.strip()
    else:
        return ''

def ret_Question(soup):
    if soup.find(class_="a-link-normal askWidgetSeeAll")!=None:
        return soup.find(class_="a-link-normal askWidgetSeeAll").text.strip()
    else:
        return ''

def ret_Answer(soup):
    if soup.find(class_="a-section askWidgetAnswerText")!=None:
        if soup.find(class_="a-section askWidgetAnswerText").find(class_="askLongText")!=None:
            return soup.find(class_="a-section askWidgetAnswerText").find(class_="askLongText").text.strip()
        else:
            return soup.find(class_="a-section askWidgetAnswerText").text.strip()
    else:
        return ''

def ret_Votes(soup):
    if soup.find(class_="count")!=None:
        return soup.find(class_="count").text.strip()
    else:
        return ''

def ret_Date(soup):
    if soup.find(class_="askAnswerAuthorAndDate")!=None:
        return soup.find(class_="askAnswerAuthorAndDate").text.strip()
    else:
        return ''

##Website Data returning functions############################################################################################
    
def ret_title_page_info(Items):
    df_ProductInfo=pd.DataFrame()
    for Item in Items:
        ProdHomePage  = requests.get('http://www.amazon.com/dp/'+Item[1]+'/',headers={'User-Agent': 'Mozilla/5.0'})
        ProdHomePagesoup = BeautifulSoup(ProdHomePage.text, 'html.parser')
        df_ProductInfo=df_ProductInfo.append({'SKU':Item[0],'ASIN':Item[1],
                                              'Name':ret_prod_title(ProdHomePagesoup),'Price':ret_prod_ourprice(ProdHomePagesoup),
                                              'Orig_Price':ret_prod_origprice(ProdHomePagesoup),'Promotions':ret_promotions(ProdHomePagesoup),
                                              'Review_Count':ret_revcount(ProdHomePagesoup),'Review_Rating':ret_revrating(ProdHomePagesoup),
                                              'Review_5_Rating':ret_rev5percent(ProdHomePagesoup),'Review_4_Rating':ret_rev4percent(ProdHomePagesoup),
                                              'Review_3_Rating':ret_rev3percent(ProdHomePagesoup),'Review_2_Rating':ret_rev2percent(ProdHomePagesoup),
                                              'Review_1_Rating':ret_rev1percent(ProdHomePagesoup)},ignore_index=True)
    return df_ProductInfo

def ret_review_page_info(Items):
    df_Reviews=pd.DataFrame()
    for Item in Items:
        pageNumber=1
        while True:
            ProdReviewPage  = requests.get('http://www.amazon.com/product-reviews/'+Item[1]+'/?pageNumber='+str(pageNumber),headers={'User-Agent': 'Mozilla/5.0'})
            ProdReviewPagesoup = BeautifulSoup(ProdReviewPage.text, 'html.parser')
            if  ret_review_pgchecker(ProdReviewPagesoup)=='Sorry, no reviews':
                print 'break'
                break
            else:
                if ProdReviewPagesoup.find_all(class_="a-section review")==None:
                    print 'break'
                    break
                else:
                    for child in ProdReviewPagesoup.find_all(class_="a-section review"):
                        df_Reviews=df_Reviews.append({'SKU':Item[0],'ASIN':Item[1],'Heading':ret_reviewhead(child),'Author':ret_reviewauthor(child),
                                                      'Date':ret_reviewdate(child),'Text':ret_reviewtext(child),
                                                      'Verified_Purchase':ret_reviewverpurch(child),'Helpful_Count ':ret_reviewhelpful(child),
                                                      'Stars':ret_reviewstars(child)},ignore_index=True)
                    print pageNumber
                    pageNumber=pageNumber+1
    return df_Reviews 

def ret_QnA_Info(Items):
    df_QnA=pd.DataFrame()
    for Item in Items:
        ProdHomePage  = requests.get('http://www.amazon.com/dp/'+Item[1]+'/',headers={'User-Agent': 'Mozilla/5.0'})
        ProdHomePagesoup = BeautifulSoup(ProdHomePage.text, 'html.parser')
        Question_Count=ret_pg_count(ProdHomePagesoup)
        print Question_Count
        if Question_Count!=None:
            Page_Count=int(math.ceil(Question_Count/10))
            print Page_Count
            for i in range(1,Page_Count+1):
                ProdQnAPage  = requests.get('http://www.amazon.com/ask/questions/asin/'+Item[1]+'/'+str(i),headers={'User-Agent': 'Mozilla/5.0'})
                ProdQnAPagesoup = BeautifulSoup(ProdQnAPage.text, 'html.parser')
                if ret_QnAs(ProdQnAPagesoup)!=None:
                    for child in ret_QnAs(ProdQnAPagesoup):
                        df_QnA=df_QnA.append({'SKU':Item[0],'ASIN':Item[1],'Question':ret_Question(child),'Answer':ret_Answer(child),
                                              'Votes':ret_Votes(child),'Date':ret_Date(child)},ignore_index=True)
    return df_QnA

def ret_similar_products(Items):
    df_SimProducts=pd.DataFrame()
    for Item in Items:
        Driver=webdriver.PhantomJS()
        Driver.get("http://www.amazon.com/dp/"+Item[1]+"/")
        SimProducts=ret_SelSimProducts(Driver)
        if SimProducts!=None:
            for SimProduct in SimProducts:
                Product=ret_SelSimProductName(SimProduct)
                Rating=ret_SelSimProductRating(SimProduct)
                Price=ret_SelSimProductPrice(SimProduct)
                Rating_Count=ret_SelSimProductRating_Count(SimProduct)
                df_SimProducts=df_SimProducts.append({'SKU':Item[0],'ASIN':Item[1],'Product':Product,'Rating':Rating,
                                                      'Price':Price,'Rating_Count':Rating_Count},ignore_index=True)
        Driver.close()
    return df_SimProducts
    
def out_NewCSV(Items):
##    ret_title_page_info(Items).to_csv(os.getcwd()+'\\title_Page.csv',index_label ="ID")
    ret_review_page_info(Items).to_csv(os.getcwd()+'\\Review_Page.csv')
##    ret_QnA_Info(Items)
##    ret_similar_products(Items)

def out_NewExcel(Items):

    writer = pd.ExcelWriter(os.getcwd()+'\\Am_Sc_Data\\TitlePage.xlsx', engine='xlsxwriter')
    ret_title_page_info(Items).to_excel(writer, sheet_name='Sheet1')
    
    writer = pd.ExcelWriter(os.getcwd()+'\\Am_Sc_Data\\Review_Page.xlsx', engine='xlsxwriter')
    ret_review_page_info(Items).to_excel(writer, sheet_name='Sheet1')
    
    writer = pd.ExcelWriter(os.getcwd()+'\\Am_Sc_Data\\QnA_Page.xlsx', engine='xlsxwriter')
    ret_QnA_Info(Items).to_excel(writer, sheet_name='Sheet1')
    
    writer = pd.ExcelWriter(os.getcwd()+'\\Am_Sc_Data\\Sim_Product_Page.xlsx', engine='xlsxwriter')
    ret_similar_products(Items).to_excel(writer, sheet_name='Sheet1')

   



Items=[['WRB322DMBM','B00KJ1AT6A'],['WRS325FDAM','B00BB4INY4'],['WRF560SEYM','B0073M80UK'],
       ['WRS571CIDM','B00KJ1B1Q2'],['WRF540CWBM','B00KAFRMBK'],['WRB329DMBM','B00KJ161TO'],
       ['WRF560SMYM','B0076TQFOS'],['WRF989SDAM','B0081VO61E'],##Refrigirator
       ['WTW4815EW','B00VGDTZ3I'],['WTW5000DW','B00U7XFKNW'],['WTW7300DW','B00WX60SBA'],
       ['WTW4850BW','B00EZ2EQ0O'],['WFC7500VW','B001A5F1YE'],##Washer
       ['WED7300DW','B00SKJMKII'],['WED7500VW','B00HSO624Y'],['LDR3822PQ','B000Y8YL1W'],
       ['WET3300XQ','B004N759CK'],['WFW88HEAW','B009THTVZU']]##Dryer

out_NewExcel(Items)   
##Items=[['WRB322DMBM','B00KJ1AT6A']]

##print ret_title_page_info(Items)
##print ret_review_page_info(Items)
##print ret_QnA_Info(Items)
##print ret_similar_products(Items)

##out_NewCSV(Items)
##out_NewExcel(Items)
##writer = pd.ExcelWriter(os.getcwd()+'\\Review_Page.xlsx', engine='xlsxwriter')
##ret_review_page_info(Items).to_excel(writer, sheet_name='Sheet1')

##ret_review_page_info(Items).to_csv(os.getcwd()+'\\Review_Page.csv')
