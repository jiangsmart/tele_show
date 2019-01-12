from flask import render_template
from . import web


@web.route('/mapserve', methods=['GET'])
def mapserve():
    return render_template('map/mapserve.html')
