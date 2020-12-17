# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api
class Event(models.Model):
    _name = 'music_events.event'
    
    date= fields.Date(required=True)
    place= fields.Char(required=True)
    ticketPrice= fields.Float(required=True)
    description= fields.Char(required=True)
    
    club= fields.Many2one('music_events.club')
    artist= fields.Many2many('music_events.artist')
    client= fields.Many2many('music_events.client')
    ratings= fields.One2many('music_events.rating', 'event')