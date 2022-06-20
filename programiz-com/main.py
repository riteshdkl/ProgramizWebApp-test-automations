import unittest

from AutomatedTesting.examplePage.Python.allExamples import allExamples
from AutomatedTesting.examplePage.Python.filesExample import filesExamples
from AutomatedTesting.examplePage.Python.popularExamples import popularExamples
from AutomatedTesting.homepage.footerSection import footerSection
from AutomatedTesting.homepage.headingSection import heading
from AutomatedTesting.homepage.mobileAppSection import mobileApp
from AutomatedTesting.homepage.navbar import navbar
from AutomatedTesting.homepage.onlineCompilersSection import onlineCompilers
from AutomatedTesting.homepage.programizProSection import programizPro
from AutomatedTesting.homepage.whyProgramizSection import whyProgramiz
from AutomatedTesting.languageLandingPage.learnPython.headingSection import \
    heading
from AutomatedTesting.languageLandingPage.learnPython.pageContents import \
    contents
from AutomatedTesting.languageLandingPage.learnPython.pageLinks import links
from AutomatedTesting.languageLandingPage.learnSQL.headingSection import \
    heading
from AutomatedTesting.languageLandingPage.learnSQL.pageContents import contents
from AutomatedTesting.languageLandingPage.learnSQL.pageLinks import Pagelinks
from AutomatedTesting.referencesPage.javaScriptReferences import \
    javaScriptReferences
from AutomatedTesting.referencesPage.pythonReferences import pythonReferences
from AutomatedTesting.tutorialPage.Java.javaIntroduction import introduction
from AutomatedTesting.tutorialPage.Python.pythonFunctions import functions
from AutomatedTesting.tutorialPage.Python.pythonIntroduction import \
    introduction




tc1 = unittest.TestLoader().loadTestsFromTestCase(navbar)
tc2 = unittest.TestLoader().loadTestsFromTestCase(heading)
tc3 = unittest.TestLoader().loadTestsFromTestCase(programizPro)
tc4 = unittest.TestLoader().loadTestsFromTestCase(onlineCompilers)
tc5 = unittest.TestLoader().loadTestsFromTestCase(whyProgramiz)
tc6 = unittest.TestLoader().loadTestsFromTestCase(mobileApp)
tc7 = unittest.TestLoader().loadTestsFromTestCase(footerSection)

tc8 = unittest.TestLoader().loadTestsFromTestCase(heading)
tc9 = unittest.TestLoader().loadTestsFromTestCase(contents)
tc10 = unittest.TestLoader().loadTestsFromTestCase(links)
tc11 = unittest.TestLoader().loadTestsFromTestCase(heading)
tc12 = unittest.TestLoader().loadTestsFromTestCase(contents)
tc13 = unittest.TestLoader().loadTestsFromTestCase(Pagelinks)


tc14 = unittest.TestLoader().loadTestsFromTestCase(allExamples)
tc15 = unittest.TestLoader().loadTestsFromTestCase(filesExamples)
tc16 = unittest.TestLoader().loadTestsFromTestCase(popularExamples)

tc17 = unittest.TestLoader().loadTestsFromTestCase(javaScriptReferences)
tc18 = unittest.TestLoader().loadTestsFromTestCase(pythonReferences)

tc19 = unittest.TestLoader().loadTestsFromTestCase(functions)
tc20 = unittest.TestLoader().loadTestsFromTestCase(introduction)
tc21 = unittest.TestLoader().loadTestsFromTestCase(introduction)




homepage = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5, tc6, tc7])
languageLandingPage = unittest.TestSuite([tc8,tc9,tc10,tc11,tc12,tc13])
examplePage = unittest.TestSuite([tc14,tc15,tc16])
referencePage = unittest.TestSuite([tc17,tc18])
tutorialPage = unittest.TestSuite([tc19,tc20,tc21])


unittest.TextTestRunner().run(homepage)
unittest.TextTestRunner().run(languageLandingPage)
unittest.TextTestRunner().run(examplePage)
unittest.TextTestRunner().run(referencePage)
unittest.TextTestRunner().run(tutorialPage)

