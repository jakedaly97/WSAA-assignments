# assignment2-carddraw.py
# Author: Jake Daly

import requests


shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1" # API shuffle URL
response = requests.get(shuffle_url) # GET request to generate and shuffle deck
data = response.json()

deck_id = data['deck_id'] # Extract deck id 

draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5" # URL to draw 5 cards from the specic deck
response = requests.get(draw_url) # GET request to draw 5 cards
cards = response.json()['cards']

for card in cards:
    print("Card:", card['value'], "of", card['suit']) # Loop through cards and print values and suit
    
# Resources
# Deck of cards API, https://deckofcardsapi.com/
# Video going through API, https://www.youtube.com/watch?v=qF6zUptypGE
# Python requests, https://www.geeksforgeeks.org/response-json-python-requests/