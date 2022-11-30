from odoo import api, models, fields, _
import datetime


class ResourceCalenderLeavesInherited(models.Model):
    _inherit = 'resource.calendar.leaves'

    def _daily_send_holiday_reminder(self):
        next_week = str((datetime.datetime.now() + datetime.timedelta(days=7)).date())
        print(next_week)
        holiday_ids = self.env['resource.calendar.leaves'].search(
            [('resource_id', '=', False)])
        for holiday_id in holiday_ids:
            print(holiday_id.date_from)
            if str(holiday_id.date_from.date()) == next_week:
                self.send_private_message_to_hr_manager(holiday_id)

    def send_private_message_to_hr_manager(self, holiday_id):
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        action_id = self.env.ref('hr_holidays.open_view_public_holiday')
        url = base_url + '/web#' + 'action=' + str(action_id.id) + '&model=resource.calendar.leaves'
        users = self.env.ref('hr.group_hr_manager').users
        for user in users:
            channel = self.env['mail.channel'].channel_get(
                [user.partner_id.id])
            channel_id = self.env['mail.channel'].browse(channel["id"])
            channel_id.message_post(
                body=('Reminder :{name} Holiday starts in {date}.\n you can configure it from {url} '.format(
                    name=holiday_id.name,
                    date=str(holiday_id.date_from.date()), url=url)),
                message_type='comment',
                subtype_xmlid='mail.mt_comment',
            )

