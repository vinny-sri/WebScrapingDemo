#This program takes in a Google Search query and opens the first 5 links that appear on different tabs of a browser

import webbrowser as wb 
import sys, requests, bs4

# HTTP Request for webpage that is the result of searching the input on Google
assert len(sys.argv) > 1
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Creating Beautiful Soup Object from Request
soup = bs4.BeautifulSoup(res.text)
links = soup.findAll("a")

# Open tab for each link
numOpen = min(5, len(links))
for i in range(numOpen):
	wb.open('http://google.com' + links[i].get('href'))




 