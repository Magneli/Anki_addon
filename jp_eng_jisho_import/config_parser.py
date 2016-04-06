# -*- coding: utf-8 -*-
# python 2.7
import codecs

deck_name = None

def read_config():
    global deck_name
    try:
        cfgfile = codecs.open("deck_name.ini", 'r','utf-8')
        deck_name = cfgfile.read()
        cfgfile.close()
    except:
        deck_name = u'語彙'
        pass


def write_config():
    cfgfile = codecs.open("deck_name.ini", 'w','utf-8')

    cfgfile.write(deck_name)
    cfgfile.close()


