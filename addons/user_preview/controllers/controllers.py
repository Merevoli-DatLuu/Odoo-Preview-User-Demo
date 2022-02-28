from odoo import http
from odoo.http import request


class UserPreviewController(http.Controller):

    @http.route('/user_preview/<model("res.users"):user>', auth='public')
    def preview_user(self, user, **kwargs):
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        image_url_1920 = base_url + '/web/image?' + 'model=res.users&id=' + str(user.id) + '&field=image_128'

        return http.request.render('user_preview.user_preview_template', {
            'user': user,
            'image_url': image_url_1920,
        })