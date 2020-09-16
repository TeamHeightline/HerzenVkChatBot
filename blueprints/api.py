import requests

r = requests.get('https://herzen-timetable.herokuapp.com/api/timetable/faculties')

print(r.text)