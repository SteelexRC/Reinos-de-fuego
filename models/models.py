from odoo import models, fields

class Jugador(models.Model):
    _name = 'reinosdefuego.jugador'
    _description = 'Jugador'

    name = fields.Char(string="Nombre del Jugador", required=True)
    nivel = fields.Integer(string="Nivel", default=1)
    dragones = fields.One2many('reinosdefuego.dragon', 'propietario_id', string="Dragones")

class Dragon(models.Model):
    _name = 'reinosdefuego.dragon'
    _description = 'Dragón'

    nombre = fields.Char(string="Nombre del Dragón", required=True)
    nivel = fields.Integer(string="Nivel", default=1)
    salud = fields.Float(string="Salud", default=100.0)
    ataque = fields.Float(string="Poder de Ataque", default=10.0)
    defensa = fields.Float(string="Defensa", default=5.0)
    propietario_id = fields.Many2one('reinosdefuego.jugador', string="Propietario")

class Objeto(models.Model):
    _name = 'reinosdefuego.objeto'
    _description = 'Objeto'

    nombre = fields.Char(string="Nombre del Objeto", required=True)
    tipo_efecto = fields.Selection([('curar', 'Curar'), ('mejorar', 'Mejorar')], string="Tipo de Efecto")
    valor_efecto = fields.Float(string="Valor del Efecto")

class Equipamiento(models.Model):
    _name = 'reinosdefuego.equipamiento'
    _description = 'Equipamiento'

    nombre = fields.Char(string="Nombre del Equipamiento", required=True)
    tipo_equip = fields.Selection([('armadura', 'Armadura'), ('arma', 'Arma')], string="Tipo")
    bonus_ataque = fields.Float(string="Bono de Ataque", default=0.0)
    bonus_defensa = fields.Float(string="Bono de Defensa", default=0.0)
    dragon_id = fields.Many2one('reinosdefuego.dragon', string="Equipado Por")

