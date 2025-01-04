# Домашнее задание по теме "Простые Юнит-Тесты"

import unittest as ut
from module12.runner_and_tournament import Runner, Tournament


class TournamentTest(ut.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for i in range(len(cls.all_results)):
            print({j: str(cls.all_results[i][j]) for j in cls.all_results[i]})

    def setUp(self):
        self.runner_U = Runner("Усэйн", 10)
        self.runner_A = Runner("Андрей", 9)
        self.runner_N = Runner("Ник", 3)

    def test_tournament(self):
        self.runner_U.distance = 0
        self.runner_N.distance = 0
        self.tournament = Tournament(90, self.runner_U, self.runner_N)
        TournamentTest.all_results[0] = self.tournament.start()
        self.runner_A.distance = 0
        self.runner_N.distance = 0
        self.tournament = Tournament(90, self.runner_A, self.runner_N)
        TournamentTest.all_results[1] = self.tournament.start()
        self.runner_U.distance = 0
        self.runner_A.distance = 0
        self.runner_N.distance = 0
        self.tournament = Tournament(90, self.runner_U, self.runner_A, self.runner_N)
        TournamentTest.all_results[2] = self.tournament.start()
        flag = True
        for i in range(len(TournamentTest.all_results)):
            if str(TournamentTest.all_results[i][max(TournamentTest.all_results[i])]) != "Ник":
                flag = False
                break
        self.assertTrue(flag)

    # Дополнительно (не обязательно)
    def test_tournament_new(self):
        """
        self.runner_U.distance = 0
        self.runner_A.distance = 0
        tournament = Tournament(90, self.runner_A, self.runner_U)
        res = tournament.start()
        self.assertTrue(str(res[min(res)]) == "Усэйн" and str(res[max(res)]) == "Андрей")
        """
        self.assertTrue(str(TournamentTest.all_results[2][min(TournamentTest.all_results[2])]) == "Усэйн" and str(
            TournamentTest.all_results[2][min(TournamentTest.all_results[2])+1]) == "Андрей")


if __name__ == "__main__":
    ut.main()
