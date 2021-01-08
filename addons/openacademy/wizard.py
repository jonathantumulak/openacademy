
from odoo import models, fields, api, exceptions

class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'
    _description = "Wizard: Quick Registration of Attendees to Sessions"

    def _default_sessions(self):
        return self.env['openacademy.session'].browse(self._context.get('active_ids'))

    def _default_attendees(self):
        return self.env['openacademy.session'].browse(self._context.get('attendee_ids'))

    session_ids = fields.Many2many(
        'openacademy.session',
        string="Sessions",
        required=True,
        default=_default_sessions,
    )
    attendee_ids = fields.Many2many(
        'res.partner',
        string="Attendees",
        default=_default_attendees,
    )

    def subscribe(self):
        for session in self.session_ids:
            if session.is_open:
                session.attendee_ids |= self.attendee_ids
            else:
                raise exceptions.ValidationError(f"Session ({session.name}) is no longer open.")

        return {}
