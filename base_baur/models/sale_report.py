# -*- coding: utf-8 -*-

from odoo import models


class SaleReport(models.Model):
    _inherit = "sale.report"

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['execution'] = ", s.execution as execution"
        groupby += ', s.execution'
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
