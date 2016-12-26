"""
PROGRAMMING CHALLENGE: by Tim Langeman

This sample is to be used as a programming challenge to
demonstrate techniques of calling multiple I/O intensive requests
while avoiding blocking

Actual code to be improved is at:
  https://github.com/neotext/neotext-django-server/blob/master/lib/neotext_quote_context/url.py
"""

import time


def main_get_citations(url):
    """
    Notice all of the folling requests are implemented with
    dummy functions that use "Sleep" to simulate actual processing
    """

    source_doc = document(url)
    for citation in citations(source_doc):
        destination_doc = document(citation)
        doc_match = document_match(source_doc, destination_doc)
        save_to_db(doc_match)
        upload_json()

""" ---------------- Supporting functions -------------- """


def document(url):
    print('downloading ' + url)
    time.sleep(0.75)


def citations(doc):
    """
    from bs4 import BeautifulSoup: this library will be used
    and memory usage should be optimized
    """

    # find citations in document
    citations = []
    num_citations = 7
    for i in range(num_citations):
        citations.append('http://www.example.com/' + str(i))
    return citations


def document_match(source_doc, destination_doc):
    """
    from google_diff_match_patch.diff_match_patch import diff_match_patch
    this memory will be used and memory should be optimized
    """

    time.sleep(0.1)
    return "This is the first 500 characters."


def save_to_db(document_match):
    print("saving to db")
    time.sleep(0.1)


def upload_json():
    time.sleep(0.5)

"""---------------- MAIN --------------------"""

start_time = time.time()
main_get_citations("http://example.com/")
print("--- %s seconds ---" % (time.time() - start_time))
