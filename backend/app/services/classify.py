import requests


def classify(model, sent=""):
    return model.predict(sent), requests.codes.ok