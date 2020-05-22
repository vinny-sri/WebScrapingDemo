import requests

#Downloads from internet
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

#Ensure download occurred successfully
res.raise_for_status()

#Create pointer to file in directory
playFile = open('RomeoAndJuliet.txt', 'wb')

#Create chunks of byte info for file (to keep unicode) and write to file
for chunk in res.iter_content(100000):
	playFile.write(chunk)

#Close file
playFile.close()