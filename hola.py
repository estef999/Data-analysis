from bs4 import BeautifulSoup
years=[1930,1934,1938,1950,1954,1958,1962,1966,1970,1974,1978,1982,1986,1990,1994,2002,2006,2010,2014,2018]
import requests
web="https://en.wikipedia.org/wiki/2014_FIFA_World_Cup"
response= requests.get(web)
print(response.text)