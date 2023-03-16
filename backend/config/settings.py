from os import environ


def convert_list_object_from_string(string):
    """Convert a string to a list of objects"""
    return [] if not string else \
        list(map(lambda x: x.strip(), string.split(",")))


class Config():
    APP_API_PREFIX = environ.get("APP_API_PREFIX")
    SECRET_KEY = environ.get("SECRET_KEY")

    NETWORK_PATH = environ.get("NETWORK_PATH")
    NETWORK_CONF_PATH = environ.get("NETWORK_CONF_PATH")
    SEGMENTER_DIR = environ.get("SEGMENTER_DIR")
    LABEL2INT = {'Anger': 0, 'Disgust': 1, 'Enjoyment': 2, 'Fear': 3, 'Other': 4, 'Sadness': 5, 'Surprise': 6}
    INT2LABEL = {0: 'Anger', 1: 'Disgust', 2: 'Enjoyment', 3: 'Fear', 4: 'Other', 5: 'Sadness', 6: 'Surprise'}
    NUM_CLASS = int(environ.get("NUM_CLASS"))
    MAX_LEN = int(environ.get("MAX_LEN"))