import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    _logger.info("Running migrate script for web_ir_actions_act_multi")

    cr.execute(
        """
        INSERT INTO ir_actions_act_multi
        SELECT *
        FROM ir_actions
        WHERE type = 'ir.actions.act_multi'
    """
    )

    cr.execute(
        """
        DELETE FROM ir_actions
        WHERE type = 'ir.actions.act_multi'
    """
    )
