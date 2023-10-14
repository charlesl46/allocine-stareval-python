from requests import get 
from bs4 import BeautifulSoup
import os
import urllib.parse as parse

def get_stars(query : str):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    query = parse.quote_plus(query)
    search_page = get(f"https://www.allocine.fr/rechercher/?q={query}",headers=headers).text
    soup = BeautifulSoup(search_page,"html.parser")
    first_film_card = soup.find("section").find("div",{"class" : "card"})
    stareval = first_film_card.find_all("div",{"class" : "stareval"})
    presse = stareval[0].find('span',{"class" : "stareval-note"}).text
    spectateurs = stareval[1].find('span',{"class" : "stareval-note"}).text
    return {"presse" : presse,"spectateurs" : spectateurs}

print(get_stars("the creator"))