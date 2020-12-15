# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields
class User(models.Model):
    _name='res.users'
    _inherit='res.users'

    fullName= fields.Char()
    biography= fields.Char()
    userStatus= fields.Selection([ ('ENABLED', 'enabled'),('DISABLED', 'disabled')])
    userPrivilege= fields.Selection([ ('ADMIN', 'admin'),('CLIENT', 'client'),('CLUB', 'club'),('ARTIST', 'artist')])
  
    lastAccess= fields.datetime()
    lastPasswordChange= fields.datetime()

    
