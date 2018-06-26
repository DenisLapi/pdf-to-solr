# PDF-to-SOLR
This python script is developed for providing the **PDF** files to the **Apache Solr** for indexing

## File structure
In your Apache Solr core add this folder with:
* pdf_post.py
* files
* public

### pdf_post.py
This file is the python script which send the data to the Apach Solr using the REST api.
Modify the file by your needs

### files
In this directory add the pdf files you want to send to Apache Solr. Indexed files later will be relocated to **public/pdf** directory

### public
In this directory are added the indexed files