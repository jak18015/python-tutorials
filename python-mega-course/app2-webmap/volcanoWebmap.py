# To create the webmap, Python itself isn't capable, need external libraries for webmaps
# Need a library called Folium
import folium
import pandas
import numpy
tiles = "Stamen Terrain"

# read in volcanoes.txt
data = pandas.read_csv("volcanoes.txt")

#html stylized formatting with google links
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

# lists to iterate markers for all sites
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

#color defining function
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    elif elevation > 3000:
        return 'red'
    else:
        return 'black'

map = folium.Map(location=[0,0], zoom_start = 2, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="World Population")

# for loop to add multiple markers based on both lat on lon lists
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(radius = 10, location=[lt, ln], fill = True, popup=folium.Popup(iframe), color = color_producer(el)))

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                                      else 'orange' if 10000000 <= x['properties']['POP2005'] < 50000000 
                                                      else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")