import urllib
from urllib import request
from bs4 import BeautifulSoup
import re

city = input("Please enter your city to check weather conditions: ")
url = "https://www.weather-forecast.com/locations/"+ city + "/forecasts/latest"
request = request.urlopen(url)
soup = BeautifulSoup(request, 'html.parser')

container = soup.find_all("table", {"class":"b-forecast__table js-forecast-table"})
mainContainer = container[0]

#Find Description to print
weatherDescription = soup.find_all("td", {"class":"b-forecast__table-description-cell--js"})
oneToThreeDayDescription =  str(weatherDescription[0].p.span)
fourToSevenDayDescription = str(weatherDescription[1].p.span)
eightToTenDayDescription = str(weatherDescription[2].p.span)
print("\n#########    WEATHER DESCRIPTION    #########\n")
print("#####   Short Term Forecast:   #####\n" + oneToThreeDayDescription[21:-7] + "\n\n#####   Mid Term Forecast:   #####\n" + fourToSevenDayDescription[21:-7] + "\n\n#####   Long Term Forecast:   #####\n" + eightToTenDayDescription[21:-7])
print("\n Nine day forecast displayed below: ")

#Find Value of Days+Date and extract required data
daysString = str(soup.find_all("span",{"class":"b-forecast__table-days-name"})).replace("<span class=\"b-forecast__table-days-name\">", "")
tempDays1 = daysString.replace("</span>,", "-")
tempDays2 = tempDays1.replace("[", "")
tempDays3 = tempDays2.replace("]", "")
tempDays4 = tempDays3.replace("</span>", "-")
days = tempDays4.split()

datesString = str(soup.find_all("span",{"class":"b-forecast__table-days-date"})).replace("<span class=\"b-forecast__table-days-date\">", "")
tempDates1 = datesString.replace("</span>,", "")
tempDates2 = tempDates1.replace("[", "")
tempDates3 = tempDates2.replace("]", "")
tempDates4 = tempDates3.replace("</span>", "")
dates = tempDates4.split()

#print(["{}{}".format(days, dates) for days,dates in zip(days, dates)])
#Create a new list object containing the days+date lists while ensuring 1-1 mapping --
daysDate = list(map(str.__add__, days, dates))

