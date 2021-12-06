import unittest
from Tests.home.login_tests import LoginPage
from Tests.safhe_asli.ijad_proje_multipledataset_csv import IjadMultipleProje2_csv


# 1) get the test we want to wrap as suite , with use of TestLoader

Tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginPage)
Tc2 = unittest.TestLoader().loadTestsFromTestCase(IjadMultipleProje2_csv)


# 2) create testSuite and combine tests, with use of TestSuite method
regression = unittest.TestSuite([Tc1, Tc2])

# 3) triggle the runner  by "TextTestRunner" method

unittest.TextTestRunner(verbosity=2).run(regression)
