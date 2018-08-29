from flask import (
    render_template,
    url_for,
    redirect,
    request)
from flask_login import login_required
from app.helpers import BaseView


class DashboardView(BaseView):

    @login_required
    def dispatch_request(self):
        return render_template(
            self.template_name
        )
