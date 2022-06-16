import time
import math

from flask import request, jsonify

from server import app, auth, database, reloader
from server.models import FlagStatus
from server.spam import is_spam_flag

config = reloader.get_config()


@app.route('/api/get_config')
@auth.api_auth_required
def get_config():
    return jsonify({key: value for key, value in config.items()
                    if 'PASSWORD' not in key and 'TOKEN' not in key})


@app.route('/api/post_flags', methods=['POST'])
@auth.api_auth_required
def post_flags():
    flags = request.get_json()
    flags = [item for item in flags if not is_spam_flag(item['flag'])]

    cur_time = round(time.time())
    tick = math.floor((cur_time - config["START_TIME"]) /  config["TICK_DURATION"])
    rows = [(item['flag'], item['sploit'], item['team'], cur_time, tick, FlagStatus.QUEUED.name)
            for item in flags]

    db = database.get()
    db.executemany("INSERT OR IGNORE INTO flags (flag, sploit, team, time, tick, status) "
                   "VALUES (?, ?, ?, ?, ?, ?)", rows)
    graph_row = [flags[0]['sploit'] + str(tick), flags[0]['sploit'], tick]
    db.execute("INSERT OR IGNORE INTO stats VALUES ( ?, 0 , ? ,?)", graph_row) 
    db.execute("UPDATE stats SET count = count + ? WHERE id LIKE ?", [len(flags), flags[0]['sploit'] + str(tick)])

    db.commit()

    return ''
