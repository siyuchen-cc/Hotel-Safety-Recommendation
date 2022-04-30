from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import app
from db import get_db

bp = Blueprint('hotelPage', __name__, url_prefix='/hotelPage')

@bp.route('/<int:idx>', methods=('GET', 'POST'))
def hotel_page(idx):
    hotel_info = app.hotels[idx-1]
    lat = hotel_info["latitude"]
    lng = hotel_info["longitude"]

    db = get_db()
    cnt = db.execute(
        'select count(*) as cnt'
        ' from crimes'
        ' where abs( latitude - ? )< 0.01 and abs( longitude - ? )< 0.01;',
        (lat, lng)
    ).fetchone()

    rate = round(cnt[0] / 209211, 4)

    return render_template('hotel.html', hotel=hotel_info, rate=rate)