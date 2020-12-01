# Importing libraries
import requests
from bs4 import BeautifulSoup

# Go to the website and get it's html form.
source = requests.get(
    'https://www.goodreads.com/quotes/tag/computer-science').text

# Parse it with bs4's html parser.
soup = BeautifulSoup(source, 'html.parser')

# Write the data that we got from parsing to quotes.txt
_file = open("quotes.txt", "w")
_file.write(str(soup))
_file.close()

# Open file for reading and read it line by line.
_file = open("quotes.txt", "r")
lines = _file.readlines()

# Filter the qoute text and it's writer. You can look in the file to understand for loop and appendings.
quotes = []
for i in range(0, len(lines)):
    line = lines[i]
    if "quoteText" in line:
        quotes.append(lines[i+1])
        quotes.append(lines[i+4])

# Always close the file that you are done with it.
_file.close()

# Open the qoutes.txt file for writing.
_file = open("quotes.txt", "w")

# Write the filtered quotes and writers to file line by line
for i in range(len(quotes)):
    _file.write(quotes[i])

# Always close the file that you are done with it.
_file.close()