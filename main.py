#!/usr/bin/env python3

# This module allows us to scrape the web using python
import requests
from bs4 import BeautifulSoup  # Allow us to parse the HTML
from random import randrange


# Used to construct url that will be scraped
def url_constructor(title):
    # we could also use regex to find the whitespace after "the"
    name = title.lower().replace("the ", "").replace(" ", "")
    for char in name:
        if not char.isalnum(): # Gets rid of spaces, apostrophes, etc.
            name = name.replace(char, "")

    return "http://epguides.com/" + name + "/"


# A function which takes the HTML payload and returns episodes in a list
def eplist(payload, alleps=None):
    # We search the BeautifulSoup object for a specific id using .find
    result = payload.find(id="eplist")
    load = result.find_all("tr")  # A list of the table row elements

    eplst = []  # All valid episodes will be added to this list

    for episode in load:

        season_episode = episode.find(class_="epinfo left pad")

        try:
            se = (str(season_episode).split(">")[1]).split("<")[0]

        # Can try to convert user input to an int - ignore otherwise
            try:
                alleps = int(alleps)
                if alleps == int(se.split("-")[0]):
                    se = f'Season: {se.split("-")[0]}, Episode: {se.split("-")[1]}'
                else:
                    continue

            except:  # If we want to take all episode into consideration (not byseason())
                se = f'Season: {se.split("-")[0]}, Episode: {se.split("-")[1]}'

        except:  # episode.find returns None for first few
            continue

        title = episode.find(class_="eptitle left")
        ttl = (str(title).split(">")[2]).rstrip("<a/")

        eplst.append([se, ttl])  # Add a list containing season-episode and title to eplst

    return eplst


# Main func will take tv show name, type of randomisation (all eps or by season) and return an ep
def main():
    show = input("Enter the name of a TV series: ")
    URL = url_constructor(show)  # URL is always constructed since it's just creating a string

    # The get method allows us to get the HTML content of the web page - returns page object
    page = requests.get(URL)
    # We can check if the URL is valid. Successful URL == True and Unsuccessful == False
    if not page:  # Check for status error code between 200-400 (__bool__ is overloaded by module)
        print("\nInvalid Show name.")
        return main()  # Invalid show name; start again

    # Create a BeautifulSoup object and specify the appropriate type of parser (html in this case)
    soup = BeautifulSoup(page.content, "html.parser")

    while True:
        alleps = input("Would you like to randomise by Season? If so, which season? ")
        eps = eplist(soup, alleps)
        
        # This exception handling is mainly for invalid season choice
        try:
            num = randrange(len(eps))
            return "\n".join(eps[num])

        except:
            print("\nSeason out of range.")
            # return main()  # Instead of restarting the whole func, restart this While loop
            continue


if __name__ == '__main__':
    print(main())
