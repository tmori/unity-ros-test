#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import sys
import glob
import re
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('./', encoding='utf8'))

if len(sys.argv) != 4:
	print "ERROR: generate.py <name> <in_dir> <out_dir>"
	sys.exit()

name=sys.argv[1]
in_dir=sys.argv[2]
out_dir=sys.argv[3]

class RosMessageContainer:
    pass

class RosMessage:
    pass

def to_conv(name):
	return name.replace("int", "Int").replace("uInt", "UInt").replace("float", "Float")

container = RosMessageContainer()
container.to_conv = to_conv
container.msgs = []

files = glob.glob(in_dir + "/*.msg")
for file in files:
	ros_msg = RosMessage()
	tmp = re.split('[./]', file)
	msg_name = tmp[len(tmp) - 2]
	ros_msg.name = msg_name
	container.msgs.append(ros_msg)

tpl_name = name + '.tpl'
out_name = name + '.cs'


for e in container.msgs:
    file = open(out_dir + '/' + e.name+'.json')
    e.json_data = json.load(file)

tpl = env.get_template('utils/' + tpl_name)
out = tpl.render({'container':container})

print out.encode('utf-8')

