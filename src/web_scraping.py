import requests
from bs4 import BeautifulSoup
import re  # regex


def is_url(url):  # checks with regex if url is url
    # make sure its with http or s so s is optional
    # just to showcase regex,but can be done with startswith
    return bool(re.match(r'^https?:\/\/', url))


def get_user_input():
    # asks for url input
    user_url = input("place the url and include http:// or https://: ")

    if not is_url(user_url):
        print("invalid URL ; include http:// or https://")
        return None
    user_needs = input(
        "Choose HTML TAG (e.g., div, p) or 'FULL' for full HTML build: ").strip().lower()

    only_html = "WITHOUT"  # Default

    # Only ask about script/style tags if not requesting full page
    if user_needs == "full":
        only_html = input(
            "Would you like 'WITH' or 'WITHOUT' <script> and <style> tags: ").strip().upper()

    return user_url, user_needs.lower(), only_html.upper()


def web_scrape(url, user_needs, only_html):
    response = requests.get(url)  # gets url
    if response.status_code != 200:
        print("Couldn't fetch the page")
        return

    soup = BeautifulSoup(response.text, 'html.parser')  # beautifies it

    if only_html == "WITHOUT":
        for tag in soup(['script', 'style']):
            tag.decompose()  # removes the tag from the gotten tree

    if user_needs != "full":
        found_tags = soup.find_all(user_needs)
        if found_tags:
            for tag in found_tags:
                print("\nScraped ---->")
                # to get specific tags ,  extracts the text inside the HTML tag. eg, if the tag is <span class="text">“This is a quote”</span>, quote.get_text() will return "This is a quote"
                print(tag.get_text())
                print("\n--------")
        else:
            print(f"Nothing found for <{user_needs}>")
    else:
        print(soup.prettify())  # if full=user_needs prints whole fetched data


def grab_web():
    user_url, user_needs, only_html = get_user_input()
    if user_url:
        web_scrape(user_url, user_needs, only_html)


if __name__ == "__main__":
    grab_web()
