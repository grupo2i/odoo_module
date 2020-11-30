# -*- coding: utf-8 -*-
from odoo import http

# class MusicEvents(http.Controller):
#     @http.route('/music_events/music_events/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/music_events/music_events/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('music_events.listing', {
#             'root': '/music_events/music_events',
#             'objects': http.request.env['music_events.music_events'].search([]),
#         })

#     @http.route('/music_events/music_events/objects/<model("music_events.music_events"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('music_events.object', {
#             'object': obj
#         })