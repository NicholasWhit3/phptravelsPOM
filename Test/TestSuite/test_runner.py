from unittest import TestLoader , TestSuite , TextTestRunner

import testtools as testtools

from Test.Scripts.Test_HomePage import Test_HomePage
from Test.Scripts.Test_RegistrationPage import Test_RegistrationPage

if __name__ == "__main__":

    test_loader = TestLoader()

    test_suite_home_page = TestSuite((
        test_loader.loadTestsFromTestCase(Test_HomePage),
        test_loader.loadTestsFromTestCase(Test_RegistrationPage)
    ))



    test_runner = TextTestRunner(verbose=2)
    test_runner.run(test_suite_home_page)

    parallel_suite = testtools.ConcurrentStreamSuite(lambda: ((case, None) for case in test_suite_home_page))
    parallel_suite.run(testtools.SteamResult())