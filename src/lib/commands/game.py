"""
!game: Displays information about the last game played

Developed by Gustavo Valdez Santiago <contacto@gustavovaldezsan.com>
"""

# coding: utf8

from urllib2 import Request, urlopen, URLError
import json
import datetime


def game():
    ## TODO: Generate this from config
    request = Request('http://us.battle.net/api/sc2/profile/690999/1/ProgX/matches')

    try:
        # Extract the json from the Starcraft 2 Api
        response = urlopen(request)
        result = response.read()
        json_response = json.loads(result)

        # Extract just the last match
        matches = json_response['matches']
        last_match = matches[0]

        # Count the time since the last game
        game_time = datetime.datetime.fromtimestamp(int(last_match['date']))
        current_time = datetime.datetime.utcnow()
        time_delta = (current_time - game_time).seconds

        ## Format the time accordingly

        if time_delta < 60:  # Less than a minute ago
            time_string = str(time_delta) + ' seconds'
        elif time_delta == 60:  # Exactly 1 minute
            time_string = '1 minute'
        elif 61 < time_delta < 3600:  # Between 1 minute and 1 hour
            time_string = str(time_delta / 60) + ' minutes'
        elif 3600 <= time_delta < 7201:  # 1 to 1.999999 hours
            time_string = '1 hour'
        else:  # Start at 2 hours
            time_string = str(time_delta / 3600) + ' hours'

        # Create the chat string base on the results from the last game
        chat_string = "ProgX "
        chat_string += 'won' if last_match['decision'] == 'WIN' else 'lost'
        chat_string += ' a ' + '1v1' if last_match['type'] == 'SOLO' else 'team game'
        chat_string += ' on ' + last_match[ 'map'] + ' '
        chat_string += time_string + ' ago.'

        return chat_string

    except URLError:
        return 'API Timed out. Blame Blizzard!'
