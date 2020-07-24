import configparser

config = configparser.ConfigParser()
config.add_section('Pinouts')
config['Pinouts']['Data'] = '13'
config['Pinouts']['Clock'] = '26'
config['Pinouts']['Latch'] = '19'

with open("habitpi.conf","w") as configfile:
    config.write(configfile)
configfile.close()
print("Config file written")
