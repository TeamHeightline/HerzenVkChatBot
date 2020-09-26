import requests
import json


async def get_timetable(url):
    payload = {"groupURL": url}
    r = requests.get('https://herzen-timetable.herokuapp.com/api/timetable/group', payload)

    res_dict = json.loads(r.content)
    print(res_dict)
    timetable_text = ''

    for i in range(0, 6):
        try:
            timetable_text += ((res_dict['subgroups'][0]['days'][i]['day']).title() + ' ' +
                           res_dict['subgroups'][0]['days'][i]['hours'][0]['weeks'][0]['classes'][0]['dates'][0]['dates_raw'] + "\n")
        except:
            pass
        for a in range(0, 4):
            try:
             timetable_text += (res_dict['subgroups'][0]['days'][i]['hours'][a]['timespan'] + " ")
            except:
                pass
            try:
                timetable_text += (res_dict['subgroups'][0]['days'][i]['hours'][a]['weeks'][0]['classes'][0]['class'] + " " +
                                   res_dict['subgroups'][0]['days'][i]['hours'][a]['weeks'][0]['classes'][0]['type'] + " \n" +
                                   res_dict['subgroups'][0]['days'][i]['hours'][a]['weeks'][0]['classes'][0]['teacher'] + " " +
                                   res_dict['subgroups'][0]['days'][i]['hours'][a]['weeks'][0]['classes'][0]['place'] + "\n")
            except:
                pass
        timetable_text += " \n \n"

    return timetable_text
