import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext
import pandas as pd

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('db-load-data')
@with_appcontext
def load_data():
    db = get_db()
    crimes = pd.read_csv("../Crimes.csv")
    police = pd.read_csv("../Police_Stations.csv")

    for idx, row in crimes.iterrows():
        to_db = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15]]
        try:
            db.execute(
                # insert data
                "INSERT INTO crimes (cases, date, block, iucr, primaryDescription, secondaryDescription, locationDescription, arrest, domestic, beat, ward, fbiCD, x, y, latitude, longitude)"
                " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                to_db)
            db.commit()
        except db.IntegrityError:
            error = "Can't insert crime data right now."
        else:
            pass

    for idx, row in police.iterrows():
        to_db = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]]
        try:
            db.execute(
                # insert data
                "INSERT INTO police (district, name, address, city, state, zip, website, phone, fax, tty, x, y, latitude, longitude)"
                " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                to_db)
            db.commit()
        except db.IntegrityError:
            error = "Can't insert crime data right now."
        else:
            pass

    print("successfully load crimes data")

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(load_data)
    print("Initialized the database.")