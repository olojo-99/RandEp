# RandEp
RandEP is a program that allows users to select a random episode of any TV series that they'd like to watch.

The program includes a HTML parser, using the requests and BeautifulSoup modules, to get a list of episodes of a particular show.
The random module is then used to select a pseudorandom episode from the list and displays it to the user.

The website that is scraped for the list of episdoes is 'epguides.com'

Users can also randomise from a list of all episodes or from specific seasons of the TV show
Includes error handling to manage erroneous inputs
