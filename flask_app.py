"""Task3 main program"""
import flask
import json
import geopy
import folium
import urllib
import twitter2

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = '1e21885e0fbc0f7b7bbe1a49996639411a44124d2d45f679'

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/', methods = ['POST'])
def findlocations():
    if flask.request.method == "POST":
        nickname = flask.request.form['content']
        print(nickname)
        try:
            data = twitter2.get_data(nickname)
        except urllib.error.HTTPError:
            return flask.render_template('index.html')
        data = json.loads(data)

    geolocator = geopy.geocoders.Nominatim(user_agent = 'Simplyname')

    map1 = folium.Map(location = (40,30), zoom_start = 10)
    fg1 = folium.FeatureGroup(name ='Locations of your friends')
    for i in data['users']:
        try:
            location = geolocator.geocode(i['location'])
        except:
            continue
        if location:
            fg1.add_child(folium.Marker(location = (location.latitude,location.longitude), popup = i['screen_name'], icon = folium.Icon()))
    map1.add_child(fg1)
    map1.add_child(folium.LayerControl())
    map1.save('templates/map.html')
    return flask.render_template('map.html')

# if __name__=='__main__':
#     app.run(debug = False,  host = '127.0.0.1', port=8080)