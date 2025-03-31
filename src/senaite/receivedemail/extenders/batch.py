# -*- coding: utf-8 -*-

from Products.Archetypes.Widget import BooleanWidget
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from archetypes.schemaextender.interfaces import ISchemaExtender
from zope.component import adapts
from zope.interface import implementer

from bika.lims.interfaces import IBatch
from senaite.receivedemail.config import _
from senaite.receivedemail.interfaces import ISenaiteReceivedemailLayer
from senaite.receivedemail.extenders.fields import ExtBooleanField


notified_samples_received_field = ExtBooleanField(
    "NotifiedSamplesReceived",
    mode="rw",
    schemata="default",
    widget=BooleanWidget(
        label=_("Notified Batch Samples have been Received"),
        format="select",
        visible={"add": "invinsible", "edit": "invinsible"},
    ),
)


@implementer(ISchemaExtender, IBrowserLayerAwareExtender)
class BatchSchemaExtender(object):
    adapts(IBatch)
    layer = ISenaiteReceivedemailLayer

    fields = [
        notified_samples_received_field,
    ]

    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
        return schematas

    def getFields(self):
        return self.fields
