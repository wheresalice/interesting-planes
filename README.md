# OpenSky Network Map

This code renders a map of the UK using [Leaflet.js](https://leafletjs.com/), and shows current planes overhead from the [OpenSky network](https://opensky-network.org/apidoc/rest.html#flights-all).

It was created by a group of people during #OpenDataDay at Open Data Manchester

## Usage

1. `python3 -m venv venv`
2. `pip3 install -r requirements.txt`
3. `env FLASK_APP=app.py flask run`
4. `open http://127.0.0.1:5000/index.html`

## Known Bugs

* the root path doesn't load index.html
* all planes are facing south

## Architecture

The main application is a Python Flask app, serving the OpenSky data as GeoJSON on `/api`

Static files are served from `public_html`, including the html and css

## License

* Aircraft data from https://junzis.com/adb/data
* Icons from unknown
* Flight data from https://opensky-network.org/apidoc/rest.html#flights-all
