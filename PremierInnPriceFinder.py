
def URL_Constuctor(date): #date format dd/mm/yyyy
    #URL example = "https://www.premierinn.com/gb/en/search.html?searchModel.searchTerm=North%20Shields,%20UK&PLACEID=ChIJ4VnkDRFufkgRAkgbSvII-k4&ARRdd=30&ARRmm=9&ARRyyyy=2023&NIGHTS=1&ROOMS=1&ADULT1=1&CHILD1=0&COT1=0&INTTYP1=DB&BOOKINGCHANNEL=WEB&SORT=1&VIEW=2"
    date_day = date[0:2]
    date_month = date[3:5]
    date_year = date[6:10]
    print("day: " + date_day + " month: " + date_month + " year: " + date_year)
    print("https://www.premierinn.com/gb/en/search.html?searchModel.searchTerm=North%20Shields,%20UK&PLACEID=ChIJ4VnkDRFufkgRAkgbSvII-k4&ARRdd=" + date_day + "&ARRmm=" + date_month + "&ARRyyyy=" + date_year + "&NIGHTS=1&ROOMS=1&ADULT1=1&CHILD1=0&COT1=0&INTTYP1=DB&BOOKINGCHANNEL=WEB&SORT=1&VIEW=2")

date_list = ["07/10/2023","14/10/2023","21/10/2023","28/10/2023"]
for date in date_list:
    URL_Constuctor(date)