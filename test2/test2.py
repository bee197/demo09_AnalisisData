import time
import urllib.request
from bs4 import BeautifulSoup
import xlsxwriter

# Specify the url
url = 'https://www.thepaper.cn/'

# Create a xlsx workbook and add a worksheet
workbook = xlsxwriter.Workbook('news.xlsx')
worksheet = workbook.add_worksheet()

# Add headers
worksheet.write('A1', 'News Headline')
worksheet.write('B1', 'Publish Date')
worksheet.write('C1', 'Image Link 1')

# Initialize row count
row = 1

# Loop through 2 pages
for page in range(1, 3):

    # Build url with page number
    url_with_page = '{}?page={}'.format(url, page)
    # Request html and parse with BeautifulSoup
    html = urllib.request.urlopen(url_with_page).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

    title, date, src = None, None, None

    # Find all news headlines
    headlines = soup.find_all('div', {"class":"small_imgposition__PYVLm"})
    # 4 rows per page
    row = (page - 1) * 4
    for h in headlines:
        title = h.img["alt"]
        # 标题、日期、图片链接写入excel表格
        worksheet.write(row, 0, title)
        print(title)
        row += 1
    row = (page - 1) * 4
    dates = soup.select('p > span:nth-of-type(2)')
    for d in dates:
        date = d.text
        worksheet.write(row, 1, date)
        print(date)
        row += 1
    row = (page - 1) * 4
    for h in headlines:
        src = h.img['src']
        worksheet.write(row, 2, src)
        print(src)
        row += 1




workbook.close()