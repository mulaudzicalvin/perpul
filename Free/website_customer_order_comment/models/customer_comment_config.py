# -*- coding: utf-8 -*-
# Part of AppJetty. See LICENSE file for full copyright and licensing details.

from flectra import fields, models


class website(models.Model):

    """Adds the fields for options of the Customer Order Comment."""

    _inherit = 'website'

    is_customer_comment_feature = fields.Boolean(
        string='Do you want to disable customer order comment feature',
        default=False)


class ResConfigSettings(models.TransientModel):

    """Settings for the Customer Order Comment."""

    _inherit = 'res.config.settings'

    is_customer_comment_feature = fields.Boolean(
        related='website_id.is_customer_comment_feature',
        string="Do you want to disable customer order comment feature")