import configparser



config = configparser.ConfigParser()
config.read('config.conf')
print(config.sections())
print(config['MySQL']['host'])
print(config['MySQL']['port'])