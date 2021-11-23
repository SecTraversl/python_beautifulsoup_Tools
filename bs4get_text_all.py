# %%
#######################################
def bs4get_text_all(soup_object):
    import re
    results = soup_object.find_all(text=re.compile(r'\w+', re.IGNORECASE))
    return results

