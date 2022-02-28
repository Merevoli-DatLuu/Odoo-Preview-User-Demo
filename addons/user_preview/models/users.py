from odoo import models, _


class User(models.Model):
    _inherit = 'res.users'

    def preview_user_page(self):
        return {
            "type": "ir.actions.act_url",
            "url": "/user_preview/%s" % self.id,
            "target": "self",
        }

