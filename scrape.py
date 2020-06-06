
# Import BeautifulSoup
from bs4 import BeautifulSoup
import requests
import pandas as pd
import pprint
import time
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist


def scrape_mars():

    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=True)

    # URL of page to be scraped
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(10)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # collect the latest News Title and Paragraph Text. Assign the text to variables
    result = soup.find("div", class_="list_text")
    main_title = result.find("div", class_="content_title").text
    title_para = result.find("div", class_="article_teaser_body").text

    featured_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(featured_image_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img = soup.find('article').find('a').get("data-fancybox-href")
    img

    # Save the image url to a variable called `img_url`
    img_url = 'https://jpl.nasa.gov' + img
    ftimg_url = img_url
    ftimg_url

    # weather_url = 'https://twitter.com/marswxreport?lang=en'
    # browser.visit(weather_url)

    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')

    # mars_twitter = soup.find_all(
    # 'div', class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0')
    # mars_twitter

    # tweet in mars_twitter:
    # weather = mars_twitter.find('span')

    # Mars Facts
    mars_facts = pd.read_html('https://space-facts.com/mars/')

    mars_facts_df = mars_facts[0]
    mars_facts_df.columns = ['Category', 'Data']
    mars_facts_df

    browser.visit(
        'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced & k1=target & v1=Mars')
    time.sleep(10)

    results = []
    for i in range(4):
        browser.find_by_css('a.product-item h3')[i].click()
        soup = BeautifulSoup(browser.html, 'html.parser')
        title = soup.find('h2', class_='title').text
        url = soup.find('a',
                        text='Sample').get('href')
        results.append({'title': title, 'url': url})
        browser.back()

    return {
        'main_title': main_title,
        'title_para': title_para,
        'img_url': img_url,
        'results': results,
        'mars_facts_df': mars_facts_df.to_html()

    }


if __name__ == '__main__':
    print(scrape_mars())
