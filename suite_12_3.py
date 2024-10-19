import unittest
import test_12_3


tourST = unittest.TestSuite()
tourST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))
tourST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))

TextTestRunner = unittest.TextTestRunner(verbosity=2)
TextTestRunner.run(tourST)