# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models
class Client(models.Model):
    _name='music_events.client'
    _inherit='res.users'
    
    events=fields.Many2many('music_events.event')
    ratings=fields.One2many('music_events.rating', 'client')
