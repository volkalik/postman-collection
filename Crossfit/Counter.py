class crossfit_open:
    def __init__(self, athlete, open_number, time, reps):
        self.open_number = open_number
        self.time = time
        self.reps = reps
        self.athlete = athlete

    def open_result(self, open_number, time):
        return f'{self.athlete} finished {open_number} in {time} minutes'


crossfit_open.open_result('open14.5', 12, 198)

"""open_14_5 = [21, 18, 15, 12, 9, 6, 3]"""
