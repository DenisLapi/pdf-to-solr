###################################
#
# Name: pdf_post.py
# Author: Denis Lapi
# Contact: denislapidenis@gmail.com
# Brief: This python script is developed for providing the PDf file to the Apache Solr for indexing
#
###################################

import requests
import shutil
import os, sys

oldDirectory = './files/'
newDirectory = './public/pdf/'
requestURL	 = ''
sorlCore 	 = 'pdf_core_sample'

headers = {
	'Content-Type': 'application/pdf',
}

dirs = os.listdir(oldDirectory)

for file in dirs:
   if file[-4:] == '.pdf':
      fileName = file[:-4] # Remove the '.pdf' extension
      requestURL = 'http://localhost:8983/solr/'+sorlCore+'/update/extract?literal.file_name='+fileName
      data = open(oldDirectory + file, 'rb').read()
      requests.post(requestURL, headers=headers, data=data)
      shutil.move(oldDirectory + file, newDirectory + file) 
      print (file)

print ('[Info] PDF files successfuly uploaded. Happy searcing!')