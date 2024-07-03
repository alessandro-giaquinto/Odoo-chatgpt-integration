from odoo import models, fields 

class CustomModel(models.model):
    _name = 'custom.model'
    _description = 'custom model of odoo chatGpt integration module'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')