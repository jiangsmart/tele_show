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
    stations = list()
    scenes = list()
    with open('app/web/scene_station_show', 'r') as fin:
        for line in fin:
            fields = line.strip().split('\t')
            sc = fields[0]
            sceneid, name, sc_lon, sc_lat, sc_r = sc.split(',')
            scenes.append((sceneid, name, sc_lon, sc_lat, sc_r))
            if len(fields) == 1:
                continue
            sts = fields[1]
            for st in sts.split(';'):
                stationid, st_lon, st_lat, st_r, dis = st.split(',')
                st_r = str(1.5 * float(st_r))
                stations.append((stationid, st_lon, st_lat, st_r, name, dis))
                # print(points)
    return render_template('map/mapserve1.html', stations=stations, scenes=scenes)


@web.route('/mapserve2', methods=['GET'])
def mapserve2():
    stations = list()
    scenes = list()
    colors = list()
    with open('app/web/scene_station_show2', 'r') as fin:
        COLOR_PLUS = 55924  # 0xffffff/300=55924
        int_color = COLOR_PLUS
        for line in fin:
            int_color += COLOR_PLUS
            str_color = '#' + str(hex(int_color))[2:]
            fields = line.strip().split('\t')
            sc = fields[0]
            sceneid, name, lonlat, r = sc.split(',')
            lonlat_l = lonlat.split('/')
            r_l = r.split('/')
            for i, sc_r in enumerate(r_l):
                sc_lon, sc_lat = lonlat_l[i].split(':')
                scenes.append((sceneid, name, sc_lon, sc_lat, sc_r, str_color))
            if len(fields) == 1:
                continue
            sts = fields[1]
            for st in sts.split(';'):
                stationid, st_lon, st_lat, st_r, dis = st.split(',')
                st_r = str(1.5 * float(st_r))
                stations.append((stationid, st_lon, st_lat, st_r, name, dis, str_color))
                # print(points)
    return render_template('map/mapserve2.html', stations=stations, scenes=scenes)

@web.route('/mapserve3', methods=['GET'])
def mapserve3():
    stations = list()
    scenes = list()
    colors = list()
    with open('app/web/scene_station_show2', 'r') as fin:
        COLOR_PLUS = 55924  # 0xffffff/300=55924
        int_color = COLOR_PLUS
        for line in fin:
            int_color += COLOR_PLUS
            str_color = '#' + str(hex(int_color))[2:]
            fields = line.strip().split('\t')
            sc = fields[0]
            sceneid, name, lonlat, r = sc.split(',')
            lonlat_l = lonlat.split('/')
            r_l = r.split('/')
            for i, sc_r in enumerate(r_l):
                sc_lon, sc_lat = lonlat_l[i].split(':')
                scenes.append((sceneid, name, sc_lon, sc_lat, sc_r, str_color))
            if len(fields) == 1:
                continue
            sts = fields[1]
            for st in sts.split(';'):
                stationid, st_lon, st_lat, st_r, dis = st.split(',')
                st_r = str(1.5 * float(st_r))
                stations.append((stationid, st_lon, st_lat, st_r, name, dis, str_color))
                # print(points)
    return render_template('map/mapserve3.html', stations=stations, scenes=scenes)
