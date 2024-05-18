from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return '<Contact %r>' % self.id


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        phone = request.form['phone']
        email = request.form['email']
        contact = Contact(last_name=last_name, first_name=first_name, phone=phone, email=email)
        try:
            db.session.add(contact)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f'Failed to add contact with error: {e}')
    else:
        contacts = Contact.query.order_by(Contact.last_name).all()
        return render_template('index.html', contacts=contacts)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    contact_to_update = Contact.query.get_or_404(id)
    if request.method == 'POST':
        contact_to_update.last_name = request.form['last_name']
        contact_to_update.first_name = request.form['first_name']
        contact_to_update.phone = request.form['phone']
        contact_to_update.email = request.form['email']
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f'Failed to update contact with error: {e}')
    else:
        return render_template('update.html', contact=contact_to_update)

@app.route('/delete/<int:id>')
def delete(id):
    contact_to_delete = Contact.query.get_or_404(id)
    try:
        db.session.delete(contact_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        print(f'Failed to delete contact with error: {e}')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
