#!/usr/bin/python
from requests import get
from bs4 import BeautifulSoup as bs
import re
import os

def exists(file):
  # Check if file exists
  return os.path.isfile(file)

feed_url = "http://knowyourmeme.com/photos.rss"
output   = "img/" 

def saveImages(feed_url):
  items   = bs ( get ( feed_url ).content ).find_all('item')
  saved   = 0
  passed  = 0
  for i in items:
    name = output + i.title.text.split("|")[1].strip()
    if exists(name) == False:
      saved += 1
      raw_image_data = get(str(i.description).split(" ")[1].split('"')[1]).content
      open(name,'w').write(raw_image_data)
    else: 
      passed += 1
  print "%d Images Saved\n%d Images passed" % (saved,passed)


saveImages(feed_url)

