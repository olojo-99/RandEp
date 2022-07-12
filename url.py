
# Used to construct url that will be scraped
def url_constructor(title):
    # we could also use regex to find the whitespace after "the"
    name = title.lower().replace("the ", "").replace(" ", "")
    for char in name:
        if not char.isalnum(): # Gets rid of spaces, apostrophes, etc.
            name = name.replace(char, "")

    return "http://epguides.com/" + name + "/"