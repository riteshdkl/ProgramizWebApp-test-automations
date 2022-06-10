import unittest

import HtmlTestRunner
from homepage.footerSection import footerSection
from homepage.headingSection import heading
from homepage.mobileAppSection import mobileApp
from homepage.navbar import navbar
from homepage.onlineCompilersSection import onlineCompilers
from homepage.programizProSection import programizPro
from homepage.whyProgramizSection import whyProgramiz

tc1 = unittest.TestLoader().loadTestsFromTestCase(navbar)
tc2 = unittest.TestLoader().loadTestsFromTestCase(heading)
tc3 = unittest.TestLoader().loadTestsFromTestCase(programizPro)
tc4 = unittest.TestLoader().loadTestsFromTestCase(onlineCompilers)
tc5 = unittest.TestLoader().loadTestsFromTestCase(whyProgramiz)
tc6 = unittest.TestLoader().loadTestsFromTestCase(mobileApp)
tc7 = unittest.TestLoader().loadTestsFromTestCase(footerSection)

homepage = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5, tc6, tc7])

unittest.TextTestRunner().run(homepage)
