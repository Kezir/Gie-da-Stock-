import requests
from bs4 import BeautifulSoup

def start():
    # download wikipage
    wikipage = "https://www.biznesradar.pl/gielda/akcje_gpw"
    result = requests.get(wikipage)

    # if successful parse the download into a BeautifulSoup object, which allows easy manipulation
    if result.status_code == 200:
        soup = BeautifulSoup(result.content, "html.parser")

    # find the object with HTML class wibitable sortable
    table = soup.find('table')

    # loop through all the rows and pull the text
    new_table = []
    last_table = []
    for row in table.find_all('tr')[1:]:
        columns = row.find_all('td')
        new_table.append([column.get_text() for column in columns])

    for i in new_table:
        if len(i)>=5:
            x = i[9].replace(" ","")
            y = i[10].replace(" ","")
            if int(x) >= 100 and float(i[2]) >=0.5:
                last_table.append([i[0],i[1],i[2],i[3],int(x),int(y)])
    return last_table

def image_download(nazwa):
    # download wikipage
    wikipage = "https://www.biznesradar.pl/notowania/"+nazwa+"#1d_lin_lin"
    result = requests.get(wikipage)

    # if successful parse the download into a BeautifulSoup object, which allows easy manipulation
    if result.status_code == 200:
        soup = BeautifulSoup(result.content, "html.parser")

    # find the object with HTML class wibitable sortable

    table = soup.find('')

    # loop through all the rows and pull the text
    new_table = []
    for row in table.find_all('tr')[0:]:
        columns = row.find_all('td')
        new_table.append([column.get_text() for column in columns])

    if len(new_table[11])==0:
        last_table = [float(new_table[12][0]), float(new_table[13][0]),
                      float(new_table[14][0]), float(new_table[15][0]), float(new_table[16][0]),float(new_table[17][0])]
    else:
        last_table = [float(new_table[11][0]),float(new_table[12][0]),float(new_table[13][0]),float(new_table[14][0]),float(new_table[15][0]),float(new_table[16][0])]

    return last_table


