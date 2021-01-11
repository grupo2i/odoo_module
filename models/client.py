# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api
class Client(models.Model):
    _name='res.users'
    _inherit='res.users'
    
    clientEvents=fields.Many2many('music_events.event')
    ratings=fields.One2many('music_events.rating', 'client')
