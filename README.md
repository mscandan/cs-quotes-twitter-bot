# Twitter Bot using Web Scraping and Twitter API

### This project allows you to go through the any website for computer science quotes and posts them on your twitter acc.

### Packages that we use in project you have to install them

- [Tweepy](http://www.tweepy.org/)
- [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [request](https://www.pythonforbeginners.com/requests/using-requests-in-python)

### How does it work?

- Installing required packages
  
  ```bash
    pip install bs4 request tweepy
  ```

- You need to create twitter application
  - [Twitter Developer](https://developer.twitter.com/apps)
    - You need to create APIKEYS.txt file and paste the secret keys into it. We will be reading our secret keys from that file.

- We will be using bs4 for web scraping the page that has computer science quotes on it. Look at getData.py
  
  ```bash
    python3 getData.py
  ```

  - [Link](https://www.goodreads.com/quotes/tag/computer-science) to web page.
  - We have to go through all the divs that has class attribute equals to quoteText
  - After the scraping the web page we are going to write our data to quotes.txt file.
  - Next step is simple we have to look at in our quotes.txt file and find the quotes and their writes.
    - Open the quotes.txt file for reading and read it line by line.
    - The first line that we read is qoute and the fourth line is the writer of the quote.
    - Append them to a empty list.
    - Write the list that contains determined quotes and writers to qoutes.txt file.

- We will be using tweepy for sending tweets to twitter.
  
  ```bash
    python3 twitterBot.py
  ```

  - The web scraping and saving the data to a text file part is done now we will send those quotes to twitter.
  - We should read our api keys from APIKEYS.txt file and split them by ','. After the spliting them we have to auth our app using those keys.
  - After the auth part we are ready to send tweets.
  - Read the quotes.txt file pick a random number that starts from 0 and ends at length of the file.
  - If the picked random number is not even we have to select another random number. Why? Because wrote the qoutes first (starts from 0) and writer name comes second. So in our stored date quotes is in even index numbers.
  - When it's done selecting random even number we can continue with the next step.
  - We need to combine quote and the writer of the qoute strings.
  - With the tweepy's function called 'update_status', we can send the combined string to twitter as a tweet.
