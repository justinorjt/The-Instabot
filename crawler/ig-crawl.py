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

	tagUrl = theUrl +tag
	browser = webdriver.Chrome('chromedriver.exe')
	pictureLinks=[]

	# get the html and the link
	browser.get(tagUrl)
	source = browser.page_source
	pretty = bsoup(source, 'html.parser')
	body = pretty.find('body')
	# FIND EVERY POST IN THE BODY
	post = body.findAll('div',{'class':'_bz0w'})
	# GET THE LINK TO EVERY POST AND ADD IT TO ARRAY
	for theLink in post:
		href = theLink.find('a').get('href')
		Link = basicIG+href
		pictureLinks.append(Link)

	print(pictureLinks)


	# CLOSE THE SCRAPING BROWSER
	browser.quit()
	
# def selectRandomPictures():






gather()

