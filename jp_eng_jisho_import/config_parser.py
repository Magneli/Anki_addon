# -*- coding: utf-8 -*-
# python 2.7


import codecs

deck_name = None
model_name = None


def read_config():
    global deck_name
    try:
        cfgfile = open("deck_name.ini", 'r')
        deck_name = cfgfile.read()
        cfgfile.close()
    except:
        print "wat"
        pass


def write_config():
    cfgfile = open("deck_name.ini", 'w')

    cfgfile.write("漢字")
    cfgfile.close()


def write_default_config():
    cfgfile = open("deck_name.ini", 'w')
    cfgfile.close()


# write_default_config()
# write_config()
read_config()

# deck_name = "かんじ"
# model_name = "asdasd"
print deck_name
print model_name


# write_config()
