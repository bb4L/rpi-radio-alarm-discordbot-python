# rpi-radio-alarm-discordbot-python
python discordbot for the rpi-radio-alarm

## installation
1) ```pip install -r requirements.txt```
2) configure the values for the ```.env```
3) ```python bot.py```

## commands
``get alarm [id]`` the specific alarm

``alarms``  list all alarms

``c alarm [id] [key] [value]``  change the alarm with the ``[id]`` and set for the acording value the key.
There may be multiple ``[key] [value]``!  

``s radio`` start the radio

``st radio`` stop the radio