# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# Ander Vicente
from odoo import models,fields,api
class Club(models.Model):
    _name='res.users'
    _inherit='res.users'
    
    clubEvents=fields.One2many('music_events.event', 'club', ondelete='cascade')
    