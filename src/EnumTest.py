from enum import Enum, unique

weekday = Enum('weekday', ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'))
for day in weekday:
    print(day)


@unique
class Month(Enum):
    Jan = 1,
    Feb = 2,
    Mar = 3

print(Month.Feb.value[0])

