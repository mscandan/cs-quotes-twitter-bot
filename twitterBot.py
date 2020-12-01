# Importing libraries
import random
import tweepy

# Open the APIKEYS.txt file for reading.
_file = open("APIKEYS.txt", "r")
# Read the line and split it by ',' and store it in keys list.
keys = _file.readline().split(",")

# Auth 
auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])
api = tweepy.API(auth)

# Always close the opened file when you are done with it.
_file.close()

# Openn the qoutes.txt file for reading
_file = open("quotes.txt", "r")

# Read the file line by line.
quotes = _file.readlines()

# Select random integer that starts from 0 and goes to length of quotes.
r = random.randint(0, len(quotes))

# If selected number is odd then select another number
while r % 2 != 0:
    r = random.randint(0, len(quotes))
    print(str(r))

# Combine the quote and writer name
quoteWithName = quotes[r] + " " + quotes[r+1]

# Tweet the combined string
api.update_status(quoteWithName)

# Always close the file when you are done with it.
_file.close()