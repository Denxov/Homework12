import unittest


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
    def test_walk(self):
        run1 = Runner('first')
        for i in range(10):
            run1.walk()
        self.assertEqual(run1.distance, 50)

    def test_run(self):
        run1 = Runner('first')
        for i in range(10):
            run1.run()
        self.assertEqual(run1.distance, 100)

    def test_challenge(self):
        run1 = Runner('first')
        run2 = Runner("second")
        for i in range(10):
            run1.walk()
            run2.run()
        self.assertNotEqual(run1.distance, run2.distance)


if __name__ == '__main__': unittest.main()
