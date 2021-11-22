# %%
#######################################
def bs4new_soup_object(url: str):
    import requests
    from bs4 import BeautifulSoup
#
    browser = requests.session()
    webreq = browser.get(url)
    thetext = webreq.text
    soup = BeautifulSoup(thetext, 'html.parser')
    return soup

