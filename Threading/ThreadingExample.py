"""
    1. Throw Threads.
    2. Check the empty directory or not. 
    3. Get the Web Page content (HTML) of 5 Web Pages by URL.
    4. Create the file with the same name as the "url" 
    5. Write the WP-content in each file 
    6. Order alphabetically the text by Sort Algorithm.
"""

__author__ = "Rafael García Cuéllar"
__email__ = "r.gc@hotmail.es"
__copyright__ = "Copyright (c) 2018 Rafael García Cuéllar"
__license__ = "MIT"

import os, sys, inspect
from urllib.request import Request, urlopen 
import threading

# Set Maximum Recursion
sys.setrecursionlimit(1_000_000_000)

# Custom Import Module
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from Utilities import getMetaDetails

urls = ['https://www.google.dk/', 'http://www.esbjergkommune.dk/', 'https://www.dsb.dk/', 'https://www.lego.com/da-dk/', 'https://www.bilka.dk/']
webcontent = []

def checkDirectoryWithoutTxt():
    checkCont = 0
    
    for root, dirs, files in os.walk('.'):
        if len(files) != 0:
            for _file in files:
                if _file.split('.')[1] == "txt":
                    checkCont = checkCont + 1
    output = 'The directory has txt Files !' if checkCont > 0 else 'The directory doesn\'t have txt Files !'
    print(output)

def openUrlsInBrowser():
    import webbrowser
    for url in urls:
        pass
        # webbrowser.open(url)    # Display url using the default browser.

def getWebContent(url):
    webcontent.append(urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read())
    print("Got Web content from: " + url)

def getWebContentUsingThreads():
    for url in urls:
        thread = threading.Thread(target=getWebContent(url), name="Thread" + url.upper(), daemon= None)
        thread.start()        
        thread.join()
    print("- enumerate():      List of all Thread currently alive: %s" % (str(list(threading.enumerate()))))
    print("- active_count():   Number of threads currently alive: %s" % (str(threading.active_count())))

def formatNameFile(nameFile):
    return nameFile.replace('/', '').replace(':', '').replace('https', '').replace('http', '').replace('www.', '').replace('.dk', '')

def writeWebContentInFile():
    for i, content in enumerate(webcontent):
        with open(formatNameFile(urls[i]) + ".txt", "w") as f: 
            f.write(str(''.join(map(str, quick_sort(list(str(content))))))) 

# https://github.com/TheAlgorithms/Python/blob/d4b4b7ba35cc4e1ef9480ce1529afa388903133a/sorts/quick_sort.py
def quick_sort(ARRAY):
    """Pure implementation of quick sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    ARRAY_LENGTH = len(ARRAY)
    if( ARRAY_LENGTH <= 1):
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        GREATER = [ element for element in ARRAY[1:] if element > PIVOT ]
        LESSER = [ element for element in ARRAY[1:] if element <= PIVOT ]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)


def main():
    targets = [checkDirectoryWithoutTxt, openUrlsInBrowser, getWebContentUsingThreads, writeWebContentInFile]
    threadNames = ['ThreadCheckDirectory', 'ThreadOpenUrls', 'ThreadGetWebContent', 'ThreadWriters']
    for i in range(4):
        thread = threading.Thread(target=targets[i], name=threadNames[i], daemon= None)
        thread.start()        
        thread.join()

    
if __name__ == "__main__":
    main()