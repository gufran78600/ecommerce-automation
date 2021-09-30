import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")


class Readconfig:
    @staticmethod
    def getApplicationURL():
        baseURL = config.get('common info', 'baseURL')
        return baseURL

    @staticmethod
    def getApplicationUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getApplicationPassword():
        password = config.get('common info', 'password')
        return password

