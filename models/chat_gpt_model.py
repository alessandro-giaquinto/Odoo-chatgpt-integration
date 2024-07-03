from odoo import models, fields 

class ChatGptModel(models.model):
    _name = 'chat_gpt_model'
    _description = 'ChatGPT data'

    name = fields.Char(required=True)