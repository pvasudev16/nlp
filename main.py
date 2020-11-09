import nltk
import requests
from bs4 import BeautifulSoup

# Download punkt, which is required for turning sentences into a list
nltk.download('punkt')

# Which website we want to look for words
link = "https://www.newyorker.com"

#Load the data, and get the HTML content.
r = requests.get(link)
soup = BeautifulSoup(r.content, features="html.parser")

# Get the sentences; soup.get_text() will return a list of sentences
sentences = nltk.sent_tokenize(soup.get_text())

result = [sentence for sentence in sentences if "Donald" in sentence]

for i in range(len(result)):
    print(result[i] + "\n\n\n")
    
