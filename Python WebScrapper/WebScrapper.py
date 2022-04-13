import shutil
import cfscrape
import requests
import numpy as np
import LS_URL_Gen as LUG
from bs4 import BeautifulSoup as bSoup
from bs4 import SoupStrainer
from tqdm import tqdm as tqdm

# spoofing for requests
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

# number of images to download
no_IMG = 10000


def single_Page_Scrap(url):
    image_ID = url.rsplit('/', 1)[-1]
    # file name to know which code the file game from
    filename = r"Images/" + image_ID + r".jpg"
    # setting up requests
    uClient = requests.get(url, headers=header)
    # search one area
    uPage_Soup = bSoup(uClient.text, 'lxml', parse_only=SoupStrainer('img', class_="no-click screenshot-image"))
    # find all the images
    uPage_Images = uPage_Soup.findAll('img')

    for image in uPage_Images:
        # try to do a normal request and then try an CF exploit request
        try:
            image_link = image.attrs.get("src")
            r = requests.get(image_link, stream=True, headers=header)
            download_Image(r, filename, image_link)
        except:
            try:
                # CF trying to get the img
                scraper = cfscrape.CloudflareScraper()
                block_Image = scraper.get(image_link, stream=True, headers=header)
                download_Image(block_Image, filename, image_link)
            except:
                # adding full HTTP linl and trying to get it again
                new_Image_Link = 'https://' + image_link[2:]
                try:
                    scraper = cfscrape.CloudflareScraper()
                    block_Image = scraper.get(new_Image_Link, stream=True, headers=header)
                    download_Image(block_Image, filename, new_Image_Link)
                except:
                    print(
                        '\n============================================================================================')
                    print('\n                                      Unkown Error')
                    print('\n' + new_Image_Link)
                    print(
                        '============================================================================================')


def download_Image(image, filename, img_ID):
    # try to get write the image and error handle
    if str(image.status_code) == "200":
        image.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(image.raw, f)
    elif str(image.status_code == "520"):
        print('\n============================================================================================')
        print('                                     Page Forbidden 403')
        print(img_ID)
        print('============================================================================================')

    elif str(image.status_code) == "404":
        print('\n============================================================================================')
        print('\n                                   Page Not Found 404 ')
        print('\nImage Couldn\'t be retreived ' + img_ID)
        print('============================================================================================')
    else:
        print('\n============================================================================================')
        print('\nImage Couldn\'t be retreived ' + img_ID)
        print('============================================================================================')


if __name__ == '__main__':
    # get the URL codes
    id_Url = LUG.get_List()
    string_Url = []

    # make the URLs with the generated codes
    for index, url in enumerate(id_Url):
        string_Url.append('https://prnt.sc/' + id_Url[index + 1])

    # shuffle the array to get random URLs each time you run
    np.random.shuffle(string_Url)

    # for testing limit the search to 100 URLs
    short_String_Url = []
    for i in range(no_IMG):
        short_String_Url.append(string_Url[i])

    # for each URL go get the image
    for index, img in enumerate(tqdm(short_String_Url)):
        if index == no_IMG:
            break
        else:
            single_Page_Scrap(short_String_Url[index])
