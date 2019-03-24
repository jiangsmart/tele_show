from flask import render_template, request, url_for, redirect, current_app, flash
from flask_login import login_user, login_required
from . import web
from app.models.user import User
import sys

sys.path.append('../neo4j/')
from conversation import Graph4Match


@web.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        graph = Graph4Match(current_app.config['NEO4J_IP'], current_app.config['NEO4J_USER'],
                            current_app.config['NEO4J_PASSWORD'])
        login_user(user, False)
        return redirect(url_for('web.home'))
    return render_template('auth/register.html')
    # form = RegisterForm(request.form)
    # if request.method == 'POST' and form.validate():
    #     user = User()
    #     user.set_attrs(form.data)
    #     db.session.add(user)
    #     db.session.commit()
    #     login_user(user, False)
    #     return redirect(url_for('web.index'))
    # return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    # form = LoginForm(request.form)
    if request.method == 'POST':
        graph = Graph4Match(current_app.config['NEO4J_IP'], current_app.config['NEO4J_USER'],
                            current_app.config['NEO4J_PASSWORD'])
        user = User().first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或密码错误', category='login_error')
    return render_template('auth/login.html')
