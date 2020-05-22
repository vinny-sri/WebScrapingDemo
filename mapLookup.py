#! python3
# This script takes in an address from the command line and opens a browser with Google Maps
# showing the location

import webbrowser as wb
import sys

# sys.argv stores a list of the program's filename and command line arguments
# Check if list has more than just the filename
if (len(sys.argv)) > 1:
	address = ' '.join(sys.argv[1:])
	wb.open('https://www.google.com/maps/place/' + address)




