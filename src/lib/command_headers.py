from src.config.config import *

commands = {

    '!game': {
        'limit': 30,
        'argc': 0,
        'return': 'command'
    },

    # Simple commands
    '!keyboard': {
        'limit': 30,
        'return': 'ProgX uses a CMStorm QuickFire Rapid with Brown Switches.'
    },

    '!mouse': {
        'limit': 30,
        'return': 'ProgX uses a Logitech G500.'
    },

}

for channel in config['channels']:
    for command in commands:
        commands[command][channel] = {}
        commands[command][channel]['last_used'] = 0
