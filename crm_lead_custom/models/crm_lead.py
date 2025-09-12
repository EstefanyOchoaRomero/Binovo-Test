from odoo import fields, models,  api


class CrmLead(models.Model):
    _inherit = "crm.lead"

    source_type = fields.Selection(
        [
            ("third_party", "Third Party"),
            ("social_media", "Social Media"),
            ("internet", "Internet Search"),
        ],
        string="Source Type",
        required=True,
    )

    @api.model
    def create_from_website(self, vals):
        if not vals.get('name'):
            vals['name'] = "Not name"
        return super(CrmLead, self).create(vals)
