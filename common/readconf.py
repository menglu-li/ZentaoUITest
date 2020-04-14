import configparser
import os

dir_path = os.path.dirname(__file__)
config_path = os.path.join(dir_path, '../conf/conf.ini')

class ReadConf:
    def __init__(self,cf_path=config_path):
        self.config_path = cf_path
        self.configparser = configparser.ConfigParser()
        self.config_info = self.configparser.read(config_path, encoding = 'utf-8')

    def get_login_url(self):
        login_url = self.configparser.get('default', 'login_url')
        return login_url

    def get_report_url(self):
        report_url = self.configparser.get('default', 'report_url')
        return report_url

if __name__ == '__main__':
    print(ReadConf().get_login_url())




