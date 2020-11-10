from bs4 import BeautifulSoup

html_doc="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>titre du site</title>
</head>
<body>
        <p class="c1 c2"> hello world</p>
        <p class="c3"> On va scraper ce texte</p>

</body>
</html>
"""

soup=BeautifulSoup(html_doc, "html5lib")
#print(soup)
for p in soup.find_all('p'):
    print(p)
    print("********************")
    print("********************")
    print(p.get("class"))
    print("********************")
    print("********************")
    print(p.string)
print(soup)

