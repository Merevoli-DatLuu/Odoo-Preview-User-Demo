from odoo import http
from odoo.http import request


class UserPreviewController(http.Controller):

    @http.route('/user_preview/<model("res.users"):user>', auth='user')
    def preview_user(self, user, **kwargs):
        current_user = request.env.user
        has_permission = current_user.sudo().user_has_groups('user_preview.group_previewable_user')
        
        if not has_permission:
            return request.env['ir.http']._response_by_status(403, None, None)
        
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        image_url_1920 = base_url + '/web/image?' + 'model=res.users&id=' + str(user.id) + '&field=image_128'

        return http.request.render('user_preview.user_preview_template', {
            'user': user,
            'image_url': image_url_1920,
        })