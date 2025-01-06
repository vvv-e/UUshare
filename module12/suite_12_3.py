# Домашнее задание по теме "Систематизация и пропуск тестов".
import unittest as ut
import runner_test
import tournament_test

tsuite_runner_and_tournament = ut.TestSuite()
tsuite_runner_and_tournament.addTest(ut.TestLoader().loadTestsFromTestCase(runner_test.RunnerTest))
tsuite_runner_and_tournament.addTest(ut.TestLoader().loadTestsFromTestCase(tournament_test.TournamentTest))
runner = ut.TextTestRunner(verbosity=2)
runner.run(tsuite_runner_and_tournament)