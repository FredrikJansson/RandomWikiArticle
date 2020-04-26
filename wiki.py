"""

   Fredrik Jansson,
   Filling out my GitHub.

"""

# ===============================
# =           Imports           =
# ===============================

import wikipedia as wk
import webbrowser as wb

# ===============================
# =           Classes           =
# ===============================

class Article:
	def __init__(self):
		temp = wk.random(1)
		temp = wk.search(temp)
		self.page = page = wk.page(temp)

	def getName(self):
		return self.page.title
	
	def getSummary(self, sent = 1):
		return wk.summary(self.page, sentences = sent)

	def getURL(self):
		return str(self.page.url)


# =================================
# =           Functions           =
# =================================

def getInput():
	while "Getting input":
		currInput = str(input("Enter (y)es, (n)o or (e)xit. Invalid counts as no: "))
		if currInput[0] == 'y':
			return 1
		elif currInput[0] == "e":
			return -1
		else:
			return 0

# ====================================
# =           Main Section           =
# ====================================

if __name__ == '__main__':
	""" Initiating an article. """
	currArticle	= Article()
	currInput 	= 0

	""" Getting input from user, want to read the article? """
	while "Searching for adequate article":
		print("\nCurrent article is:", currArticle.getName())
		print("Summary:", currArticle.getSummary())
		print()
		currInput = getInput()
		if currInput:
			break
		currArticle = Article()

	""" Opening article. """
	if currInput == 1:
		wb.open(currArticle.getURL())
	else:
		print("Closing application.")