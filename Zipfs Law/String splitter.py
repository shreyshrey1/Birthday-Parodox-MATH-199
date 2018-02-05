import string

def stringsplitter(string1):
	arr2 = []
	string1 = ''.join(c for c in string1 if c not in string.punctuation)
	arr = string1.split(" " or "\n")
	for i in range(len(arr)):
		if not (type(arr[i]) != str or len(arr[i]) == 0):
			arr2.append(arr[i])
	print(arr2)


def zipfslaw1(arr):
	d = {}
	for i in range(len(arr)):
		word = arr[i]
		char1 = word[0].lower()
		if char1 in d:
			d[char1] += 1
		else:
			d[char1] = 1
	print(d)

file = open("text1.txt", "r")

stringsplitter(file)