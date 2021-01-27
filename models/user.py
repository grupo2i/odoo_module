# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api
class User(models.Model):
    _name='res.users'
    _inherit='res.users'

    biography= fields.Text()
    # Selection fieds are given as a pair like (value, label).
    userPrivilege= fields.Selection([ ('ADMIN', 'admin'),('CLIENT', 'client'),('CLUB', 'club'),('ARTIST', 'artist')])
    lastAccess= fields.Datetime()
    lastPasswordChange= fields.Datetime()
    
    # Some fields have been replace by existing one in the res.users model:
    # Our data model ---> res.users
    # fullName ---> name
    # userStatus ---> active
    # login ---> login
    # email ---> email
    # profileImage ---> image