#Find Number of AMs and PMs so we know how many values added for current day
amPMString = str(soup.find_all("tr", {"class":"b-forecast__table-time js-daytimes"})).replace("<tr class=\"b-forecast__table-time js-daytimes\"><th class=\"b-forecast__table-units\"><div class=\"b-forecast__table-units-container\"><button class=\"b-forecast__table-units-button b-forecast__table-float\" data-units=\"Imperial\"><div class=\"b-forecast__table-units-button-wrapper\">°F</div></button></div></th><td class=\"b-forecast__table-time-item b-forecast__table-day-end\" data-t-periods=\"2\"><div class=\"b-forecast__text-limit\">", " ")
tempAMPM1 = amPMString.replace("[<span class=\"b-forecast__table-value\">", " ")
tempAMPM2 = tempAMPM1.replace("</span></div></td><td class=\"b-forecast__table-time-item b-forecast__table-day-odd\" data-t-periods=\"4\"><div class=\"b-forecast__text-limit\"><span class=\"b-forecast__table-value\">", " ")
tempAMPM3 = tempAMPM2.replace("</span></div></td><td class=\"b-forecast__table-time-item b-forecast__table-day-odd\" data-t-periods=\"2\"><div class=\"b-forecast__text-limit\"><span class=\"b-forecast__table-value\">", " ")
tempAMPM4 = tempAMPM3.replace("</span></div></td><td class=\"b-forecast__table-time-item b-forecast__table-day-end b-forecast__table-day-odd\" data-t-periods=\"2\"><div class=\"b-forecast__text-limit\"><span class=\"b-forecast__table-value\">"," ")
tempAMPM5 = tempAMPM4.replace("</span></div></td><td class=\"b-forecast__table-time-item\" data-t-periods=\"4\"><div class=\"b-forecast__text-limit\"><span class=\"b-forecast__table-value\">", " ")
tempAMPM6 = tempAMPM5.replace("</span></div></td><td class=\"b-forecast__table-time-item\" data-t-periods=\"2\"><div class=\"b-forecast__text-limit\"><span class=\"b-forecast__table-value\">", " ")
tempAMPM7 = tempAMPM6.replace("</span></div></td><td class=\"b-forecast__table-time-item b-forecast__table-day-end\" data-t-periods=\"2\"><div class=\"b-forecast__text-limit\"><span class=\"b-forecast__table-value\">"," ")
tempAMPM8 = tempAMPM7.replace("</span></div></td><td class=\"b-forecast__table-time-item b-forecast__table-day-odd\"><div class=\"b-forecast__text-limit\"><span class=\"b-forecast__table-value\">", " ")
tempAMPM9 = tempAMPM8.replace("</span></div></td><td class=\"b-forecast__table-time-item b-forecast__table-day-end b-forecast__table-day-odd\"><div class=\"b-forecast__text-limit\"><span class=\"b-forecast__table-value\">", " ")
tempAMPM10 = tempAMPM9.replace("</span></div></td><td class=\"b-forecast__table-time-item\"><div class=\"b-forecast__text-limit\"><span class=\"b-forecast__table-value\">", " ")
tempAMPM11 = tempAMPM10.replace("</span></div></td><td class=\"b-forecast__table-time-item b-forecast__table-day-end\"><div class=\"b-forecast__text-limit\"><span class=\"b-forecast__table-value\">", " ")
tempAMPM12 = tempAMPM11.replace("</span></div></td></tr>]", " ")
tempAMPM13 = tempAMPM12.replace("<span class=\"b-forecast__table-value\">", "")
tempAMPM14 = tempAMPM13.replace("<tr class=\"b-forecast__table-time js-daytimes\"><th class=\"b-forecast__table-units\"><div class=\"b-forecast__table-units-container\"><button class=\"b-forecast__table-units-button b-forecast__table-float\" data-units=\"Imperial\"><div class=\"b-forecast__table-units-button-wrapper\">°F</div></button></div></th><td class=\"b-forecast__table-time-item b-forecast__table-day-odd\" data-t-periods=\"4\"><div class=\"b-forecast__text-limit\">"," ")
tempAMPM15 = tempAMPM14.replace("<tr class=\"b-forecast__table-time js-daytimes\"><th class=\"b-forecast__table-units\"><div class=\"b-forecast__table-units-container\"><button class=\"b-forecast__table-units-button b-forecast__table-float\" data-units=\"Imperial\"><div class=\"b-forecast__table-units-button-wrapper\">°F</div></button></div></th><td class=\"b-forecast__table-time-item b-forecast__table-day-end b-forecast__table-day-odd\" data-t-periods=\"2\"><div class=\"b-forecast__text-limit\">", "")
tempAMPM16 = tempAMPM15.replace("<tr class=\"b-forecast__table-time js-daytimes\"><th class=\"b-forecast__table-units\"><div class=\"b-forecast__table-units-container\"><button class=\"b-forecast__table-units-button b-forecast__table-float\" data-units=\"Imperial\"><div class=\"b-forecast__table-units-button-wrapper\">°F</div></button></div></th><td class=\"b-forecast__table-time-item b-forecast__table-day-odd\" data-t-periods=\"2\"><div class=\"b-forecast__text-limit\">", "")
tempAMPM17 = tempAMPM16.replace("<tr class=\"b-forecast__table-time js-daytimes\"><th class=\"b-forecast__table-units\"><div class=\"b-forecast__table-units-container\"><button class=\"b-forecast__table-units-button b-forecast__table-float\" data-units=\"Imperial\"><div class=\"b-forecast__table-units-button-wrapper\">°F</div></button></div></th><td class=\"b-forecast__table-time-item\" data-t-periods=\"4\"><div class=\"b-forecast__text-limit\">", "")
tempAMPM18 = tempAMPM17.replace("<tr class=\"b-forecast__table-time js-daytimes\"><th class=\"b-forecast__table-units\"><div class=\"b-forecast__table-units-container\"><button class=\"b-forecast__table-units-button b-forecast__table-float\" data-units=\"Imperial\"><div class=\"b-forecast__table-units-button-wrapper\">°F</div></button></div></th><td class=\"b-forecast__table-time-item\" data-t-periods=\"2\"><div class=\"b-forecast__text-limit\">", "")
tempAMPM19 = tempAMPM18.replace("[","")
amPMnumber = tempAMPM19.split()
#print(amPMnumber[0])


