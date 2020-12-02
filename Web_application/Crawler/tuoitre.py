import requests
import bs4
import pandas

titles = []
imgCaps = []
imgLinks = []


for i in range(1,30):
    page = requests.get("https://tuoitre.vn/suc-khoe/phong-mach/trang-"+str(i)+".htm")
    soup = bs4.BeautifulSoup(page.content,"html.parser")

    atribute = soup.find_all("li",{"class":"news-item"})
    for j in atribute:
        title = j.find('a')
        img = j.find('img')
        titles.append(title.get('title'))
        imgLinks.append(img.get('src'))
        imgCaps.append(img.get('alt'))

print('\n'.join(titles))
print('\n')
print('\n'.join(imgCaps))
print('\n')
print('\n'.join(imgLinks))

data = {
   "Image Caption": imgCaps,
   "Image URL": imgLinks
}
df = pandas.DataFrame(data)
df.to_csv(r'..\UI_demo_II\Tuoitre.csv', index=False)