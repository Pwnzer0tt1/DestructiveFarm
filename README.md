Pwnzer0tt1's Destructive Farm
================
 
Exploit farm for attack-defense CTF competitions!

<p align="center">
    <img src="https://raw.githubusercontent.com/Pwnzer0tt1/DestructiveFarm/master-ccit/docs/images/farm_server_screenshot.png" width="700">
</p>

## Differences between stock and Pwnzer0tti1's Destructive Farm

1. Added ticks to the config file. They are easily configurable in `server/config.py` with very little effort. 
```
    'TICK_DURATION': 120,#in seconds       (yyyy,mm,dd,hh,mm)
    'START_TIME' : round(datetime.datetime(2022, 6, 14, 22, 0).timestamp()),
    'END_TIME' : round(datetime.datetime(2022, 6, 15, 12, 0).timestamp()),
```

2. Added a table showing Teams with the number of every flag captured by a sploit in a specified tick.
<p align="center">
    <img src="https://raw.githubusercontent.com/Pwnzer0tt1/DestructiveFarm/master-ccit/docs/images/table_screenshot.png" width="700">
</p>

3. Beatuiful chart showing flags/tick per each sploit.

4. Dark Mode! 

5. Dark Mode!

6. Did I mention? Dark Mode!

## TODO

-Automatic updates every tick

## Original Authors

Copyright &copy; 2017&ndash;2018 [Aleksandr Borzunov](https://github.com/borzunov)

Inspired by the [Bay's farm](https://github.com/alexbers/exploit_farm).
