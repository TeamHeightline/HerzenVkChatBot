import ast
import re

import requests
import json
import logging

from blueprints.services.dbsystem import get_time_table_file, add_time_table_file


async def get_timetable(url):
    res_dict = await get_time_table_file(table_url=url)
    # print(res_dict)
    # Отказываемся от идеи проверки наличая насписания каждый раз, получение и сохраниение расписания только при
    # регистрации
    if len(res_dict) < 100:
        res_dict = await get_json_from_server(url=url)
        logging.debug("На сервере json не найден")
        # if len(res_dict) > 100:
        try:
            logging.debug("Попытка сохранения файла на сервере")
            await add_time_table_file(table_url=url, table_file=str(res_dict))
        except:
            pass
    timetable_text = await sort_server_json(res_dict)
    return timetable_text


async def get_json_from_server(url: str) -> dict:
    payload = {"groupURL": url}
    r = requests.get('https://herzen-timetable.herokuapp.com/api/timetable/group', payload)

    res_dict = json.loads(r.content)
    logging.debug("Получено расписание с сервера" + str(res_dict))
    return res_dict


async def sort_server_json(timetable_dict: dict) -> str:
    timetable_text = ''
    # print(timetable_dict)
    res_dict = timetable_dict
    # res_dict = re.sub("^\s+|\n|\r|\s+$", '', res_dict)
    res_dict = ast.literal_eval(str(res_dict))
    # print(type(res_dict))
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
    # return timetable_text


def get_timetable_test(url):
    payload = {"groupURL": url}
    r = requests.get('https://herzen-timetable.herokuapp.com/api/timetable/group', payload)

    res_dict = json.loads(r.content)
    # print(str(res_dict).replace("'", "\""))
    return str(res_dict).replace("'", "\"")


# print(get_timetable_test("/static/schedule_view.php?id_group=12460&sem=1"))
