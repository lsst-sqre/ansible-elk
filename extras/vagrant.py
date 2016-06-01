#!/usr/bin/env python
import sys
import os.path
import subprocess
import re
from paramiko import SSHConfig
from cStringIO import StringIO
from optparse import OptionParser
from collections import defaultdict
try:
    import json
except:
    import simplejson as json


parser = OptionParser(usage="%prog [options] --list | --host <machine>")
parser.add_option('--list', default=False, dest="list", action="store_true",
                  help="Produce a JSON consumable grouping of Vagrant servers for Ansible")
parser.add_option('--host', default=None, dest="host",
                  help="Generate additional host specific details for given host for Ansible")
(options, args) = parser.parse_args()

def get_list():
  return open("hosts.json").read()

def get_host(hostname):
  hosts = json.loads(open("hosts.json").read())
  return json.dumps(hosts["_meta"]["hostvars"][hostname])

if options.list:
  print(get_list())
  sys.exit(0)
elif options.host:
  print(get_host(options.host))
  sys.exit(0)
else:
  parser.print_help()
  sys.exit(0)
