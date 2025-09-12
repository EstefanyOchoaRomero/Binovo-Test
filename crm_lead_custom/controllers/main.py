from odoo import http
from odoo.http import request

class WebsiteCrm(http.Controller):

    @http.route(['/contactus/submit'], type='http', auth='public', website=True)
    def contactus_form(self, **post):
        # Esto es lo que “ignora la validación del frontend”
        vals = {
            'name': post.get('name') or 'Sin Nombre',  # valor por defecto si Name está vacío
            'email_from': post.get('email'),
            'phone': post.get('phone'),  # si quieres mantenerlo, aunque esté oculto
            'source_type': post.get('source_type'),
        }
        request.env['crm.lead'].sudo().create(vals)
        return request.redirect('/contactus?success=1')

