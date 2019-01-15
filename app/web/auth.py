from flask import render_template
from . import web


@web.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')

@web.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/register.html')