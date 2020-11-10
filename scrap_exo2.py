from bs4 import BeautifulSoup
site="http://quotes.toscrape.com/page/1/"
parser="html5lib"

soup=BeautifulSoup(site,parser)
#citations= tag_analyser(soup,"span")
for i in soup.find_all("span"):
    print(i)
