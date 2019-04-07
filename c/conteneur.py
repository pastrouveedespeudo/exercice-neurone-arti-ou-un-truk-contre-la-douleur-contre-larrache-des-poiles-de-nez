
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

PRONOMS = ["je","tu","il","nous","vous","ils"]

FEMININ = ["lle","nne","tte","sse","ve","se","che","gne","ée", "ées","e",
           "ie","ée","ue"]

IMPERATIF = ["e", "ons", "ds", "is","issons", "issez", "is", "ons"]

PONCTUATION = ['.',',',';','!','?',':']


