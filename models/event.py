# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# Martin Angulo
from odoo import models,fields,api
from odoo.exceptions import ValidationError
from datetime import datetime

class Event(models.Model):
    _name = 'music_events.event'
    
    name= fields.Char(required=True)
    date= fields.Date(required=True)
    place= fields.Char(required=True)
    ticketPrice= fields.Float(required=True)
    description= fields.Text(required=True)
    
    club= fields.Many2one('res.users', domain=[('userPrivilege', '=', 'CLUB')],
                    default=lambda self: self.env.user)
    artists= fields.Many2many('res.users', domain=[('userPrivilege', '=', 'ARTIST')])
    clients= fields.Many2many('res.users', domain=[('userPrivilege', '=', 'CLIENT')])
    ratings= fields.One2many('music_events.rating', 'event')
    
    @api.constrains('ticketPrice')
    def _check_ticket_price_not_negative(self):
        for r in self:
            if r.ticketPrice < 0:
                raise ValidationError("Ticket price must be a positive number.")
            
    @api.constrains('date')
    def _check_date_not_before(self):
        if datetime.strptime(self.date, "%Y-%m-%d") < datetime.today():
            raise ValidationError("Event date must be after current date.")
        
    @api.onchange('name')
    def _on_change_name(self):
        if(self.name):
            for i, c in enumerate(self.name):
                if i == 0:
                    if not c.isalpha():
                        return { 'warning': {'title': "Warning", 'message': "Event name must start with a letter"},}