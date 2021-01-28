# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# Matteo Fernandez
from odoo import models,fields,api
class Artist(models.Model):
    _name='res.users'
    _inherit='res.users'
    
    musicGenre= fields.Selection([('POP','pop'),('ROCK', 'rock'),
    ('REAGGAE', 'reaggae'),('EDM', 'edm'),('TRAP', 'trap'),('RAP', 'rap'),
    ('INDIE', 'indie'),('REGGAETON', 'reggaeton'),('OTHER', 'other')])
    
    artistEvents=fields.Many2many('music_events.event')
    socialNetworks=fields.One2many('music_events.socialnetwork', 'artists')