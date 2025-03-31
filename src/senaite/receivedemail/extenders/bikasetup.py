# -*- coding: utf-8 -*-

from Products.Archetypes.Widget import BooleanWidget
from Products.Archetypes.Widget import RichWidget
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from archetypes.schemaextender.interfaces import ISchemaExtender
from zope.component import adapts
from zope.interface import implementer

from bika.lims.interfaces import IBikaSetup
from senaite.receivedemail.config import _
from senaite.receivedemail.extenders.fields import ExtBooleanField
from senaite.receivedemail.extenders.fields import ExtTextField
from senaite.receivedemail.interfaces import ISenaiteReceivedemailLayer

received_samples_email_body_field = ExtTextField(
    "ReceivedSamplesEmailBody",
    mode="rw",
    default_content_type="text/html",
    default_output_type="text/x-html-safe",
    schemata="Notifications",
    # Needed to fetch the default value from the registry
    default=_(
        "Dear $recipients,"
        "<br/>"
        "<br/>"
        "We received $number_of_samples samples and they were submitted "
        "to the lab for Analysis in batch $client_batch_number, $batch_title, "
        "$batch_id"
        "<br/>"
        "<br/>"
        "Much appreciated"
        "<br/>"
        "<br/>"
        "$lab_name"
    ),
    widget=RichWidget(
        label=_(
            "label_bikasetup_received_samples_email_body",
            "Email body for Samples received notifications",
        ),
        description=_(
            "description_bikasetup_received_samples_email_body",
            default="Set the email body text to be used by default when "
            "sending out received samples notification to the selected recipients. "
            "You can use reserved keywords: "
            "$batch_id, $batch_title, $client_batch_number, $client_name, $lab_name, "
            "$lab_address, $number_of_samples, $recipients",
        ),
        default_mime_type="text/x-html",
        output_mime_type="text/x-html",
        allow_file_upload=False,
        rows=15,
    ),
)

email_samples_receive_notifications_field = ExtBooleanField(
    "EmailSampleReceiveNotifications",
    mode="rw",
    schemata="Notifications",
    default=False,
    widget=BooleanWidget(
        label=_(
            "label_bikasetup_email_samples_receive_notifications",
            "Email Samples Receive Notifications",
        ),
        description=_(
            "description_bikasetup_email_samples_receive_notifications",
            default="Send email notification on samples received on a batch"
        ),
    ),
)


@implementer(ISchemaExtender, IBrowserLayerAwareExtender)
class BikaSetupSchemaExtender(object):
    adapts(IBikaSetup)
    layer = ISenaiteReceivedemailLayer

    fields = [
        email_samples_receive_notifications_field,
        received_samples_email_body_field,
    ]

    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
        return schematas

    def getFields(self):
        return self.fields
