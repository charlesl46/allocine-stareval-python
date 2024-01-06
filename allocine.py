from requests import get 
from bs4 import BeautifulSoup
import dateparser
import urllib.parse as parse

def get_stars(query : str):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    query = parse.quote_plus(query)
    search_page = get(f"https://www.allocine.fr/rechercher/?q={query}",headers=headers).text
    soup = BeautifulSoup(search_page,"html.parser")
    first_film_card = soup.find("section").find("div",{"class" : "card"})
    meta = first_film_card.find("div",class_="meta")
    title = meta.find("h2",class_="meta-title").text.strip()
    release_date = meta.find("div",class_="meta-body").find("span",class_="date").text.strip()
    date_obj = dateparser.parse(release_date)
    release_date = date_obj.date().strftime("%d/%m/%Y")
    stareval = first_film_card.find_all("div",{"class" : "stareval"})
    presse = stareval[0].find('span',{"class" : "stareval-note"}).text
    spectateurs = stareval[1].find('span',{"class" : "stareval-note"}).text
    return {"title" : title,"release_date" : release_date,"presse" : presse,"spectateurs" : spectateurs}