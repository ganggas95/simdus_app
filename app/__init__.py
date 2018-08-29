from app.create_app import app as app_instance
from app.auth_app.urls import auth_bp
from app.dashboard_app.urls import dashboard_bp
from app.alamat_app.urls import alamat_bp, api_alamat_bp
from app.keluarga_app.urls import kk_bp
import app.loader


app_instance.register_blueprint(auth_bp)
app_instance.register_blueprint(dashboard_bp)
app_instance.register_blueprint(alamat_bp)
app_instance.register_blueprint(kk_bp)
app_instance.register_blueprint(api_alamat_bp)

