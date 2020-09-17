
import requests

payload = {'faculty': 'институт информационных технологий и технологического образования', 'level': "бакалавриат"}

r = requests.get('https://herzen-timetable.herokuapp.com//api/timetable/programs', params=payload)
print(r.text)
