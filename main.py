#!/usr/bin/env python3

# This module allows us to scrape the web using python
import requests
from bs4 import BeautifulSoup  # Allow us to parse the HTML
from random import randrange
from url import url_constructor
from episodes import eplist 


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
