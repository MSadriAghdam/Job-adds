import re


def visualization_softwares(text):
    """Is there a need to have any visualization software skill?"""
    t = ['power bi', 'powerbi', 'tableau', 'd3', 'qlikview', 'datawrapper']
    for i in t:
        x = re.search(i, text.lower())
        if x:
            result =  True
        else:
            result = False
        return result