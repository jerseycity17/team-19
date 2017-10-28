from flask import Flask, send_from_directory, request, redirect, url_for
from flask import render_template
from flask_login import LoginManager, UserMixin, login_required
import sqlalchemy
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dir_path + '/6degree.db'
#db = sqlalchemy(app)


@app.route('/static/<path:path>')
def send_css(path):
    return send_from_directory('static', path)

# login stuff
login_manager = LoginManager()
login_manager.init_app(app)


# Our mock database.
users = {'foo@bar.tld': {'password': 'secret'}}



@login_manager.user_loader
def load_user(user_id):
	return User.get(user_id)


@app.route("/")
def main():
	return render_template("login.html")


class User(UserMixin):
    
    def get(user_id):
        pass


@login_manager.user_loader
def user_loader(email):
	if email not in users:
		return

	user = User()
	user.id = email
	return user


@login_manager.request_loader
def request_loader(request):
	email = request.form.get('email')
	if email not in users:
		return

	user = User()
	user.id = email

	# DO NOT ever store passwords in plaintext and always compare password
	# hashes using constant-time comparison!
	user.is_authenticated = request.form['password'] == users[email]['password']

	return user


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template("login.html")
			

	email = request.form['email']
	if request.form['password'] == users[email]['password']:
		user = User()
		user.id = email
		flask_login.login_user(user)
		return redirect(url_for('protected'))

	return 'Bad login'

@app.route('/logout')
def logout():
	flask_login.logout_user()
	return 'Logged out'

@login_manager.unauthorized_handler
def unauthorized_handler():
	return 'Unauthorized'


@app.route('/protected')
@login_required
def protected():
	return 'Logged in as: ' + Flask_Login.current_user.id

@app.route('/OrgsSummary')
def OrgsSummarymethod():
    return render_template('OrgsSummary.html')

@app.route('/Drive')
def Drivemethod():
    return render_template('Drive.html')

@app.route('/OrgsDescriptionmethod')
def OrgsDescriptions():
    return render_template('OrgsDescriptions.html')

@app.route('/finalmethod')
def finalmethod():
	return render_template('final.html')
	
if __name__ == "__main__":
		app.run()

