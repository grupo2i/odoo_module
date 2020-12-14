# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models
class Club(models.Model):
    _name='music_events.club'
    _inherit='res.users'
    
    location=fields.Char()
    phoneNumber=fields.Char()
    
    events=fields.One2many('music_events.event', 'club', ondelete='cascade')
    