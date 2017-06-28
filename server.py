from flask import Flask, session, redirect, render_template, request
from mysqlconnection import MySQLConnection

app = Flask(__name__)
app.secret_key = open('secret-key.txt', 'r').read().strip()

db = MySQLConnection(app, 'friendsdb')

@app.route('/')
def index():
	fields = ['id', 'first_name', 'last_name', 'email']
	query = 'select {} from friends'.format(','.join(fields))
	friends = db.query_db(query)

	friends = [tuple(rec[nm] for nm in fields) for rec in friends]
	# print (friends)
	return render_template('index.html', friends=friends)

@app.route('/add', methods=['POST'])
def add_user():
	
	data = {
		'fn': request.form['first_name'],
		'ln': request.form['last_name'],
		'em': request.form['email']
	}

	query = 'insert into friends(first_name, last_name, email) values(:fn, :ln, :em)'
	result = db.query_db(query, data)
	# print(result)

	return redirect('/')

@app.route('/update', methods=['POST'])
def update():
	params = {
		'id': request.form['id'],
		'first_name': request.form['first_name'],
		'last_name': request.form['last_name'],
		'email': request.form['email']
	}
	query = ('update friends set first_name = :first_name,'
		'last_name = :last_name,'
		'email = :email '
		'where id=:id'
		)
	db.query_db(query, params)
	return redirect('/')

@app.route('/edit/<user_id>', methods=['POST'])
def edit_user(user_id):
	query = 'select id, first_name, last_name, email \
		from friends where id = :id'

	user = db.query_db(query, {'id': user_id})[0]

	return render_template('edit.html', **user)


@app.route('/delete/<user_id>', methods=['POST'])
def delete_user(user_id):
	params = {
		'id': user_id
	}
	query = 'delete from friends where id = :id'
	
	db.query_db(query, params)

	return redirect('/')


app.run(debug=True)