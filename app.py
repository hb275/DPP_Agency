from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, static_folder='./build/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


'''
db = SQLAlchemy(app)
class User(db.Model):
    __tablename__ = 'user'
    
    token_id = db.Column(db.String(255), primary_key=True, unique=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    companyName = db.Column(db.String(255), unique=True
    def __init__(self, token_id, email, companyName, solutionsCompleted, userOnboardingCompleted):
        self.token_id = token_id
        self.email = email
        self.companyName = companyName
'''

@app.route('/', defaults={"filename": "index.html"})
@app.route('/<path:filename>')
def index(filename):
    return send_from_directory('./build', filename)

#Function that sends a full route for POSTing data to your Flask API
'''
@app.route('/api/login', methods=['GET', 'POST'])
@cross_origin()
def login():
    if request.method == 'POST':
        # Returns User object if exists
        requestData = request.get_json()
        token_id = requestData['user']['sub'][6:]
        email = requestData['user']['email']
        
        if token_id and email:
            userExists = User.query.filter_by(token_id=token_id).first()
            if userExists is None:
                # Create new user and store in db
                userExists = User(token_id, email, None, None, None)
                db.session.add(userExists)
                db.session.commit()
            
            return json.jsonify(
                token_id=userExists.token_id,
                email=userExists.email,
                solutionsCompleted=userExists.solutionsCompleted,
                userOnboardingCompleted=userExists.userOnboardingCompleted,
            )
            
    return {'Success': False, 'Response': 'bad request'}
'''

app.run(
    host=os.getenv('IP',"0.0.0.0"),
    port=int(os.getenv("PORT",8081)),
    debug=True,
    )
