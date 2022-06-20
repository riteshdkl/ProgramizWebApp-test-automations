import unittest

from AutomatedTesting.languageLandingPage.learnPython.headingSection import \
    heading
from AutomatedTesting.languageLandingPage.learnPython.pageContents import \
    contents
from AutomatedTesting.languageLandingPage.learnPython.pageLinks import links

# import HtmlTestRunner
# from homepage.footerSection import footerSection
# from homepage.headingSection import heading
# from homepage.mobileAppSection import mobileApp
# from homepage.navbar import navbar
# from homepage.onlineCompilersSection import onlineCompilers
# from homepage.programizProSection import programizPro
# from homepage.whyProgramizSection import whyProgramiz


# tc1 = unittest.TestLoader().loadTestsFromTestCase(navbar)
# tc2 = unittest.TestLoader().loadTestsFromTestCase(heading)
# tc3 = unittest.TestLoader().loadTestsFromTestCase(programizPro)
# tc4 = unittest.TestLoader().loadTestsFromTestCase(onlineCompilers)
# tc5 = unittest.TestLoader().loadTestsFromTestCase(whyProgramiz)
# tc6 = unittest.TestLoader().loadTestsFromTestCase(mobileApp)
# tc7 = unittest.TestLoader().loadTestsFromTestCase(footerSection)
tc8 = unittest.TestLoader().loadTestsFromTestCase(heading)
tc9 = unittest.TestLoader().loadTestsFromTestCase(contents)
tc10 = unittest.TestLoader().loadTestsFromTestCase(links)

# homepage = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5, tc6, tc7])
languageLandingPage = unittest.TestSuite([tc8])

# unittest.TextTestRunner().run(homepage)
unittest.TextTestRunner().run(languageLandingPage)
