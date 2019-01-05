import csv
import time
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
	myurl ='https://www.pro-football-reference.com/'
	player = 'players/A/AndeJu00.htm'
	tag = 'bears'

	tagUrl = theUrl +tag
	purl = myurl+player
	# driver = webdriver.PhantomJS()
	browser = webdriver.Chrome('chromedriver.exe')

	# get the html
	browser.get(purl)
	source = browser.page_source
	pretty = bsoup(source, 'html.parser')
	body = pretty.find('body')
	# script_tag = body.find('script')
	# raw_string = script_tag.text.strip().replace('window._sharedData =', '').replace(';', '')
	# print(json.loads(raw_string))

	print(pretty)
	# CLOSE THE SCRAPING BROWSER
	browser.quit()
	pagetitle = pretty.title.get_text()
	print('THIS IS THE PAGE title',pagetitle)

	# print('SEPARATE  ---->  ',pretty.section.main.div.div.div.div)

	#Diving in
	# picLinks = []
	# for elem in pretty.find_element_by_class_name('_bz0w'):
	# 	picLinks.append(elem)

	# sample = pretty.find_element_by_class_name('_bz0w')
	# # print(sample.get_attribute('href'))
	# # print(picLinks)
	# print((sample.text), 'is my sample')

gather()