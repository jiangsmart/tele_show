"""
创建蓝图，导入包下的各个视图函数
"""

from flask import Blueprint

web = Blueprint('web', __name__)

from . import autochat
from . import home
from . import mapserve
from . import auth

