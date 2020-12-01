from app import app
from flask import render_template
from app.models.games import Games
from app.models.payments import Payments ## import kelas Project dari model
from flask import request, redirect, url_for, render_template
from datetime import datetime
import locale
import random
import os

@app.route('/order/payment', methods = ['POST', 'GET'])
def payment():
	item = request.form.get('budget')
	user_id = request.form.get('user_id')
	items = request.form.get('items')
	items = items.replace('[','').replace(']','').split("',")
	harga = 0
	games_id = request.form.get('games_id')
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
	print(listpay)
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

@app.route('/Admin1/<payments_id>/Manage/failed', methods = ['GET','POST'])
def failedPayment(payments_id):
	payment = Payments(payments_id)
	payment.setStatus('pembayaran gagal')
	view = payment.getData()
	return redirect(url_for('showAdmin'))

@app.route('/Admin1/<payments_id>/Manage/delete', methods = ['GET','POST'])
def deletePayment(payments_id):
	payment = Payments(payments_id)
	payment.deletePayments()
	view = payment.getData()
	return redirect(url_for('showAdmin'))

@app.route('/order/payment/<payments_id>/upload', methods = ['GET','POST'])
def uploadPayment(payments_id):
	payment = Payments(payments_id)
	# item = request.form.get('items')
	# user_id = request.form.get('user_id')
	# items = request.form.get('items')
	# items = items.replace('[','').replace(']','').split("',")
	# harga = request.form.get('budget')
	# games_id = request.form.get('games_id')
	# payment_method = request.form.get('payment_method')
	# email = random.randint(100000,999999)
	# telepon = request.form.get('telepon')
	# status = 'belum dibayar'
	image = request.files['image']
	imagename = request.form['image-name']
	imagepath = 'uploads/'+ imagename
	imagepath_fix = os.path.join(app.root_path, 'static/'+imagepath)
	image.save(imagepath_fix)
	payment = Payments(payments_id)
	payment.setImg(imagepath)
	return render_template('status.html')
	# hasil = payment.addPayments(games_id, user_id, harga, payment_method, email, telepon, item, status)
	# return render_template('status.html',harga = harga, user_id=user_id, item=item, games_id=games_id, email=email, telepon=telepon, payment_method=payment_method, status=status)

@app.route('/order/payment/status', methods = ['GET','POST'])
def status():
	item = request.form.get('items')
	user_id = request.form.get('user_id')
	items = request.form.get('items')
	items = items.replace('[','').replace(']','').split("',")
	harga = request.form.get('budget')
	harga = random.randint(int(harga)-500, int(harga))
	harga = str(harga)
	games_id = request.form.get('games_id')
	payment_method = request.form.get('payment_method')
	email = random.randint(100000,999999)
	telepon = request.form.get('telepon')
	status = 'pembayaran sedang di proses'
	payment = Payments()
	hasil = payment.addPayments(games_id, user_id, harga, payment_method, email, telepon, item, status)
	return render_template('status.html',harga = harga, user_id=user_id, item=item, games_id=games_id, email=email, telepon=telepon, payment_method=payment_method, status=status, payments_id=hasil.inserted_id)

@app.route('/status', methods = ['GET','POST'])
def checkStatus():
	payment = Payments()
	listpay = payment.showAllPayments()
	return render_template('cek-status.html',listpay=listpay)

@app.route('/status/info', methods = ['GET','POST'])
def viewStatus():
	email = request.form.get('email')
	payment = Payments()
	tmp = payment.showAllPayments()
	listpay = []
	for info in tmp:
		if(str(info['email']) == email):
			listpay.append(info)
	return render_template('info.html',listpay=listpay)