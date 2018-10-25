from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

#form homepage
@app.route("/")
def index():
    return render_template('user_validation.html')

#input validation requested
@app.route('/validate-user', methods=['POST'])
def validate_user():
#variable names assigned to user input from form fields
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
#errors are given variable names and assigned an empty string as placeholders
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    validation = True
#validation and error assignment for validation failures
    if not username or len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = 'That is not a valid username. Username must be 3-20 characters in length'
        username = ''
        validation = False
    
    if not password or len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = 'That is not a valid password.  Username must be 3-20 characters in length'
        password = ''
        validation = False

    if not verify or password != verify:
        verify_error = 'The passswords you entered do not match.'
        verify = ''
        validation = False

    if len(email) < 3 and len(email) > 0 or len(email) > 20 or len(email) > 0 and '@' not in email or len(email) > 0 and "." not in email or ' ' in email:
        email_error = 'The email you entered is invalid.'
        email = ''
        validation = False
	
    if validation is False:
        return render_template('user_validation.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=username, password=password, email=email)

    else:
        return render_template('/validated_user.html', username=username)


if __name__ == '__main__':	
    app.run(debug=True)