# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields
class Rating(models.Model):
    _name='music_events.rating'
    
    rating= fields.Integer
    comment= fields.Char()
    
    client= fields.Many2one('music_events.client')
    event= fields.Many2one('music_events.event')
