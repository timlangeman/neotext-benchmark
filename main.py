import time, timeit

def main_get_citations(url):
 source_doc = document(url)
 for citation in citations(source_doc):
   destination_doc = document(citation)
   doc_match = document_match(source_doc, destination_doc)
   save_to_db(doc_match)
 	upload_json()

def document(url):	# download url
  print('downloading ' + url)
  time.sleep(0.75)

def citations(doc): # find citations in document
 #from bs4 import BeautifulSoup
 citations = []
 num_citations = 7 
 for i in range(num_citations):
   citations.append('http://www.example.com/' + str(i))
 return citations

def document_match(source_doc, destination_doc):
  #from google_diff_match_patch.diff_match_patch import diff_match_patch
  time.sleep(0.1)
  return "This is the first 500 characters."

def save_to_db(document_match):
  print("saving to db")
  time.sleep(0.1)

  def upload_json():
  time.sleep(0.5)

start_time = time.time()
main_get_citations("http://example.com/")
print("--- %s seconds ---" % (time.time() - start_time))

