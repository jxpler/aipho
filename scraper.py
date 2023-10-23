from bs4 import BeautifulSoup
import requests

word_url = "https://www.merriam-webster.com/word-of-the-day"
website = requests.get(word_url)

soup = BeautifulSoup(website.text, 'html.parser')

daily_word = soup.find(class_="word-header-txt")
main_atr = soup.find(class_="main-attr")
definition_container = soup.find(class_="wod-definition-container")
definition = definition_container.find("p")

main_atr_text = main_atr.text
definition_text = definition.text
daily_word_text = daily_word.text