#Find Values of Temperatures Displayed
mainTempString = str(soup.find_all("span",{"class":"temp b-forecast__table-value"})).replace("[<span class=\"temp b-forecast__table-value\">", "")
tempString = mainTempString.replace("</span>, <span class=\"temp b-forecast__table-value\">", " ")
#Makes a list of 81 ojects (3 x 27 temps) --- basically high,low,chill and readings for AM PM for each day
temperatures = tempString.replace("</span>]", "").split()

#Making 3 If COnditions to check if the current day has displayed AM, PM or Night and adjust index values/ accordingly
if (str(amPMnumber[0]) == str('Night')):
    step = 0
    print ("   Day/Date             AM    PM   Night")
    print ("    Today-" + str(int(dates[0])-1) + "\n             High:     ['-' , '-', " + str(temperatures[0]) + "]\n             Low:      ['-' , '-', " + str(temperatures[27]) + "]\n             Chill:    ['-' , '-', " + str(temperatures[54]) + "]")
    for temps in range(0,len(daysDate)-1):
        print("    " + daysDate[temps] + "\n             High:     " + str(temperatures[step+1:step+4]) + "\n             Low:      " + str(temperatures[step+28:step+31]) + "\n             Chill:    " + str(temperatures[step+55:step+58]))
        step = (temps*3)+3 #had to make this correction cuz we basically want to step the temps array by 3 but not step daysDate array so manually stepping tempsList
    print ("    " + daysDate[len(daysDate)-1] + "\n             High:     " + str(temperatures[25:27]) + ", '-']\n             Low:      " + str(temperatures[25+27:27+27]) + ", '-']\n             Chill:    " + str(temperatures[25+54:27+54]) + ", '-']" )


elif (str(amPMnumber[0]) == str('PM')):
    step = 0
    print ("   Day/Date             AM    PM   Night")
    print ("    " + daysDate[0] + "\n             High:     ['-' , " + str(temperatures[0:2]) + "\n             Low:      ['-' , " + str(temperatures[27:29]) + "\n             Chill:    ['-' , " + str(temperatures[54:56]))
    for temps in range(0,len(daysDate)-2):
        print("    " + daysDate[temps+1] + "\n             High:     " + str(temperatures[step+2:step+5]) + "\n             Low:      " + str(temperatures[step+29:step+32]) + "\n             Chill:    " + str(temperatures[step+56:step+59]))
        step = (temps*3)+3 #had to make this correction cuz we basically want to step the temps array by 3 but not step daysDate array so manually stepping tempsList
    print("    " + daysDate[len(daysDate)-1] + "\n             High:     ['" + str(temperatures[26])  + ", '-', '-']\n             Low:      ['" + str(temperatures[26+27]) + ", '-', '-']\n             Chill:    ['" + str(temperatures[26+54]) + ", '-', '-']" )


elif (str(amPMnumber[0]) == str('AM')):
    step = 0
    print ("   Day/Date             AM    PM   Night")
    for temps in range(0,len(daysDate)-1):
        print("    " + daysDate[temps] + "\n             High:     " + str(temperatures[step:step+3]) + "\n             Low:      " + str(temperatures[step+27:step+30]) + "\n             Chill:    " + str(temperatures[step+54:step+57]))
        step = (temps*3)+3 #had to make this correction cuz we basically want to step the temps array by 3 but not step daysDate array so manually stepping tempsList
