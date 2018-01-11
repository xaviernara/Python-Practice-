#Module example cont...
#import Python_ex_4
#import random #this is importing the random module(class) from python

#Python_ex_4.fish()
# x = random.randrange(1,1000)
# print(x)
   
   
#--------------------------------------
#Download an image from the internet example 
# import random #this is importing the random module(class) from python
# import urllib.request
# 
# def download_web_image(url):
#    name = random.randrange(1,1000)
#    full_name= str(name) + ".jpg"
#    urllib.request.urlretrieve(url,full_name)
# 
# #the picture will be downloaded and placed  in the same folder as this file   
# download_web_image("https://upload.wikimedia.org/wikipedia/en/d/d2/Sawada_Tsunayoshi_6.jpg")
# 

#--------------------------------------
#How to read and write to a file example 
#writing to a file
# file_write = open("sample.txt","w")
# file_write('wrting some stuff in my text file \n')
# file_write('i like bacon \n')
# file_write.close()
# 
# #reading from a file
# file_reader= open ("sample.txt","r")
# text= file_reader.read()
# print(text)
# file_reader.close

#-----------------------------------------------
#Downloading Files from the Web example
# from urllib import request #a different way you can import modules
# ibm_url = "https://www.ibm.com/support/knowledgecenter/SVU13_7.2.1/com.ibm.ismsaas.doc/reference/AssetsImportExtendedSample.csv?view=kc"
# 
# def download_csv_file(csv_url):
#    response = request.urlopen(csv_url)
#    csv = response.read()
#    csv_str= str(csv)
#    lines = csv_str.split("\\n")
#    dest_url = r'ibm.csv' #r = raw string
#    fx = open (dest_url, "w")
#    
#    for line in lines:
#       fx.write(line + "\n")
#       
#    fx.close()
#       
# download_csv_file(ibm_url)
#    
# 
#-----------------------------------------------
#How to Build a Web Crawler example
import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
   page = 1
   while page < max_pages:
        url = 'https://www.thenewboston.com/search.php?type=1&sort=pop&page=' + str(page)
        source_code = request.get(url)
        plain_text=source_code.text
        soup = BeautifulSou(plain_text)
        
        for link in soup.findAll('a',{'class', 'item-name'}):
            href = "https://www.thenewboston.com" + link.get('href')
            title = link.string
            #print(href)
            #print(title)
        page += 1   


def get_signle_item_var(item_url):
    source_code = request.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('div',{'class', 'i-name'}):
         print(item_name.string)

    for link in soup.findAll('a'):
         href = "https://www.thenewboston.com" + link.get('href')
         print(href)



trade_spider(1)

