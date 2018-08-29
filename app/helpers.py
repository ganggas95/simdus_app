from flask import (
    jsonify,
    make_response,
    views)


class BaseView(views.View):
    def __init__(self, template_name):
        self.template_name = template_name


class MethodView(views.MethodView):
    def __init__(self, template_name):
        self.template_name = template_name


def custome_response(data=None, status=200, paginate=None, message=""):
    res_data = jsonify({
        "data": data,
        "msg": message,
        "meta": paginate
    })
    return make_response(res_data, status)
