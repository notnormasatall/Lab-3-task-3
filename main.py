'''
The following module creates a webpage, where user can enter any Twitter
nickname and generatates a map with that profile's follower's locations.
'''

from flask import Flask, render_template, request
import folium as fl
from friends_map import find_locations
from twitter_followers import gen_followers


app = Flask(__name__)


@app.route("/")
def index():
    '''
    The function generates index.html file
    '''
    return render_template("index.html")


@app.route("/followers", methods=["POST"])
def register():
    '''
    The function generates a map with locations of user's followers on Twitter.
    '''
    nickname = request.form.get("nickname")

    if not nickname:
        return render_template("failure.html")

    js_data = gen_followers(nickname)
    data = find_locations(js_data)

    lat = data['Lat'].tolist()
    lon = data['Lon'].tolist()
    nicknames = data['Nickname'].tolist()
    locations = data['Location'].tolist()
    length = len(nicknames)

    friend_map = fl.Map(zoom_start=5)

    friend_points = fl.FeatureGroup(name='Film map')
    for _ in range(length):

        if lat[_] == 0.000000:
            pass

        html = """
        <strong>
        <h5><b>@{}</b></h5>
        <p><b>Location: </b></br>{}
        </strong>
        """

        friend_points.add_child(fl.Marker(location=[lat[_], lon[_]],
                                          popup=html.format(
            nicknames[_], locations[_]), icon=fl.Icon()))

    friend_map.add_child(friend_points)
    friend_map.save('./templates/FollowersAroundYou.html')

    return friend_map._repr_html_()


if __name__ == "__main__":
    app.run(debug=True)
