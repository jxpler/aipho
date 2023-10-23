from bs4 import BeautifulSoup
import requests

website = requests.get("https://www.merriam-webster.com/word-of-the-day")

soup = BeautifulSoup(website.text, 'html.parser')

daily_word = soup.find(class_="word-header-txt")
main_atr = soup.find(class_="main-attr")
definition_container = soup.find(class_="wod-definition-container")
definition = definition_container.find("p")

main_atr_text = main_atr.text
definition_text = definition.text
daily_word_text = daily_word.text


def scrape():
    return daily_word_text, main_atr_text, definition_text
