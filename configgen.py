import configparser

config = configparser.ConfigParser()
config.add_section('LEDPinouts')
config['LEDPinouts']['Data'] = '13'
config['LEDPinouts']['Clock'] = '26'
config['LEDPinouts']['Latch'] = '19'
config.add_section('KeypadPinouts')
config['KeypadPinouts']['Row1'] = '4'
config['KeypadPinouts']['Row2'] = '17'
config['KeypadPinouts']['Row3'] = '27'
config['KeypadPinouts']['Row4'] = '18'
config['KeypadPinouts']['Column1'] = '12'
config['KeypadPinouts']['Column2'] = '16'
config['KeypadPinouts']['Column3'] = '20'
config['KeypadPinouts']['Column4'] = '21'

with open("habitpi.conf","w") as configfile:
    config.write(configfile)
configfile.close()
print("Config file written")
