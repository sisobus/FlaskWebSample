#!/usr/bin/python
import sys
import os
import logging
logging.basicConfig(stream=sys.stderr)
cur_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,cur_path)
print sys.path
from Application.routes import app as application
