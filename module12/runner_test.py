# Домашнее задание по теме "Простые Юнит-Тесты"

import unittest as ut
from module12.runner import Runner


class RunnerTest(ut.TestCase):
    def test_walk(self):
        run = Runner("one")
        for _ in range(10):
            run.walk()
        self.assertEqual(run.distance, 50)

    def test_run(self):
        run = Runner("two")
        for _ in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        run_one = Runner("one")
        run_two = Runner("two")
        for _ in range(10):
            run_one.run()
            run_two.walk()
        self.assertNotEqual(run_one.distance, run_two.distance)


if __name__ == "__main__":
    ut.main()
