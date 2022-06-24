import datetime
import requests, json

IGNORED_TEAMS = [0,5]

CONFIG = {
    # Don't forget to remove the old database (flags.sqlite) before each competition.

    # The clients will run sploits on TEAMS and
    # fetch FLAG_FORMAT from sploits' stdout.
    'TEAMS': {  f"{team['name']} #{id}" : '10.60.{}.1'.format(id)  
                for id,team in enumerate(requests.get(url="http://10.10.0.1/api/game.json").json()["teams"]) 
                if not id in IGNORED_TEAMS },
    #'TEAMS': {'Team #{}'.format(i): '10.60.{}.1'.format(i)
    #          for i in range(1, 38 + 1)},
    'FLAG_FORMAT': r'[A-Z0-9]{31}=',

    'TICK_DURATION': 120,
    'START_TIME' : round(datetime.datetime(2022, 6, 16, 12, 0).timestamp()),
    'END_TIME' : round(datetime.datetime(2022, 6, 16, 22, 0).timestamp()),
    
    # This configures how and where to submit flags.
    # The protocol must be a module in protocols/ directory.

    'SYSTEM_PROTOCOL': 'ccit_http',
    'SYSTEM_HOST': '127.0.0.1',
    'SYSTEM_PORT': 4444,
    'SYSTEM_TOKEN': '5fe56451972cb2e8be0703412981a718',
    'SYSTEM_URL': 'http://10.10.0.1:8080/flags',
    'FLAG_IDS_URL': 'http://10.10.0.1:8081/flagIds',

    # 'SYSTEM_PROTOCOL': 'ructf_http',
    # 'SYSTEM_URL': 'http://monitor.ructfe.org/flags',
    # 'SYSTEM_TOKEN': 'your_secret_token',

    # 'SYSTEM_PROTOCOL': 'volgactf',
    # 'SYSTEM_HOST': '127.0.0.1',

    # 'SYSTEM_PROTOCOL': 'forcad_tcp',
    # 'SYSTEM_HOST': '127.0.0.1',
    # 'SYSTEM_PORT': 31337,
    # 'TEAM_TOKEN': 'your_secret_token',

    # The server will submit not more than SUBMIT_FLAG_LIMIT flags
    # every SUBMIT_PERIOD seconds. Flags received more than
    # FLAG_LIFETIME seconds ago will be skipped.
    'SUBMIT_FLAG_LIMIT': 100,
    'SUBMIT_PERIOD': 1,
    'FLAG_LIFETIME': 10 * 60,

    # Password for the web interface. You can use it with any login.
    # This value will be excluded from the config before sending it to farm clients.
    'SERVER_PASSWORD': 'ccit-poliba',

    # Use authorization for API requests
    'ENABLE_API_AUTH': False,
    'API_TOKEN': '00000000000000000000'
}
