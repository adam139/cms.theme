from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from zope.configuration import xmlconfig

class Theme(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import cms.theme
        xmlconfig.file('configure.zcml', cms.theme, context=configurationContext)
    
    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cms.theme:default')

FIXTURE = Theme()
INTEGRATION_TESTING = IntegrationTesting(bases=(FIXTURE,), name="Theme:Integration")
FUNCTION_TESTING = FunctionalTesting(bases=(FIXTURE,), name="Theme:Functional")
