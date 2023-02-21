import tweepy
import random
import lyricsgenius
import time

# Twitter API credentials
auth = tweepy.OAuthHandler("your 1st credential", "your 2nd credential")
auth.set_access_token("your acess token",
                      "yout acess key")
api = tweepy.API(auth)

# Initialize the Genius API client
genius = lyricsgenius.Genius("your genius API key", timeout=70,#this is the timeout for conection
                             skip_non_songs=True,
                             excluded_terms=["Remix", "Live", "Mix", "Medley", "Cover", "Version"],
                             retries=1)
#creating a list of artits that the bot will look for
artists = ["artist 1",
           "artist 2"
           ]

#this get the lyrics from the api
#It choose a random artist from tha list and look up for 100 songs of this artists
#It get the lyrics, name and section of the song(chorus, verse,etc.)
def get_raw_lyrics():
    random_artist = random.choice(artists)
    song_list = genius.search_artist(random_artist, max_songs=100)
    random_song = random.choice(song_list.songs)
    lyrics = random_song.lyrics
    song = random_song.title
    sections = lyrics.split("\n\n")
    return lyrics, sections,song, random_artist


#Here is where it generates the tweet
#It choose a random section from the lyrics
#It returns a quote from the choosen section
def get_tweet_from(lyrics, sections):
    if sections:
        random_section = random.choice(sections)
        lines = random_section.split('\n')
    else:
        lines = lyrics.split('\n')
    for index in range(len(lines)):
        if lines[index] == "" or "[" in lines[index]:
            lines[index] = "XXX"
    lines = [i for i in lines if i != "XXX"]

    random_num = random.randrange(0, len(lines)-2)
    tweet = lines[random_num] + "\n" + lines[random_num+1]
    tweet = tweet.replace("\\", "")
    return tweet

#simply tweets the quote and sets a timer for it to run again :) 
while True:
    lyrics, sections,song, random_artist = get_raw_lyrics()
    tweet = get_tweet_from(lyrics, sections)
    status = f"{random_artist} - {song}\n\n{tweet}"
    api.update_status(status)
    print("Tweeted successfully!")
    time.sleep(3600) # sleep for 1 hours (60 seconds * 60 minutes * 1)
