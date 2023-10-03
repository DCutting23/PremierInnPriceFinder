from urllib import request

def URL_Constructor(date): #date format "dd/mm/yyyy"
    date_day = date[0:2]
    date_month = date[3:5]
    date_year = date[6:10]
    print("day: " + date_day + " month: " + date_month + " year: " + date_year)
    return "https://www.premierinn.com/gb/en/search.html?searchModel.searchTerm=North%20Shields,%20UK&PLACEID=ChIJ4VnkDRFufkgRAkgbSvII-k4&ARRdd=" + date_day + "&ARRmm=" + date_month + "&ARRyyyy=" + date_year + "&NIGHTS=1&ROOMS=1&ADULT1=1&CHILD1=0&COT1=0&INTTYP1=DB&BOOKINGCHANNEL=WEB&SORT=1&VIEW=2"

date = "07/10/2023"

def Get_Page(url):
    req = request.Request(url, data=None, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'} )
    page = request.urlopen(req)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    fileobject = open('C:\\Users\\danie\\OneDrive\\Documents\\Code\\PremierInnPriceFinder\\html.txt','w')
    fileobject.write(html)
    fileobject.close()
    return html

def Get_Price(page, hotel):
    if (hotel in page):
        print("true")
    else:
        print("false")

url = URL_Constructor(date)
page = Get_Page(url)
Get_Price(page, "kjnsda")