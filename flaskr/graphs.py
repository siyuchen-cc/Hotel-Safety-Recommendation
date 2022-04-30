from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from matplotlib.figure import Figure
import base64
from io import BytesIO
import pandas as pd
import numpy as np

bp = Blueprint('graph', __name__, url_prefix='/graphs')
crimes = pd.read_csv('../Crimes.csv')
df1= crimes.groupby(' PRIMARY DESCRIPTION').count()
df1.sort_values(by='LOCATION', ascending=False, inplace=True)
df1=df1.head(20)
crimes['street']= crimes['BLOCK'].str.split("X ").str[1]

df2= crimes.groupby('street').count()
df2.sort_values(by='CASE#', ascending=False, inplace=True)
df2=df2.head(20)

crimes['month']= crimes['DATE  OF OCCURRENCE'].str.split("/").str[0]
df3= crimes.groupby('month').count()
df3.sort_index( ascending=True, inplace=True)

df4= crimes.groupby(' LOCATION DESCRIPTION').count()
df4.sort_values(by='CASE#', ascending=False, inplace=True)
df4=df4.head(20)


def draw_img_1():
    # Generate the figure **without using pyplot**.
    fig = Figure()

    # Plot your image here:
    ax = fig.subplots()
    ax.bar(
        x=df1.index,
        height=df1['CASE#']
    )
    ax.set_title('Top 20 Crime Types in Chicago', fontsize=15)
    ax.set_xticklabels(df1.index, rotation=20,  ha='right', fontsize=5)

    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")

    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data


def draw_img_2():
    # Generate the figure **without using pyplot**.
    fig = Figure()

    # Plot your image here:
    ax = fig.subplots()
    ax.bar(
        x=df1.index,
        height=df1['CASE#']
    )
    ax.set_title('Most Dangerous Street in Chicago', fontsize=15)
    ax.set_xticklabels(df1.index, rotation=20,  ha='right', fontsize=5)

    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")

    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data


def draw_img_3():
    # Generate the figure **without using pyplot**.
    fig = Figure()

    # Plot your image here:
    ax = fig.subplots()
    ax.plot(
        df3.index, df3['CASE#']
    )
    ax.set_title('Crime in Month', fontsize=15)
    ax.set_xlabel('month of the year')


    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")

    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data


def draw_img_4():
    # Generate the figure **without using pyplot**.
    fig = Figure()

    # Plot your image here:
    ax = fig.subplots()
    ax.bar(
        x=df4.index,
        height=df4['CASE#']
    )
    ax.set_title('Top place for crimes', fontsize=15)
    ax.set_xticklabels(df4.index, rotation = 20,  ha='right', fontsize=5)
    ax.set_xlabel('crime location ')

    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")

    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data


@bp.route('/', methods=('GET', 'POST'))
def graph_page():
    url1 = draw_img_1()
    url2 = draw_img_2()
    url3 = draw_img_3()
    url4 = draw_img_4()

    return render_template('graph.html', url1=url1, url2=url2, url3=url3, url4=url4)