import web
import config

db = config.db


def get_all_asesor():
    try:
        return db.select('asesor')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_asesor(id_as):
    try:
        return db.select('asesor', where='id_as=$id_as', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_asesor(id_as):
    try:
        return db.delete('asesor', where='id_as=$id_as', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_asesor(correo,horario,habilidades,validado):
    try:
        return db.insert('asesor',correo=correo,
horario=horario,
habilidades=habilidades,
validado=validado)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_asesor(id_as,correo,horario,habilidades,validado):
    try:
        return db.update('asesor',id_as=id_as,
correo=correo,
horario=horario,
habilidades=habilidades,
validado=validado,
                  where='id_as=$id_as',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
