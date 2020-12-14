# Tubify

Youtube autoplay sucks in my experience. So created
this script to automate getting recommendations from spotify
and playing videos of those songs on youtube.


## How it works (for now) ?

Uses spotipy (spotify python client) to get recommendations based on seed song(s) from user input
and then selenium library to automate searching youtube, playing video song, waiting for it to end, 
and repeat.


TLDRCode

- Uses spotipy (spotify python client)
    - to search spotify with user's song to get spotify song id
    - Use that id to get recommendations
- For each song in the recommendation, uses selenium library to automate
    - searching youtube
    - playing the first search result
    - waiting for the video to end

Also,
- I use chromedriver to be able to install adblock extension to avoid youtube ads; there's some logic to deal with
 installation and post-installation-welcome-tab-closing.
 

## To set it up
- [Optional] Setup virtual env
- Install requirements: `pip3 install -r requirements.txt`
- Download chromedriver and update chromedriver path in main.py (See [chromedriver downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads) )
- Get adblock crx file (chrome extension file) and update the path in main.py; I got it from here: https://www.crx4chrome.com/crx/31928/
- Last, but not the least, get spotify developer credentials and add it to environment
  ```
  export SPOTIFY_CLIENT_ID="xxxxx"
  export SPOTIFY_CLIENT_SECRET="xxxxx"
  ```
 
- Run the main script
    ```
  python3 main.py
  ```
  
## Demo

https://youtu.be/pacS0_vJDQk


## Next

Thinking of packaging it into an browser extension