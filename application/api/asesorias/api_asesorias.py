import web
import config as config
import json


class Api_asesorias:
    def get(self, num_as):
        try:
            # http://0.0.0.0:8080/api_asesorias?user_hash=12345&action=get
            if num_as is None:
                result = config.model.select_asesoria()
                asesorias_json = []
                for row in result:
                    tmp = dict(row)
                    asesorias_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(asesorias_json)
            else:
                # http://0.0.0.0:8080/api_asesorias?user_hash=12345&action=get&num_as=1
                result = config.model.num_as(int(num_as))
                asesorias_json = []
                asesorias_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(asesorias_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            asesorias_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(asesorias_json)

    def get_asesor(self, asesor):
        try:
            # http://0.0.0.0:8080/api_asesorias?user_hash=12345&action=get
            if asesor is None:
                result = config.model.select_asesoria()
                asesorias_json = []
                for row in result:
                    tmp = dict(row)
                    asesorias_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(asesorias_json)
            else:
                # http://0.0.0.0:8080/api_asesorias?user_hash=12345&action=get&num_as=1
                result = config.model.get_asesor(asesor)
                asesorias_json = []
                asesorias_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(asesorias_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            asesorias_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(asesorias_json)

    def get_solicitante(self, solicitante):
        try:
            # http://0.0.0.0:8080/api_asesorias?user_hash=12345&action=get
            if solicitante is None:
                result = config.model.select_asesoria()
                asesorias_json = []
                for row in result:
                    tmp = dict(row)
                    asesorias_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(asesorias_json)
            else:
                # http://0.0.0.0:8080/api_asesorias?user_hash=12345&action=get&num_as=1
                result = config.model.get_solicitante(solicitante)
                asesorias_json = []
                asesorias_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(asesorias_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            asesorias_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(asesorias_json)

# http://0.0.0.0:8080/api_asesorias?user_hash=12345&action=put&num_as=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, dia,hora,estado,solicitante,asesor,tema):
        try:
            config.model.insert_asesorias(dia,hora,estado,solicitante,asesor,tema)
            asesorias_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(asesorias_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_asesorias?user_hash=12345&action=delete&num_as=1
    def delete(self, num_as):
        try:
            config.model.delete_asesorias(num_as)
            asesorias_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(asesorias_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_asesorias?user_hash=12345&action=update&num_as=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, num_as, dia,hora,estado,solicitante,asesor,tema):
        try:
            config.model.edit_asesorias(num_as,dia,hora,estado,solicitante,asesor,tema)
            asesorias_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(asesorias_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            asesorias_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(asesorias_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            num_as=None,
            dia=None,
            hora=None,
            estado=None,
            solicitante=None,
            asesor=None,
            tema=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            num_as=user_data.num_as
            dia=user_data.dia
            hora=user_data.hora
            estado=user_data.estado
            solicitante=user_data.solicitante
            asesor=user_data.asesor
            tema=user_data.tema
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(num_as)
                elif action == 'get_asesor':
                    return self.get_asesor(asesor)
                elif action == 'get_solicitante':
                    return self.get_solicitante(solicitante)
                elif action == 'put':
                    return self.put(dia,hora,estado,solicitante,asesor,tema)
                elif action == 'delete':
                    return self.delete(num_as)
                elif action == 'update':
                    return self.update(num_as, dia,hora,estado,solicitante,asesor,tema)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
