# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time
from pprint import pprint
from typing import List

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

CHROME_DRIVER_PATH = '/Users/viveks/Downloads/chromedriver'
ADBLOCK_EXTENSION_PATH = '/Users/viveks/Downloads/extension_4_24_1_0.crx'


def main(seed_song:str):
    # Use a breakpoint in the code line below to debug your script.
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                                                               client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")))
    results = sp.search(q=seed_song, limit=1)
    first_result = results['tracks']['items'][0]
    recs = sp.recommendations(seed_tracks=[first_result['id']], limit=100)
    song_query_strings = list(map(lambda x: x['name'] + " " + x['artists'][0]['name'], recs['tracks']))
    pprint(song_query_strings)
    open_youtube_and_play([seed_song]+ song_query_strings)

def open_youtube_and_play(tracks: List[str]):

    chrome_options = Options()
    chrome_options.add_extension(ADBLOCK_EXTENSION_PATH)
    driver = webdriver.Chrome(CHROME_DRIVER_PATH, chrome_options=chrome_options)
    driver.maximize_window()

    # Navigate to url with video being appended to search_query
    for track in tracks:
        search_and_play(driver, track)

    driver.close()


def search_and_play(driver, track: str):
    driver.get('https://www.youtube.com/results?search_query={}'.format(track))

    print(f"tabs: {len(driver.window_handles)}")
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    wait = WebDriverWait(driver, 10)
    visible = EC.visibility_of_element_located

    wait.until(visible((By.ID, "video-title")))
    driver.find_element_by_id("video-title").click()
    player_status = -1
    fullscreen = False
    wait.until(visible((By.ID, 'movie_player')))

    # check player status = 0 means playback is over
    while player_status != 0:
        player_status = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
        if player_status == 1 and not fullscreen:
            print("Playing now in fullscreen")
            driver.find_element_by_id("movie_player").send_keys("f")
            fullscreen=True
        time.sleep(2)

    print("video is over, playing next if possible")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('No argument found.\nUsage: python3 main.py "seed song"')
        exit(1)
    main(sys.argv[1])

