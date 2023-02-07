from odoo import api, models, fields, _
from datetime import datetime, timedelta


class mail_message_inherited(models.Model):
    _inherit = 'mail.message'

    note = fields.Html(string='Note')

    @api.model
    def create(self, vals_list):
        rec = super(mail_message_inherited, self).create(vals_list)
        if rec.model == 'project.task':
            if rec.subtype_id.name != 'Discussions':
                self.get_message_note(rec)
            task_id = self.env['project.task'].search([('id', '=', int(rec.res_id))])
            for user in task_id.message_partner_ids:
                if user.id != rec.author_id.id:

                    channel = self.env['mail.channel'].channel_get(
                        [user.id])
                    channel_id = self.env['mail.channel'].browse(channel["id"])
                    if rec.subtype_id.name == 'Discussions':
                        body = ('{author} sent a message In {name} Task chatter with content: {message} '.format(
                            author=rec.author_id.name,
                            name=task_id.name,
                            message=rec.body,
                            message_type='comment',
                            subtype_xmlid='mail.mt_comment'))
                    else:
                        body = ('{author} wrote a note In {name} Task chatter with content: {note} '.format(
                            author=rec.author_id.name,
                            name=task_id.name,
                            note=rec.note,
                            message_type='comment',
                            subtype_xmlid='mail.mt_comment'))

                    channel_id.message_post(body=body)
        return rec

    def get_message_note(self, message):
        if message.body:
            message.note = message.body
        else:
            message.note = (
                    """<div><p>""" + message.subtype_id.description + """</p></div>""") if message.subtype_id.description else """"""
            if message.sudo().tracking_value_ids:
                for value in message.tracking_value_ids:
                    message.note = """<div>""" + str(message.note) + """</div><span>""" + str(
                        value.field_desc) + """<span>:  </span> </span>"""
                    if value.field_type == 'datetime':
                        message.note = str(message.note) + """<span>""" + str(
                            value.old_value_datetime) + """</span><span>  =>  """ + str(
                            value.new_value_datetime) + """</span>"""
                    elif value.field_type == "float":
                        message.note = str(message.note) + """<span>""" + str(
                            value.old_value_float) + """</span><span>  =>  """ + str(
                            value.new_value_float) + + """</span>"""
                    elif value.field_type == "integer":
                        message.note = str(message.note) + """<span>""" + str(
                            value.old_value_integer) + """</span><span>  =>  """ + str(
                            value.new_value_integer) + """</span>"""
                    else:
                        message.note = str(message.note) + """<span>""" + str(
                            value.old_value_char) + """</span><span>  =>  """ + str(
                            value.new_value_char) + """</span>"""
        return message.note
