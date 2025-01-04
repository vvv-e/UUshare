class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        # отсортировать список в соответствии со скоростями для корректной работы программы
        # Дополнительно (не обязательно)
        self.participants = []
        lp = list(participants)
        while lp:
            max_speed = 0
            max_prt = None
            for prt in lp:
                if prt.speed >= max_speed:
                    max_speed = prt.speed
                    max_prt = prt
            self.participants.append(max_prt)
            lp.remove(max_prt)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


if __name__ == "__main__":
    all_results = {}
    runner_U = Runner("Усэйн", 10)
    runner_A = Runner("Андрей", 9)
    runner_N = Runner("Ник", 3)
    tournament = Tournament(90, runner_U, runner_N)
    all_results[0] = tournament.start()
    runner_A.distance = 0
    runner_N.distance = 0
    tournament = Tournament(90, runner_A, runner_N)
    all_results[1] = tournament.start()
    runner_U.distance = 0
    runner_A.distance = 0
    runner_N.distance = 0
    tournament = Tournament(90, runner_U, runner_A, runner_N)
    all_results[2] = tournament.start()
    runner_U.distance = 0
    runner_A.distance = 0
    tournament = Tournament(90, runner_A, runner_U)
    all_results[3] = tournament.start()
    for i in range(len(all_results)):
        print({j: str(all_results[i][j]) for j in all_results[i]})
