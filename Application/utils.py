#-*- coding:utf-8 -*-
from datetime import date, datetime, timedelta
import commands
import os
import json
def create_directory(directory_name):
    if not os.path.exists(directory_name):
        command = 'mkdir %s'%directory_name
        ret = commands.getoutput(command)
        command = 'chmod 777 %s'%directory_name
        ret = commands.getoutput(command)

