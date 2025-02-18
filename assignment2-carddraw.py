# assignment2-carddraw.py
# Author: Jake Daly

import requests


shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(shuffle_url)
data = response.json()

deck_id = data['deck_id']

draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(draw_url)
cards = response.json()['cards']

for card in cards:
    print("Card:", card['value'], "of", card['suit'])