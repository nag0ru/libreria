# -*- coding: utf-8 -*-

from odoo import models, fields, api


class libreria_libro(models.Model):
    _name = 'libreria.libro'
    _description = 'libreria.libro'

    name = fields.Char(string="Título", required= True, help="Introduzca el título")
    autor= fields.Char(string="Autor", required= True, help="Introduzca el Autor")
    precio = fields.Float(string="Precio")
    ejemplares = fields.Integer(string="Número de ejemplares", required= True)
    fecha = fields.Integer(string="Fecha de publicación", required= True)
    estado = fields.Selection([('0','Bueno'), ('1', 'Regular'), ('2', 'Defectuoso')], string ="Estado del libro", default='0')
    valor=fields.Float(string="Valor de stock", compute="_importetotal", store=True)
    categoria_id=fields.Many2one("libreria.categoria", required=True)
    
    #FUNCION que multiplica el precio por los ejemplares
    @api.depends('precio', 'ejemplares')
    def _importetotal(self):
        for r in self:
            r.valor = r.ejemplares * r.precio
    
class libreria_categoria(models.Model):
    _name = 'libreria.categoria'
    _description = 'libreria.categoria'

    name = fields.Char(string="Categoría", required=True, help="Introduce una Categoría")
    descripcion = fields.Char(string="Descripción de la categoría", required=False)
    libro_id=fields.One2many("libreria.libro", "categoria_id")
    
    
    

    
    


#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
