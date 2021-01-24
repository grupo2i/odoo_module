# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api
class Rating(models.Model):
    _name='music_events.rating'
    
    rating= fields.Integer(required=True)
    comment= fields.Char()
    
    client= fields.Many2one('res.users', domain=[('userPrivilege', '=', 'CLIENT')])
    event= fields.Many2one('music_events.event')
    
    
    from odoo.exceptions import ValidationError
    @api.constrains('rating')
    def _check_rating_range(self):
        for r in self:
            if r.rating > 5 or r.rating < 1:
                raise exceptions.ValidationError(_("Rating must be a value betwen 1 and 5."))
