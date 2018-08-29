from flask import Blueprint
from flask_restplus import Api


alamat_bp = Blueprint(
    'alamat_bp',
    __name__,
    template_folder='templates'
)
api_alamat_bp = Blueprint(
    'api_alamat_bp',
    __name__,
    url_prefix="/api/v0.1/alamat"
)
api_alamat = Api(
    api_alamat_bp,
    "v0.1",
    "API Alamat",
    "API For alamat proccess"
)
