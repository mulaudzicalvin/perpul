# -*- coding: utf-8 -*-
from flectra import fields, models, api, _

class paymentTerm(models.Model):
    _inherit = 'account.payment.term'

    dte_sii_code = fields.Selection((
        ('1', '1: Contado'),
        ('2', '2: Credito'),
        ('3', '3: Otro')), 'DTE Sii Code', )
