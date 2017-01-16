#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
import time
import urllib
import base64
import json
from datetime import datetime, timedelta
from flask import Flask, url_for
from flask import render_template, flash, redirect, session, request, g, jsonify
from flask import get_flashed_messages
from flask_paginate import Pagination
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from werkzeug import secure_filename
from werkzeug.datastructures import ImmutableMultiDict 
from werkzeug.datastructures import FileStorage
from sqlalchemy import func
from sqlalchemy import *
from config import (
        SECRET_KEY,
        )
app = Flask(__name__)
app.config['SECRET_KEY']                = SECRET_KEY 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

import utils

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='localhost',debug=True)
