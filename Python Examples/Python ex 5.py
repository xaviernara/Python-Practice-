#Module example cont...
#import Python_ex_4
#import random #this is importing the random module(class) from python

#Python_ex_4.fish()
# x = random.randrange(1,1000)
# print(x)
   
   
#--------------------------------------
#Download an image from the internet example 
import random #this is importing the random module(class) from python
import urllib.request

def download_web_image(url):
   name = random.randrange(1,1000)
   full_name= str(name) + ".jpg"
   urllib.request.urlretrieve(url,full_name)

#the picture will be downloaded and placed  in the same folder as this file   
download_web_image("https://upload.wikimedia.org/wikipedia/en/d/d2/Sawada_Tsunayoshi_6.jpg")

