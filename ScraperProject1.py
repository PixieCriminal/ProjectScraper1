from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("/path/2/to/Chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["name", "distance", "mass", "radius"]
    star_data = []