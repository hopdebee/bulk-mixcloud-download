import selenium
import time

from selenium import webdriver
chromedriver_path = "/usr/lib/chromium-browser/chromedriver"

driver = webdriver.Chrome(executable_path=chromedriver_path)

###change this
playlisturl = "https://www.mixcloud.com/lowlight/"


driver.get(playlisturl)



SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

linklist = driver.find_elements_by_css_selector(".card-title h1 a")

#transform to downloader links
newlinks = []
for link in linklist:
    href = link.get_attribute("href")
    newlink = href.replace("https://www.mixcloud.com/", "http://www.mixcloud-downloader.com/dl/mixcloud/")
    newlinks.append(newlink)

#download all the linkes in the linklst
for newlink in newlinks:
    driver.get(newlink)
    time.sleep(3)

driver.close()