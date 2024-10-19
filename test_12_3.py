import unittest
import Test


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты заморожены')
    def test_walk(self):
        a1 = Runner('max')
        for i in range(10):
            a1.walk()

        self.assertEqual(a1.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты заморожены')
    def test_run(self):
        a1 = Runner('max')
        for i in range(10):
            a1.run()

        self.assertEqual(a1.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты заморожены')
    def test_chalLenge(self):
        a1 = Runner('david')
        a2 = Runner('max')
        for i in range(10):
            a1.run()

        for i in range(10):
            a2.walk()
        self.assertNotEqual(a1.distance, a2.distance)


if __name__ == '__main__':
    unittest.main()



class TournamentTest(unittest.TestCase):
    all_results = {}
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.a1 = Test.Runner('Усэйн', 10)
        self.a2 = Test.Runner('Андрей', 9)
        self.a3 = Test.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(test_key)
            for key, value in test_value.items():
                print(f'{key}: {value.name}')

    # @unittest.skipUnless(is_frozen == False, 'ok')
    @unittest.skipIf(is_frozen == True, 'Тесты заморожены')
    def test_run(self):
        run1 = Test.Tournament(90, self.a1, self.a3)
        win = run1.start()

        self.assertTrue(win[list(win.keys())[-1]] == "Ник")
        self.all_results['1) Результат'] = win

    # @unittest.skipUnless(is_frozen == False, 'ok')
    @unittest.skipIf(is_frozen == True, 'Тесты заморожены')
    def test_run2(self):
        run2 = Test.Tournament(90, self.a2, self.a3)
        win = run2.start()

        self.assertTrue(win[list(win.keys())[-1]] == 'Ник')
        self.all_results['\n2) Результат'] = win

    # @unittest.skipUnless(is_frozen == False, 'ok')
    @unittest.skipIf(is_frozen == True, 'Тесты заморожены')
    def test_run3(self):
        run3 = Test.Tournament(90, self.a1, self.a2, self.a3)
        win = run3.start()

        self.assertTrue(win[list(win.keys())[-1]] == 'Ник')
        self.all_results['\n3) Результат'] = win


if __name__ == '__main__':
    unittest.main()