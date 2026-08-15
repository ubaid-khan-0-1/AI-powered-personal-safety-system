from flask import Flask, render_template, request, jsonify, session, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'women_safety_secret_2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///women_safety.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'static', 'recordings')

db = SQLAlchemy(app)

# ─────────────────────────────────────────
# DATABASE MODELS
# ─────────────────────────────────────────

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    contacts = db.relationship('EmergencyContact', backref='user', lazy=True, cascade='all, delete-orphan')
    alerts = db.relationship('AlertHistory', backref='user', lazy=True, cascade='all, delete-orphan')

class EmergencyContact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    relationship = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    is_primary = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class AlertHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    alert_type = db.Column(db.String(50), nullable=False)
    alert_message = db.Column(db.Text, nullable=False)
    location_lat = db.Column(db.Float, nullable=True)
    location_lng = db.Column(db.Float, nullable=True)
    location_link = db.Column(db.String(300), nullable=True)
    contact_name = db.Column(db.String(100), nullable=True)
    contact_phone = db.Column(db.String(20), nullable=True)
    audio_file = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(50), default='Delivered Successfully')
    triggered_by = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# ─────────────────────────────────────────
# AUTH ROUTES
# ─────────────────────────────────────────

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name', '').strip()
        email = data.get('email', '').strip().lower()
        phone = data.get('phone', '').strip()
        password = data.get('password', '')
        if not all([name, email, phone, password]):
            return jsonify({'success': False, 'message': 'All fields are required.'})
        if User.query.filter_by(email=email).first():
            return jsonify({'success': False, 'message': 'Email already registered.'})
        user = User(name=name, email=email, phone=phone,
                    password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Registration successful!'})
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email', '').strip().lower()
        password = data.get('password', '')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            return jsonify({'success': True})
        return jsonify({'success': False, 'message': 'Invalid email or password.'})
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    return render_template('dashboard.html', user=user)




# ─────────────────────────────────────────
# INIT DB
# ─────────────────────────────────────────

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=5000)