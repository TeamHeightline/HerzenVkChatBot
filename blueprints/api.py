import requests
import json


payload = {"groupURL": "/static/schedule_view.php?id_group=12459&sem=1"}
r = requests.get('https://herzen-timetable.herokuapp.com/api/timetable/group', payload)

res_dict = json.loads(r.content)
print(res_dict)
for i in range(0, 5):
    print((res_dict['days'][i]['day']).title() + ' ' +
          res_dict['days'][i]['hours'][0]['weeks'][0]['classes'][0]['dates'][0]['dates_raw'])
    for a in range(0, 4):
        print(res_dict['days'][i]['hours'][a]['timespan'])
        try:
            # print(res_dict['days'][i]['hours'][a]['weeks'][0]['classes'][0]['class'])
            # print(res_dict['days'][i]['hours'][a]['weeks'][0]['classes'][0]['type'])
            # # print(res_dict['days'][i]['hours'][a]['weeks'][0]['classes'][0]['dates'][0]['dates_raw'])
            # print(res_dict['days'][i]['hours'][a]['weeks'][0]['classes'][0]['teacher'])
            # print(res_dict['days'][i]['hours'][a]['weeks'][0]['classes'][0]['place'])
            print(res_dict['days'][i]['hours'][a]['weeks'][0]['classes'][0]['class'] + " " +
                  res_dict['days'][i]['hours'][a]['weeks'][0]['classes'][0]['type'] + " " +
                  res_dict['days'][i]['hours'][a]['weeks'][0]['classes'][0]['teacher'] + " " +
                  res_dict['days'][i]['hours'][a]['weeks'][0]['classes'][0]['place'] + "\n")
        except:
            pass
    print("\n")
