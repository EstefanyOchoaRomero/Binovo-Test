from odoo import api, fields, models


class Blog(models.Model):
    _inherit = "blog.blog"

    company_id = fields.Many2one(
        "res.company",
        string="Company",
        required=True,
        default=lambda self: self.env.company,
    )


class BlogPost(models.Model):
    _inherit = "blog.post"

    company_id = fields.Many2one(
        "res.company",
        string="Company",
        related="blog_id.company_id",
        store=True,
        readonly=True,
    )

