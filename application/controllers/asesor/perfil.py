# -*- coding:utf-8 -*-
import web
import config as config
"""
    Clase para mostrar cada campo a detalle de los registros en el index
"""
class Perfil():
    def __init__(self):
        pass
    
    def GET(self,id_as):
        asesor = config.model_asesor.select_id_as(id_as) # Selecciona el registro que coincida con el nombre
        return config.render.perfil_asesor(asesor) # Envia el registro y renderiza el view.html
        
