import json
import os
from http.client import HTTPConnection
from dotenv import load_dotenv
from helper.parser import COMMANDS, ALARM_IDX


class ApiHelper(object):
    conn: HTTPConnection

    def __init__(self):
        load_dotenv()
        self.conn = HTTPConnection(os.getenv('RPI-RADIO-ALARM-URL'))
        self.FUNCTIONS = {COMMANDS.GET_ALARMS: self.get_alarms, COMMANDS.GET_ALARM: self.get_alarms,
                          COMMANDS.CHANGE_ALARM: self.change_alarm}

    def do_command(self, cmd, args):
        return self.FUNCTIONS.get(cmd)(args)

    def get_alarms(self, args):
        has_args = len(args) > 0
        if has_args:
            self.conn.request("GET", '/alarm/' + str(args).replace(' ', ''))
        else:
            self.conn.request("GET", "/alarm")
        resp = json.loads(self.conn.getresponse().read().decode())

        if isinstance(resp, dict):
            resp = [resp]

        return (
                   '' if has_args else f'__**Alarms**__ \n') + f'{"".join("__**Alarm " + str(args if has_args else idx) + "**__" + self.alarm_string(alarm, True) for idx, alarm in enumerate(resp))}'

    def change_alarm(self, args=dict):
        alarm_id = args.pop(ALARM_IDX)
        print(args)
        headers = {"Content-type": "application/json", "Accept": "text/plain"}
        self.conn.request("PUT", "/alarm/" + str(alarm_id), json.dumps(args), headers=headers)
        resp = json.loads(self.conn.getresponse().read().decode())

        return f"__**Alarm {alarm_id}**__" + self.alarm_string(resp, True)

    @staticmethod
    def alarm_string(alarm, preline):
        if preline:
            prefix = '\n\t'
        else:
            prefix = ''
        return prefix + f'name: {alarm["name"]} \n\t' \
                        f'time: {alarm["hour"]}:{alarm["min"]} \n\t' \
                        f'days: {alarm["days"]} \n\t' \
                        f'on: {alarm["on"]} \n'
