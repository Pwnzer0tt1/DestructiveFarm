import datetime
import requests

"""
IGNORED_TEAMS = [0,6]
'TEAMS': {  f"{team['shortname']}" : '10.60.{}.1'.format(team["teamId"])  
                for team in requests.get(url="http://10.10.0.1/api/scoreboard/table/1", timeout=1).json()["scoreboard"] 
                if not team["teamId"] in IGNORED_TEAMS },
"""

CONFIG = {
    # Don't forget to remove the old database (flags.sqlite) before each competition.

    # The clients will run sploits on TEAMS and
    # fetch FLAG_FORMAT from sploits' stdout.
    "TEAMS": {},
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
    'SYSTEM_TOKEN': 'CHANGE_ME',
    'SYSTEM_URL': 'http://10.10.0.1:8080/flags',
    'FLAG_IDS_URL': 'http://10.10.0.1:8081/flagIds',
    'HTTP_TIMEOUT': 30,
    
    # The server will submit not more than SUBMIT_FLAG_LIMIT flags
    # every SUBMIT_PERIOD seconds. Flags received more than
    # FLAG_LIFETIME seconds ago will be skipped.
    'SUBMIT_FLAG_LIMIT': 1000,
    'SUBMIT_PERIOD': 20,
    'FLAG_LIFETIME': 5 * 120,
    

    # Password for the web interface. You can use it with any login.
    # This value will be excluded from the config before sending it to farm clients.
    'SERVER_PASSWORD': None, # No Authentication

    # Use authorization for API requests
    'API_TOKEN': None # No Authentication
}
