from rpiradioalarm import ResponseParser, COMMANDS


class DiscordResponseParser(ResponseParser):

    def __init__(self):
        super(DiscordResponseParser, self).__init__()
        self.parse_fun = {COMMANDS.GET_ALARMS: self.__get_alarms, COMMANDS.GET_ALARM: self.__get_alarm,
                          COMMANDS.CHANGE_ALARM: self.__change_alarm, COMMANDS.START_RADIO: self.__start_radio,
                          COMMANDS.STOP_RADIO: self.__stop_radio}

    def __get_alarms(self, args, response):
        return f'__**Alarms**__ \n' + f'{"".join("__**Alarm " + str(idx) + "**__" + self.__alarm_string(alarm, True) for idx, alarm in enumerate(response))}'

    def __get_alarm(self, args, response):
        print('get ALARM')
        return f'{"".join("__**Alarm " + str(args) + "**__" + self.__alarm_string(response[0], True))}'

    def __start_radio(self, args, response):
        return self.__radio_string(args, response)

    def __stop_radio(self, args, response):
        return self.__radio_string(args, response)

    def __change_alarm(self, args, response):
        return self.__get_alarm(args, response)

    @staticmethod
    def __alarm_string(alarm, preline):
        print(alarm)
        if preline:
            prefix = '\n\t'
        else:
            prefix = ''
        return prefix + f'name: {alarm["name"]} \n\t' \
                        f'time: {alarm["hour"]}:{alarm["min"]} \n\t' \
                        f'days: {alarm["days"]} \n\t' \
                        f'on: {alarm["on"]} \n'

    @staticmethod
    def __radio_string(args, response):
        return f"__**Radio**__ Is playing:" + str(response["isPlaying"])
