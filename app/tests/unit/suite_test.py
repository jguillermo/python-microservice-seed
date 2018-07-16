# -*- coding: utf-8 -*-

import unittest

from tests.unit.user import TestUserFinderService, TestUserCreateService, TestUserUpdateService


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(TestUserFinderService))
    suite.addTests(loader.loadTestsFromModule(TestUserCreateService))
    suite.addTests(loader.loadTestsFromModule(TestUserUpdateService))
    return suite


if __name__ == '_main_':
    unittest.TextTestRunner(verbosity=2).run(suite())
