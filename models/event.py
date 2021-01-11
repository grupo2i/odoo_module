# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api
class Event(models.Model):
    _name = 'music_events.event'
    
    name= fields.Char(required=True)
    date= fields.Date(required=True)
    place= fields.Char(required=True)
    ticketPrice= fields.Float(required=True)
    description= fields.Text(required=True)
    
    club= fields.Many2one('res.users')
    artists= fields.Many2many('res.users')
    clients= fields.Many2many('res.users')
    ratings= fields.One2many('music_events.rating', 'event')