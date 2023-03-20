from unittest.mock import seal
from urllib import response
import bs4
import requests
from selenium import webdriver
import os
import time

#Creating directory to save image
folder_name = 'layak'
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)

folder_path = os.path.join("E:\Kuliah\BangkitLearning\Capstone", folder_name)
def download_image(url, folder_name, num):
    #write image to file
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(folder_name, str(num)+".jpg"), 'wb') as file:
            file.write(response.content)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
chromeDriverPath = r'C:\Users\Edwin\OneDrive - Universitas Atma Jaya Yogyakarta\Documents\MyPythonScript\chromedriver.exe'
driver = webdriver.Chrome(chromeDriverPath, options=options)

search_URL = "https://www.google.com/search?q=foto+rumah&tbm=isch&ved=2ahUKEwjtrqz8mtL3AhWujNgFHSsSDdcQ2-cCegQIABAA&oq=foto+rumah&gs_lcp=CgNpbWcQAzIHCCMQ7wMQJzIHCCMQ7wMQJzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgUIABCABDIFCAAQgAQyBQgAEIAEOgQIABBDOggIABCABBCxAzoKCCMQ7wMQ6gIQJzoKCAAQsQMQgwEQQzoECAAQAzoICAAQsQMQgwFQ1whYxyJgvSRoAXAAeAGAAVaIAd8IkgECMTeYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCsABAQ&sclient=img&ei=FO14Yu3UEq6Z4t4Pq6S0uA0&bih=799&biw=873"
driver.get(search_URL)

a = input("Waiting..")

#scrolling
driver.execute_script("window.scrollTo(0, 0);")

page_html = driver.page_source
pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
containers = pageSoup.findAll('div', {'class':"isv-r PNCib MSM1fd BUooTd"} )
print("jumlahnya segini: "+str(len(containers)))

len_containers = len(containers)
for i in range(1, len_containers+1):
    if i%25 == 0:
        continue

    xPath = """//*[@id="islrg"]/div[1]/div[%s]"""%(i)

    #Preview Image
    previewImageXPath = """//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img"""%(i)
    previewImageElement = driver.find_element_by_xpath(previewImageXPath)
    previewImageURL = previewImageElement.get_attribute("src")
    #print("preview URL", previewImageURL)

    driver.find_element_by_xpath(xPath).click()

    timeStarted = time.time()
    while True:
        imageElement = driver.find_element_by_xpath("""//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img""")
        imageURL= imageElement.get_attribute('src')

        if imageURL != previewImageURL:
            #print("actual URL", imageURL)
            break
        else:
            # timeout if the full res image can't be loaded
            currentTime = time.time()
            if currentTime - timeStarted > 10:
                print("Timeout!!")
                break;

    # Downloading Image
    try:
        download_image(imageURL, folder_path, i)
        print("Downloaded element %s out of %s total. URL: %s" % (i, len_containers + 1, imageURL))
    except:
        print("Couldn't download an image %s, continuing downloading the next one"%(i))