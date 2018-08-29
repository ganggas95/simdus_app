from flask import (
    render_template,
    redirect,
    url_for,
    request)
from app.helpers import BaseView
from .models import Keluarga


class KeluargaView(BaseView):
    def dispatch_request(self):
        search = request.args.get('search', default='', type=str)
        page = request.args.get('page', default=1, type=int)
        keluarga = Keluarga.get_all(page, search)
        return render_template(
            self.template_name,
            data=keluarga.items,
            search=search)
