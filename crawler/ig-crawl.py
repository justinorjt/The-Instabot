import csv
import time
import random
import requests
import urllib.request
from urllib.request import urlopen
import numpy as np
from html.parser import HTMLParser
import pandas as pd
import json
from bs4 import BeautifulSoup as bsoup
from pandas.io.html import read_html
#downloaded to deal with js loaded html. May have to look it up
from selenium import webdriver

def gather():

	theUrl = 'https://www.instagram.com/explore/tags/'
	basicIG = 'https://www.instagram.com'
	# tag = '5454jt54'
	tag = 'lockeddddd'
	# tag = 'lokkedin'

	tagUrl = theUrl +tag
	browser = webdriver.Chrome('chromedriver.exe')
	pictureLinks=[]

	# get the html and the link
	browser.get(tagUrl)
	source = browser.page_source
	# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	pretty = bsoup(source, 'html.parser')
	body = pretty.find('body')
	# FIND EVERY POST IN THE BODY
	post = body.findAll('div',{'class':'_bz0w'})
	# GET THE LINK TO EVERY POST AND ADD IT TO ARRAY
	for theLink in selectRandomPictures(post):
		href = theLink.find('a').get('href')
		Link = basicIG+href
		pictureLinks.append(Link)

	print((pictureLinks))


	# CLOSE THE SCRAPING BROWSER
	browser.quit()

# something = [1,2,3,4,5,6,7,8,9]
# other=[]
# other.extend(range(1, 100))
def selectRandomPictures(anArray):
	i =[]
	i.extend(range(1,9))
	start = random.choice(i)
	theGist=[]
	nex = start

	while nex < len(anArray):
		theGist.append(anArray[nex])
		nex += random.choice(i)

	return (theGist)

# selectRandomPictures(other)

gather()

