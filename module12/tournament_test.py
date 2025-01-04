# Домашнее задание по теме "Простые Юнит-Тесты"

import unittest as ut
from pprint import pprint

from module12.runner_and_tournament import Runner, Tournament


class TournamentTest(ut.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner_U = Runner("Усэйн", 10)
        self.runner_A = Runner("Андрей", 9)
        self.runner_N = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        pprint(cls.all_results)

    def create_tournament(self):
        self.tournament_1 = Tournament(90,(self.runner_U,self.runner_N))
        TournamentTest.all_results.append(self.tournament_1.start())




