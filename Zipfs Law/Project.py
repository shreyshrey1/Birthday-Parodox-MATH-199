import string
import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt

def findText(link):
    data = requests.get(link).text
    return data

def getTop100BookLinks():
    data = requests.get('https://www.gutenberg.org/browse/scores/top').text
    soup = BeautifulSoup(data, 'html5lib')
    rawLinks = soup.find_all('a')
    bookLinks = []
    for i in range(len(rawLinks)):
        rawLinks[i] = rawLinks[i].get('href')
        if rawLinks[i].startswith('/ebooks/') and len(rawLinks[i]) > 8:
            bookLinks.append('https://www.gutenberg.org/files/' + rawLinks[i][8:] + '/' + rawLinks[i][8:] + '-0.txt')
    return bookLinks

def stringSplitter(string1):
	arr2 = []
	string1 = ''.join(c for c in string1 if c not in string.punctuation)
	arr = string1.splitlines()
	finalArr = []
	hasStarted = False
	for i in range(len(arr)):
		if "END OF THIS PROJECT GUTENBERG" in arr[i]:
			break
		elif hasStarted:
			for element in arr[i].split(" "):
				if element != "":
					finalArr.append(element)
		elif "START OF THIS PROJECT GUTENBERG" in arr[i]:
				hasStarted = True
				i += 1
	return finalArr


def zipfsLaw1(arr):
	d = {}
	for i in range(len(arr)):
		char1 = arr[i][0].lower()
		if char1 in d:
			d[char1] += 1
		else:
			d[char1] = 1
	sortedResult = sorted(d.items(), key=lambda x: x[1], reverse=True)
	sum = 0
	for element in sortedResult:
		sum += element[1]
	finalResult = []
	for element in sortedResult:
		finalResult.append([element[0], element[1] / sum])
	return finalResult[:36]

def zipfsLaw2(arr):
	d = {}
	for i in range(len(arr)):
		word = arr[i].lower()
		if word in d:
			d[word] += 1
		else:
			d[word] = 1
	sortedResult = sorted(d.items(), key=lambda x: x[1], reverse=True)
	sum = 0
	for element in sortedResult:
		sum += element[1]
	finalResult = []
	for element in sortedResult:
		finalResult.append([element[0], element[1] / sum])
	return finalResult[:50]

def zipfsLaw3(arr):
	d = {}
	for i in range(len(arr)):
		word = arr[i].lower()
		if word in d:
			d[word[:2]] += 1
		elif len(word) > 1:
			d[word[:2]] = 1
	sortedResult = sorted(d.items(), key=lambda x: x[1], reverse=True)
	sum = 0
	for element in sortedResult:
		sum += element[1]
	finalResult = []
	for element in sortedResult:
		finalResult.append([element[0], element[1] / sum])
	print(finalResult[:50])

def bigAssEnglishWordArray():
	links = getTop100BookLinks()
	hugeArray = []
	for element in links:
		text = findText(element)
		hugeArray += stringSplitter(text)
	return hugeArray

def bigAssGermanWordArray():
    links = ["https://www.gutenberg.org/files/19755/19755-0.txt", "http://www.gutenberg.org/cache/epub/44051/pg44051.txt", "https://www.gutenberg.org/files/15734/15734-0.txt", "https://www.gutenberg.org/files/14225/14225-0.txt", "https://www.gutenberg.org/files/13953/13953-0.txt", "https://www.gutenberg.org/files/14105/14105-0.txt", "https://www.gutenberg.org/files/19163/19163-0.txt", "https://www.gutenberg.org/files/30883/30883-0.txt", "https://www.gutenberg.org/files/52556/52556-0.txt"]
    hugeArray = []
    for element in links:
        text = findText(element)
        hugeArray += stringSplitter(text)
    return hugeArray

def bigAssFrenchWordArray():
    links = ["http://www.gutenberg.org/cache/epub/39331/pg39331.txt", "http://www.gutenberg.org/cache/epub/44054/pg44054.txt", "https://www.gutenberg.org/files/33378/33378-0.txt", "https://www.gutenberg.org/files/27566/27566-0.txt", "https://www.gutenberg.org/files/36460/36460-0.txt", "https://www.gutenberg.org/files/49619/49619-0.txt", "http://www.gutenberg.org/cache/epub/5781/pg5781.txt", "http://www.gutenberg.org/cache/epub/23444/pg23444.txt", "https://www.gutenberg.org/files/26376/26376-0.txt"]
    hugeArray = []
    for element in links:
        text = findText(element)
        hugeArray += stringSplitter(text)
    return hugeArray

def bigAssSpanishWordArray():
    links = ["http://www.gutenberg.org/cache/epub/39947/pg39947.txt", "http://www.gutenberg.org/cache/epub/46279/pg46279.txt", "http://www.gutenberg.org/cache/epub/16109/pg16109.txt", "http://www.gutenberg.org/cache/epub/13458/pg13458.txt", "https://www.gutenberg.org/files/41842/41842-0.txt", "http://www.gutenberg.org/cache/epub/29731/pg29731.txt", "http://www.gutenberg.org/cache/epub/28978/pg28978.txt", "http://www.gutenberg.org/cache/epub/44584/pg44584.txt", "http://www.gutenberg.org/cache/epub/26508/pg26508.txt"]
    hugeArray = []
    for element in links:
        text = findText(element)
        hugeArray += stringSplitter(text)
    return hugeArray

def bigAssShakespeareArray():
    links = ["http://www.gutenberg.org/cache/epub/5137/pg5137.txt", "https://www.gutenberg.org/files/3875/3875-0.txt", "https://www.gutenberg.org/files/46440/46440-0.txt"]
    hugeArray = []
    for element in links:
        text = findText(element)
        hugeArray += stringSplitter(text)
    return hugeArray

def bigAssDickensArray():
    links = ["http://www.gutenberg.org/cache/epub/1023/pg1023.txt", "http://www.gutenberg.org/cache/epub/19337/pg19337.txt", "https://www.gutenberg.org/files/766/766-0.txt", "http://www.gutenberg.org/cache/epub/730/pg730.txt", "https://www.gutenberg.org/files/1400/1400-0.txt"]
    hugeArray = []
    for element in links:
        text = findText(element)
        hugeArray += stringSplitter(text)
    return hugeArray

def bigAssFitzgeraldArray():
    links = ["http://www.gutenberg.org/cache/epub/9830/pg9830.txt", "http://www.gutenberg.org/cache/epub/4368/pg4368.txt", "http://www.gutenberg.org/cache/epub/6695/pg6695.txt", "https://www.gutenberg.org/files/805/805-0.txt"]
    hugeArray = []
    for element in links:
        text = findText(element)
        hugeArray += stringSplitter(text)
    return hugeArray

def plotZipf(arr):
    charsArr = [element[0] for element in arr]
    intsArr = [element[1] for element in arr]
    ranksArr = [i for i in range(len(arr))]
    plt.plot(ranksArr, intsArr)
    plt.xticks(ranksArr, charsArr)
    plt.show()
    return 0

#plotZipf(zipfsLaw1(bigAssEnglishWordArray()))
zipfsLaw3(bigAssEnglishWordArray())
