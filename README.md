# Twitter Lyrics Bot
This is a twitter bot that tweets quotes from lyrics of my favorite bands/artists.
It was made using Genius API and Twitter API.
The code begins by importing the necessary libraries, which include Tweepy, random, LyricsGenius, and time. The Twitter API credentials are stored in the auth variable using the OAuthHandler method, and the Genius API client is initialized using the Genius method.

Next, a list of artists is defined in the artists variable, and the get_raw_lyrics function is defined to retrieve a random song and its lyrics from a randomly selected artist using the Genius API. The function returns the raw lyrics, song sections, song title, and artist name.

The get_tweet_from function is then defined, which randomly selects a section of lyrics from the song and formats it as a tweet. The function returns the tweet.

Finally, the program enters a loop that runs indefinitely, which retrieves raw lyrics using the get_raw_lyrics function, formats a tweet using the get_tweet_from function, and posts the tweet to the authenticated Twitter account using the update_status method from the Tweepy library. The program then sleeps for 1 hour before repeating the process. The printed message "Tweeted successfully!" confirms that the tweet was successfully posted.

Overall, this code uses the Tweepy and LyricsGenius libraries to post random lyrics from a set of artists to a Twitter account at regular intervals.