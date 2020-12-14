# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models
class SocialNetwork(Model.models):
    _name='music_events.socialNetwork'
    
    socialNetwork=fields.Char()
    
    artists=fields.Many2one('music_events.artist')
