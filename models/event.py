# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api
from odoo.exceptions import ValidationError

class Event(models.Model):
    _name = 'music_events.event'
    
    name= fields.Char(required=True)
    date= fields.Date(required=True)
    place= fields.Char(required=True)
    ticketPrice= fields.Float(required=True)
    description= fields.Text(required=True)
    
    club= fields.Many2one('res.users', domain=[('userPrivilege', '=', 'CLUB')])
    artists= fields.Many2many('res.users', domain=[('userPrivilege', '=', 'ARTIST')])
    clients= fields.Many2many('res.users', domain=[('userPrivilege', '=', 'ADMIN')])
    ratings= fields.One2many('music_events.rating', 'event')
    
    
    @api.constrains('ticketPrice')
    def _check_ticket_price_not_negative(self):
        for r in self:
            if r.ticketPrice < 0:
                raise ValidationError("Ticket price must be a positive number.")
            