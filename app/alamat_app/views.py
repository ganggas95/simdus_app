from flask import (
    render_template,
    redirect,
    url_for,
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
        if form.validate_on_submit:
            alamat = Alamat()
            alamat.id_dusun = form.dusun.data
            alamat.rt_rw = form.rt_rw.data
            alamat.kode_pos = form.kode_pos.data
            alamat.save()
            return redirect(
                url_for('alamat_bp.alamat_view')
            )


class EditAlamatView(BaseView):
    def dispatch_request(self, id_alamat):
        form = AlamatForm(request.form)
        alamat = Alamat.get_by_id(id_alamat)
        if request.method == 'GET':
            form.init_choices()
            if alamat:
                form.default_data(alamat)
            return render_template(
                self.template_name,
                form=form,
                kab_id=1
            )
        if form.validate_on_submit:
            
            alamat.id_dusun = form.dusun.data
            alamat.rt_rw = form.rt_rw.data
            alamat.kode_pos = form.kode_pos.data
            alamat.save()
            return redirect(
                url_for('alamat_bp.alamat_view')
            )
