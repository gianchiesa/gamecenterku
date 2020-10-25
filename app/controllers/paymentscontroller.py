from app import app
from flask import render_template
from app.models.games import Games
from app.models.payments import Payments ## import kelas Project dari model
from flask import request, redirect, url_for, render_template
from datetime import datetime
import locale
import random

@app.route('/order/payment', methods = ['POST', 'GET'])
def payment():
	item = request.form.get('budget')
	user_id = request.form.get('user_id')
	items = request.form.get('items')
	items = items.replace('[','').replace(']','').split("',")
	harga = 0
	games_id = ''
	payment_method = request.form.get('payment_method')
	email = ''
	telepon = ''
	status = 'false'
	for i in items:
		i = i.split(',')
		if i[1] == item:
			harga = i[0].replace(' ','')[1:]
			break
	return render_template('payment.html',harga = harga, user_id=user_id, item=item, games_id=games_id, email=email, telepon=telepon, payment_method=payment_method, status=status)

@app.route('/qwerty123', methods = ['GET','POST'])
def showAdmin():
	payment = Payments()
	listpay = payment.showAllPayments()# dict in list
	return render_template('admin.html',listpay=listpay)

@app.route('/admin1/<payments_id>/Manage', methods = ['GET','POST'])
def adminManage(payments_id):
	payment = Payments(payments_id)
	view = payment.getData()
	print(view)
	return render_template('admin-manage.html',view=view)

@app.route('/Admin1/<payments_id>/Manage/confirm', methods = ['GET','POST'])
def confirmPayment(payments_id):
	payment = Payments(payments_id)
	payment.setStatus('sukses')
	view = payment.getData()
	return redirect(url_for('showAdmin'))

@app.route('/order/payment/status', methods = ['GET','POST'])
def status():
	item = request.form.get('items')
	user_id = request.form.get('user_id')
	items = request.form.get('items')
	items = items.replace('[','').replace(']','').split("',")
	harga = request.form.get('budget')
	games_id = ''
	payment_method = request.form.get('payment_method')
	email = ''
	telepon = request.form.get('telepon')
	status = 'Pesanan Sedang Diproses'
	payment = Payments()
	hasil = payment.addPayments(games_id, user_id, harga, payment_method, email, telepon, item, status)
	return render_template('status.html',harga = harga, user_id=user_id, item=item, games_id=games_id, email=email, telepon=telepon, payment_method=payment_method, status=status)

@app.route('/status', methods = ['GET','POST'])
def checkStatus():
	payment = Payments()
	listpay = payment.showAllPayments()
	print(listpay)
	return render_template('cek-status.html',listpay=listpay)

@app.route('/status/info', methods = ['GET','POST'])
def viewStatus():
	user_id = request.form.get('user_id')
	payment = Payments()
	tmp = payment.showAllPayments()
	listpay = []
	for info in tmp:
		if(info['user_id'] == user_id):
			listpay.append(info)
	print(listpay)
	return render_template('info.html',listpay=listpay)