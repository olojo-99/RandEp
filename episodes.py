
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