from src.config.config import *

commands = {

    '!game': {
        'limit': 30,
        'argc': 0,
        'return': 'command'
    },

}

for channel in config['channels']:
    for command in commands:
        commands[command][channel] = {}
        commands[command][channel]['last_used'] = 0
