from flask import render_template
from . import web


@web.route('/mapserve', methods=['GET'])
def mapserve():
    points = list()
    with open('app/web/scene_show.csv', 'r') as fin:
        for line in fin:
            id, (lon, lat, r) = line.strip().split(',')[0], map(float, line.strip().split(',')[1:])
            points.append((id, lon, lat, r))
    # print(points)
    return render_template('map/mapserve.html', points=points)


@web.route('/mapserve1', methods=['GET'])
def mapserve1():
    points = list()
    with open('app/web/station.csv', 'r') as fin:
        for line in fin:
            id, (lon, lat, r) = line.strip().split(',')[0], map(float, line.strip().split(',')[1:])
            points.append((id, lon, lat, r))
    # print(points)
    return render_template('map/mapserve1.html', points=points)