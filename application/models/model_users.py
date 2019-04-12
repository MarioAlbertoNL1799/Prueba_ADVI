import web
import config as config

db = config.db


def get_all_users():
    try:
        return db.select('users')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_users(user):
    try:
        return db.select('users', where='user=$user', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_users(user):
    try:
        return db.delete('users', where='user=$user', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_users(nombre,carrera,grado,tipo,user):
    try:
        return db.insert('users',nombre=nombre,
carrera=carrera,
grado=grado,
tipo=tipo,
user=user)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_users(user,nombre,carrera,grado,tipo):
    try:
        return db.update('users',user=user,
nombre=nombre,
carrera=carrera,
grado=grado,
tipo=tipo,
                  where='user=$user',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
