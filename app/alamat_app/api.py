from flask import request
from flask_restplus import Namespace, Resource
from .models import (
    Kec,
    KecSchema,
    Desa,
    DesaSchema,
    Dusun,
    DusunSchema)
from app.helpers import custome_response


alamat_ns = Namespace("")

kec_schs = KecSchema(many=True)
desa_schs = DesaSchema(many=True)
dusun_schs = DusunSchema(many=True)

@alamat_ns.route("/kecamatan/<int:kab_id>/data")
class KecamatanResource(Resource):
    def get(self, kab_id):
        search = request.args.get('search', type=str, default='')
        kec = Kec.get_by_kab(kab_id, search=search)
        res = kec_schs.dump(kec).data
        return custome_response(
            data=res,
            status=200,
            paginate=None,
            message="Data Retrived successfully")


@alamat_ns.route("/desa/<int:kec_id>/data")
class DesaResource(Resource):
    def get(self, kec_id):
        search = request.args.get('search', type=str, default='')
        desa = Desa.get_by_kec(kec_id, search=search)
        res = desa_schs.dump(desa).data
        return custome_response(
            data=res,
            status=200,
            paginate=None,
            message="Data Retrived successfully")


@alamat_ns.route("/dusun/<int:desa_id>/data")
class DusunResource(Resource):
    def get(self, desa_id):
        search = request.args.get('search', type=str, default='')
        dusun = Dusun.get_by_desa(desa_id, search=search)
        res = dusun_schs.dump(dusun).data
        return custome_response(
            data=res,
            status=200,
            paginate=None,
            message="Data Retrived successfully")
