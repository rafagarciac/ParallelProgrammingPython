"""
    1. Throw Threads.
    2. Check the empty directory or not. 
    3. Get the Web Page content (HTML) of 5 Web Pages by URL.
    4. Create the file with the same name as the "url" 
    5. Write the WP-content in each file 
    6. Order alphabetically the text by Sort Parallel Algorithm.
"""

__author__ = "Rafael García Cuéllar"
__email__ = "r.gc@hotmail.es"
__copyright__ = "Copyright (c) 2018 Rafael García Cuéllar"
__license__ = "MIT"

import os, sys, inspect
from urllib.request import Request, urlopen
from urllib import error
import threading

# Custom Import Module
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from Utilities import getMetaDetails

# Put your URLS
urls = ['https://www.google.dk/', 'http://www.esbjergkommune.dk/', 'https://www.dsb.dk/', 'https://www.lego.com/da-dk/', 'https://www.bilka.dk/'] # , 'https://docs.python.org/3.8/library/threading.html#module-threading']
webcontent = []

def checkDirectoryWithoutTxt():
    checkCont = 0
    
    for root, dirs, files in os.walk('txt/'):
        if len(files) != 0:
            for _file in files:
                if _file.split('.')[1] == "txt":
                    checkCont = checkCont + 1
    output = 'The directory has txt Files !' if checkCont > 0 else 'The directory doesn\'t have txt Files !'
    print(output)

def openUrlsInBrowser():
    import webbrowser
    for url in urls:
        webbrowser.open(url)    # Display url using the default browser.

def getWebContent(url):
    try:
        webcontent.append(urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read())
        print("Got Web content from: " + url)
    except error.HTTPError as httpError:
        print("Didn't get Web content from: " + url + " " + str(httpError))

def makeThread(group=None, numberThreadsToCreate=1, target=None, name=None, args=(), daemon=None):
    for i in range(numberThreadsToCreate):
        thread = threading.Thread(group=group, target=target, name=name, args=args, daemon= None)
        thread.start()        
        thread.join()

def getWebContentUsingThreads():
    for url in urls:
        makeThread(None, 1, getWebContent, "Thread_" + url.upper(), (url,), None)
        # thread = threading.Thread(target=getWebContent(url), name="Thread" + url.upper(), daemon= None)
        # thread.start()        
        # thread.join()
    print("- enumerate():      List of all Thread currently alive: %s" % (str(list(threading.enumerate()))))
    print("- active_count():   Number of threads currently alive: %s" % (str(threading.active_count())))

def formatNameFile(nameFile):
    return nameFile.replace('/', '').replace(':', '').replace('https', '').replace('http', '').replace('www.', '').replace('.dk', '')

def writeFileHTML(fileName, content):
    with open("html/" +fileName + ".html", "w") as f:
        f.write(''.join(str(content)))

def writeFileTXT(fileName, content):
    with open("txt/" + fileName + ".txt", "w") as f:
        f.write(str(''.join(sorted(str(content)))).replace(' ', '')) # Merge-sort and insertion-sort hybrid -> Timsort O(n\log n) max. level performance

def writeWebContentInFile():
    for i, content in enumerate(webcontent):
        makeThread(None, 1, writeFileHTML, "ThreadWriteHTML", (formatNameFile(urls[i]), content,), None)
        makeThread(None, 1, writeFileTXT, "ThreadWriteTXT", (formatNameFile(urls[i]), content,), None)
        # threadHTML = threading.Thread(target=writeFileHTML, name="ThreadWriteHTML", args=(formatNameFile(urls[i]), content,), daemon= None)
        # threadTXT = threading.Thread(target=writeFileTXT, name="ThreadWriteTXT", args=(formatNameFile(urls[i]), content,), daemon= None)
        # threadHTML.start()        
        # threadTXT.start()        
        # threadHTML.join()
        # threadTXT.join()
        
def main():
    targets = [checkDirectoryWithoutTxt, openUrlsInBrowser, getWebContentUsingThreads, writeWebContentInFile]
    threadNames = ['ThreadCheckDirectory', 'ThreadOpenUrls', 'ThreadGetWebContent', 'ThreadWriters']
    for i in range(4):
        makeThread(None, 1, targets[i], threadNames[i], (), None)
        # thread = threading.Thread(target=targets[i], name=threadNames[i], daemon= None)
        # thread.start()        
        # thread.join()
    getMetaDetails()
    
if __name__ == "__main__":
    main()