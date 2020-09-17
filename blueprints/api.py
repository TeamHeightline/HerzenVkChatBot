import requests

# payload = {'faculty': 'институт информационных технологий и технологического образования', 'level': "бакалавриат",
#            "type":"очная форма обучения"}

# r = requests.get('https://herzen-timetable.herokuapp.com/api/timetable/programs', params=payload)
# print(r.text)
payload = {"groupURL": "/static/schedule_view.php?id_group=12459&sem=1"}
r = requests.get('https://herzen-timetable.herokuapp.com/api/timetable/group', payload)
print(r.text)