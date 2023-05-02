from configparser import ConfigParser


def read_configuration(category,key):
    config=ConfigParser()
    config.read("C:\\Users\\91789\\PycharmProjects\\miniProject\\configs01.ini")
    return config.get(category,key)