import csv
import time
import urllib.request
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bsoup
from pandas.io.html import read_html
#downloaded to deal with js loaded html. May have to look it up
from selenium import webdriver

def gather(url, tag):

	theUrl = 'https://www.instagram.com/explore/tags/'
	tag = 'bears'