from flask import (
    render_template,
    request)
from app.helpers import BaseView
from .models import (
    Alamat, AlamatForm)


class AlamatView(BaseView):
    def dispatch_request(self):
        page = request.args.get('page', type=int, default=1)
        search = request.args.get('search', type=str, default='')
        alamats = Alamat.get_all(search=search, page=page)

        return render_template(
            self.template_name,
            data=alamats.items,
            search=search
        )


class AddAlamatView(BaseView):
    def dispatch_request(self):
        form = AlamatForm(request.form)

        if request.method == 'GET':
            form.init_choices()
            return render_template(
                self.template_name,
                form=form,
                kab_id=1
            )
