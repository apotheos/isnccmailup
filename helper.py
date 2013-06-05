from app import config


def get_level(percentage):
    levels = config['application']['levels']
    if percentage >= levels[0]:
        return 'good'
    elif percentage >= levels[1]:
        return 'warning'
    else:
        return 'bad'
