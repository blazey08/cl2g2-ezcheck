<<<<<<< HEAD
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
import firebase_admin
from firebase_admin import credentials, firestore, storage, db

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

mail = Mail(app)


=======
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
import firebase_admin
from firebase_admin import credentials, firestore, storage, db

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

mail = Mail(app)


>>>>>>> 7051cf6f23955ab084e2c4ceb770357b960ec771
from app import routes, models