# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class IrActionsActMulti(models.Model):
    _name = "ir.actions.act_multi"
    _description = "Action Multi"
    _inherit = "ir.actions.actions"
    _table = "ir_actions_act_multi"

    type = fields.Char(default="ir.actions.act_multi")

    def _get_readable_fields(self):
        return super()._get_readable_fields() | {"actions"}
