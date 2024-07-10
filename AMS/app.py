from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the MaintenanceRequest model
class MaintenanceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20), nullable=False)
    asset_id = db.Column(db.String(100), nullable=False)
    comments = db.Column(db.Text, nullable=False)

# Create the database and tables
@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('maintenance.html')

@app.route('/submit', methods=['POST'])
def submit():
    category = request.form['category']
    asset_id = request.form['id']
    comments = request.form['comments']
    
    # Save the data to the database
    maintenance_request = MaintenanceRequest(category=category, asset_id=asset_id, comments=comments)
    db.session.add(maintenance_request)
    db.session.commit()
    
    return 'Form submitted successfully!'

@app.route('/maintenance-requests')
def maintenance_requests():
    # Fetch all records from the database
    requests = MaintenanceRequest.query.all()
    return render_template('maintenance_requests.html', requests=requests)

if __name__ == '__main__':
    app.run(debug=True)
