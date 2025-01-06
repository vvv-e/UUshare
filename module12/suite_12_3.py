# Домашнее задание по теме "Систематизация и пропуск тестов".
import unittest as ut
import runner_test_next
import tournament_test_next

tsuite_runner_and_tournament = ut.TestSuite()
tsuite_runner_and_tournament.addTest(ut.TestLoader().loadTestsFromTestCase(runner_test_next.RunnerTest))
tsuite_runner_and_tournament.addTest(ut.TestLoader().loadTestsFromTestCase(tournament_test_next.TournamentTest))
runner = ut.TextTestRunner(verbosity=2)
runner.run(tsuite_runner_and_tournament)