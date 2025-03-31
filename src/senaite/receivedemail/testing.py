# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import senaite.receivedemail


class SenaiteReceivedemailLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=senaite.receivedemail)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'senaite.receivedemail:default')


SENAITE_RECEIVEDEMAIL_FIXTURE = SenaiteReceivedemailLayer()


SENAITE_RECEIVEDEMAIL_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SENAITE_RECEIVEDEMAIL_FIXTURE,),
    name='SenaiteReceivedemailLayer:IntegrationTesting',
)


SENAITE_RECEIVEDEMAIL_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SENAITE_RECEIVEDEMAIL_FIXTURE,),
    name='SenaiteReceivedemailLayer:FunctionalTesting',
)


SENAITE_RECEIVEDEMAIL_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SENAITE_RECEIVEDEMAIL_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SenaiteReceivedemailLayer:AcceptanceTesting',
)
