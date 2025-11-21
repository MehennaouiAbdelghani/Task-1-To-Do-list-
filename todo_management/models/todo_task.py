# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


STATUS_SELECTION = [
('new', 'New'),
('in_progress', 'In Progress'),
('done', 'Completed'),
]


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-Do Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Task Name', required=True, tracking=True)
    user_id = fields.Many2one('res.users', string='Assign To', index=True, tracking=True,
    default=lambda self: self.env.user)
    description = fields.Text(string='Description')
    date_deadline = fields.Datetime(string='Due Date', index=True)
    state = fields.Selection(STATUS_SELECTION, string='Status', default='new', tracking=True)
    date_create = fields.Datetime(string='Created On', readonly=True, default=lambda self: fields.Datetime.now())



    @api.constrains('date_deadline')
    def _check_deadline(self):
        for rec in self:
            if rec.date_deadline and rec.date_create and rec.date_deadline < rec.date_create:
                raise ValidationError(_('Due date cannot be set before creation date.'))


    def action_set_in_progress(self):
        for rec in self:
            rec.state = 'in_progress'


    def action_set_done(self):
        for rec in self:
            rec.state = 'done'


    def action_reset(self):
        for rec in self:
            rec.state = 'new'