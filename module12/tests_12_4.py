# Домашнее задание по теме "Логирование"
import logging
import unittest as ut

from module12.rt_with_exceptions import Runner


class RunnerTest(ut.TestCase):

    def test_walk(self):
        try:
            run = Runner("one", -5)
            for _ in range(10):
                run.walk()
            self.assertEqual(run.distance, 50)
            logging.info(f'"test_walk" выполнен успешно', exc_info=False)
        except Exception as exc:
            logging.warning(f"Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            run = Runner(2, 10)
            for _ in range(10):
                run.run()
            print(run.distance, 100)
            self.assertEqual(run.distance, 200)
            if run.distance == 200:
                logging.info(f'"test_run" выполнен успешно', exc_info=False)
            else:
                logging.info(f'"test_run" не выполнен успешно, дистанции не совпали', exc_info=False)
        except Exception as exc:
            logging.warning(f"Неверный тип данных для объекта Runner", exc_info=True)


logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                    format="%(asctime)s; %(levelname)s; %(message)s.")
