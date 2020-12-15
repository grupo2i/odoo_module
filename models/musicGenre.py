# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields
class MusicGenre(models.Model):
    _name='music_events.musicGenre'
    
    musicGenre= fields.Selection([('POP','pop'),('ROCK', 'rock'),
    ('REAGGAE', 'reaggae'),('EDM', 'edm'),('TRAP', 'trap'),('RAP', 'rap'),
    ('INDIE', 'indie'),('REGGAETON', 'reggaeton'),('OTHER', 'other')])
    
    artist= fields.One2Many('music_events.artist','musicGenre')