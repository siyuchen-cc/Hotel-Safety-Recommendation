from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

import graphs
import hotel
import os
import tree
import requests


app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)
app.register_blueprint(graphs.bp)
app.register_blueprint(hotel.bp)

# ensure the instance folder exists and init database
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# db.init_app(app)


def init_hotels(an="2", rn="1", cn="2", ob="popularity", cur="USD", id="true"):
    url = "https://booking-com.p.rapidapi.com/v1/hotels/search"

    querystring = {
        "checkout_date": "2022-10-01",
        "units": "metric",
        "dest_id": "20033173",  # chicago id : 20033173
        "dest_type": "city",
        "locale": "en-us",
        "adults_number": an,
        "order_by": ob,
        "filter_by_currency": cur,
        "checkin_date": "2022-09-30",
        "room_number": rn,
        "children_number": cn,
        "page_number": "0",
        "children_ages": "5,0",
        "categories_filter_ids": "class::2,class::4,free_cancellation::1",
        "include_adjacency": id
    }

    headers = {
        "X-RapidAPI-Host": "booking-com.p.rapidapi.com",
        "X-RapidAPI-Key": "5a080ada46mshc35c1b571b40699p16cc73jsnfd925b51bf56"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    res = response.json()
    return res["result"]


hotels = init_hotels()


@app.route('/')
def create_app():
    tree.get_tree()
    return render_template('index.html', hotels=hotels)


@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        ob = request.form['order']
        an = request.form['adults_number']
        cn = request.form['children_number']
        rn = request.form['room_number']
        cur = request.form['currency']
        id = request.form['include_adjacency']
        new_hotels = init_hotels(an, rn, cn, ob, cur, id)
        return render_template('index.html', hotels=new_hotels)


if __name__ == "__main__":
    app.run(debug=True)