from flask import Flask, request, render_template, url_for
from send_mail import send_mail

app = Flask(__name__)
app.secret_key = 'secretkey'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success',methods=['GET', 'POST'] )
def success():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        send_mail(name=name, email=email, message=message)
    return render_template('success.html', name=name, email=email)

@app.route('/project01')
def project01():
    return render_template('project01.html')

@app.route('/project02')
def project02():
    return render_template('project02.html')

@app.route('/project03')
def project03():
    return render_template('project03.html')

@app.route('/project04')
def project04():
    return render_template('project04.html')

@app.route('/project05')
def project05():
    return render_template('project05.html')

if __name__=='__main__':
    app.run()
