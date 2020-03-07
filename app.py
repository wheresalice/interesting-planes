from opensky_api import OpenSkyApi
from flask import Flask
import pandas as pd

api = OpenSkyApi()
app = Flask(__name__,static_url_path='',
            static_folder='public_html',)

aircraft_db = pd.read_csv('data/aircraft_db.csv')


def get_icon(icao):
    icons_list = ['a', 'b', 'c','d', 'e', 'f', 'l']

    try:
        plane_mdl = aircraft_db[aircraft_db['icao'] == icao]['mdl'].iloc[0]
       # print (plane_mdl)
    except:
        plane_mdl ='0generic'
    if plane_mdl[0] in icons_list:
        return plane_mdl[0] + '.svg'
    else:
        return 'generic.svg'


def states_to_geojson(states):
    geojson = {}
    geojson['type'] = 'FeatureCollection'
    geojson['features'] = []
    for state in states.states:
        point = {}
        point['type'] = 'Feature'
        point['properties'] = {'icao': state.icao24, 'callsign': state.callsign, 'origin_country': state.origin_country,
                             'on_ground': state.on_ground, 'velocity': state.velocity, 'spi': state.spi, 'icon': get_icon(state.icao24), 'heading': state.heading}
        point['geometry'] = {'type': 'Point', 'coordinates': [state.longitude, state.latitude]}
        geojson['features'].append(point)
    return geojson


@app.route('/api')
def hello():
    s = api.get_states(bbox=[49.82380908513249, 59.478568831926395, -10.8544921875, 2.021484375])
    return states_to_geojson(s)
