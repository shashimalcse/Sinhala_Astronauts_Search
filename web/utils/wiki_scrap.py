import pandas as pd
import wikipedia
import re
import csv
from bs4 import BeautifulSoup
import os.path
import sys
import translator
import elastic_search_send
def create_corpus():
    astronauts = wikipedia.page("List of astronauts by name").content
    pattern = '^== [A-B] ==$'
    name_pattern = '^[A-Z]+[a-z]+$'
    fold = 2
    count = 0
    lines = astronauts.split('\n')
    names = []

    for i,line in enumerate(lines):
        line = line.strip()
        if len(line)<3:
            continue
        result = re.match(pattern, line)
        if result:
            count += 1
            continue
        if count >0 and count<fold:
            # isname = re.match(name_pattern, line)
            # if isname:
            if line[0].isalpha():
                for k,c in enumerate(line):
                    if c == "(" or c == "," or c=="-" or c == "—" or c == "△▲" or c == "†":
                        break  
                linek = line[0:k]
                names.append(linek)

    data  = []  

    for name in names:           
        try:
            html = wikipedia.page(name).html()
            soup = BeautifulSoup(html, 'html.parser')
            try:
                tab = soup.find("table",{"class":"infobox biography vcard"})
                bday = tab.find("span",{"class":"bday"}).text
                try:
                    status_tag = tab.find('th',text = "Status")
                    status_tag_tr = status_tag.find_parent('tr')
                    status = status_tag_tr.find('td').text
                except:
                    status = "N/A"
                finally:
                    try:
                        nationality_tag = tab.find('th',text = "Nationality")
                        nationality_tag_tr = nationality_tag.find_parent('tr')
                        nationality = nationality_tag_tr.find('td').text
                    except:
                        nationality = "N/A"  
                    finally:
                        try:
                            time_tag = tab.find('th',text = "Time in space")
                            time_tag_tr = time_tag.find_parent('tr')
                            time = time_tag_tr.find('td').text
                        except:
                            time = "N/A" 
                        finally:
                            try:
                                mission_names = []
                                missions_tag = tab.find('th',text = "Missions")
                                missions_tr = missions_tag.find_parent('tr')
                                missions = missions_tr.findAll('td')
                                for mission in missions:
                                    mission_names.append(mission.text)
                            except:
                                mission_names = "N/A"
                            finally:
                                try:
                                    selection_tag = tab.find('th',text = "Selection")
                                    selection_tr = selection_tag.find_parent('tr')
                                    selection = selection_tr.find('td').text
                                except:
                                    selection = "N/A"
                                finally:
                                    try:
                                        occupation_tag = tab.find('th',text = "Occupation")
                                        occupation_tr = occupation_tag.find_parent('tr')
                                        occupation = occupation_tr.find('td').text
                                    except:
                                        occupation = "N/A"
                                    finally:
                                        summary = wikipedia.summary(name)
            except:
                print("table not available")    
        except:
            print("name not available")    
        data.append([name,bday,status,nationality,time,mission_names,selection,occupation,summary])

    header = ['name', 'bday', 'status', 'nationality',"time","mission_names","selection","occupation","summary"]    
    with open('astronauts.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
    print("done")    
def translate_corpus():
    df = translator.translate()
    df.to_csv('astronauts_sinhala.csv', encoding='utf-8', index=False)
    print("translate done")
if __name__ == '__main__':
    if os.path.isfile("./astronauts.csv"):
        if os.path.isfile("./astronauts_sinhala.csv"):
            elastic_search_send.send_data()
        else:
            translate_corpus()
    else:
        create_corpus()
