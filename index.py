#import modules
from unittest import result
from bs4 import BeautifulSoup
import csv
import requests
from itertools import zip_longest

#list of items we gon use
article_title = []
article_content = []
article_publish = []
article_category = []
article_link = []

#fetch the url
resultat = requests.get("https://ensak.usms.ac.ma/ensak/category/news/")

#get page content in a variable
src = resultat.content

#soup object to parse with lxml
soup = BeautifulSoup(src, "html.parser")

#find elements containing infos we need
article_titles = soup.find_all("h2",{"class":"entry-title"})
article_published = soup.find_all("span",{"class":"posted-on"})
article_categories = soup.find_all("span",{"class":"cat-links"})


#loop over, to extract my needed infos
for i in range(len(article_categories)):
    article_title.append(article_titles[i].text)
    article_category.append((article_categories[i].text))
    article_publish.append(article_published[i].text)
    article_link.append(article_titles[i].find("a").attrs['href'])

for lien in article_link:
    result = requests.get(lien)
    src = resultat.content
    soup = BeautifulSoup(src, "html.parser")
    contenu = soup.find("div",{"class":"entry-content"})
    article_content.append(contenu.text)

    print(contenu.text)


#we save all data in a csv file
list_fichier = [article_title, article_category,article_publish, article_content, article_link]
then = zip_longest(*list_fichier)
with open("C:/Users/EliteBooK/Desktop/my scrapping/scrpped_Ensakh.csv","w", encoding = "utf-8") as fichier:
    wr = csv.writer(fichier)
    wr.writerow(["Titre", "Categorie", "Date","Contenu","lien"])
    wr.writerows(then)
