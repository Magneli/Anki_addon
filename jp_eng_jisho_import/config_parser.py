# -*- coding: utf-8 -*-
# python 2.7

import ConfigParser

config = ConfigParser.ConfigParser()


def write_config():
    cfgfile = open("config.ini", 'w')
    config.add_section('Deck')
    config.set('Deck', 'Deck name', '語彙')
    config.set('Deck', 'Model', 'Japanese-eng words')
    config.write(cfgfile)
    cfgfile.close()

#write_config()

config.read("config.ini")
options = config.options('Deck')
asd = config.get('Deck', 'Deck name')
print config.sections()
print asd
