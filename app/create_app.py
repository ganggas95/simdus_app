from flask import Flask
from app.extensions import (
    db, csrf, login_manager, migrate, ma)
from app.settings import (
    BaseConfig,
    UploadPathConfig)


app = Flask(__name__)

app.config.from_object(BaseConfig)
app.config.from_object(UploadPathConfig)
app.config.from_pyfile('settings.conf')

db.init_app(app)
csrf.init_app(app)
login_manager.init_app(app)
migrate.init_app(app, db=db)
ma.init_app(app)
