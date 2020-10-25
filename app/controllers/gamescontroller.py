from app import app
from app.models.games import Games
from app.models.payments import Payments
from flask import render_template, request, redirect, url_for
from datetime import datetime
import random
import os
from werkzeug.utils import secure_filename

@app.route('/', methods = ['GET'])
def showIndex():
    games = Games()
    listgame = games.showAllGame() # dict in list
    return render_template('index.html',listgame=listgame)

@app.route('/Order/<games_id>/detail', methods = ['POST', 'GET'])
def order(games_id):
    # if request.method == 'POST':
    #     return render_template('payment')
    # else:
    games = Games(games_id)
    detail = games.getData()
    print(detail)
    return render_template('order.html', detail=detail)