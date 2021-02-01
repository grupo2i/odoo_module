# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# Aitor Fidalgo
from odoo import models,fields,api
from odoo.exceptions import ValidationError
import re

class Rating(models.Model):
    _name='music_events.rating'
    
    rating= fields.Integer(required=True)
    comment= fields.Text()
    
    client= fields.Many2one('res.users', domain=[('userPrivilege', '=', 'CLIENT')],
                    default=lambda self: self.env.user)
    event= fields.Many2one('music_events.event')
                    
    
    @api.constrains('rating')
    def _check_rating_range(self):
        for r in self:
            if r.rating > 5 or r.rating < 1:
                raise ValidationError("Rating must be a value betwen 1 and 5.")
            
    @api.onchange('comment')
    def _check_comment_pattern(self):
        if self.comment:
            match = re.match("^([a-zA-Z]+)+$", self.comment)
            if match == None:
                raise ValidationError("Comment must not contain numbers.")
                return{
                    'warning':{
                        'title': 'Wrong format for comment field',
                        'message': 'Comments must not contain numbers.',
                    }
                }
                
    @api.onchange('event')
    def _default_comment_for_bbklive(self):
        if self.event.name == "BBKLive":
            self.comment = "BBKLive"
            
                
#    @api.constrains('comment')
#    def _check_comment_pattern(self):
#        for r in self:
#            #if len(r.comment) != "^[a-zA-Z]+$":
#            if re.match("^[a-zA-Z]+$", r.comment) == None:
#                raise ValidationError("Comment must not contain numbers.")
