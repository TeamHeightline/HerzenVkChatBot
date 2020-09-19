import requests
import json


async def get_timetable(url):
    payload = {"groupURL": url}
    r = requests.get('https://herzen-timetable.herokuapp.com/api/timetable/group', payload)

    res_dict = json.loads(r.content)

    timetable_text = ''

    for i in range(0, 6):
        timetable_text += ((res_dict['days'][i]['day']).title() + ' ' +
                           res_dict['days'][i]['hours'][0]['weeks'][0]['classes'][0]['dates'][0]['dates_raw'] + "\n")
        for a in range(0, 4):
            timetable_text += (res_dict['days'][i]['hours'][a]['timespan'] + " ")
            try:
                timetable_text += (res_dict['days'][i]['hours'][a]['weeks'][0]['classes'][0]['class'] + " " +
                                   res_dict['days'][i]['hours'][a]['weeks'][0]['classes'][0]['type'] + " " +
                                   res_dict['days'][i]['hours'][a]['weeks'][0]['classes'][0]['teacher'] + " " +
                                   res_dict['days'][i]['hours'][a]['weeks'][0]['classes'][0]['place'] + "\n")
            except:
                pass
        timetable_text += " \n \n"

    return timetable_text
