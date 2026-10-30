class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def plus_day(self):
        months_dict = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            if self.month == 2 and self.day == 28:
                self.day = 29

        elif self.day == months_dict[self.month]:
            self.month += 1
            self.day = 1
        elif self.month == 12:
            self.year += 1
            self.month = 1
            self.day = 1
        else:
            self.day += 1


    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"


d = Date(28, 12, 2009)
print(d)
d.plus_day()
d.plus_day()
d.plus_day()
d.plus_day()
d.plus_day()
for i in range(30):
    d.plus_day()
print(d)
