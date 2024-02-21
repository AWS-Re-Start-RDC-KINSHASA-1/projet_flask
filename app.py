from flask import Flask, render_template, request, redirect, url_for
import socket

app = Flask(__name__)

# Cette liste contient des paires username:password. À des fins de démonstration uniquement, ne stockez jamais les mots de passe en clair comme ceci dans une application réelle.
users = {'ezer': '12345', 'jane': 'doe'}

@app.route('/')
def home():
    # Mettre en pause pendant 3 secondes (à des fins de démonstration)
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('success'))
        else:
            return render_template('login.html', error='Mauvais nom d\'utilisateur ou mot de passe')
    return render_template('login.html')

@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

