from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///certificates.db'
db = SQLAlchemy(app)

class Certification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    certificate_name = db.Column(db.String(80),nullable=False)

@app.route("/")
def index():
    certificates = Certification.query.all()
    
    return render_template('index.html',certificates=certificates)

@app.route("/add")
def add():
    name = Certification(text=request.form['certificate_name'])
    db.session.add(name)
    db.session.commit()
    
    return redirect(url_for('index'))


if __name__ == "__main":
    app.run(debug=True)