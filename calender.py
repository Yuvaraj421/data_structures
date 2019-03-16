import numpy


def day(month, year, day):

    y0 = year - (14 - month) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = month + 12 * ((14 - month) // 12) - 2
    d0 = (day + x + 31 * m0 // 12) % 7
    return d0


def isleapyear(year):

    if int(year) % 4 == 0 and int(year) % 400 == 0 and int(year) % 100 != 0:
        return True
    else:
        return False


if __name__ == "__main__":
    try:
        months = ["", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
                  "november", "december"]
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = int(input("Enter the month: "))
        year = int(input("Enter the year: "))
        if month == 2 and isleapyear(year):
            days[month] = 29
        space = day(month, year, 1)

        array = numpy.zeros((6, 7), dtype=int)
        x = 1
        dayz = space
        for i in range(6):
            for j in range(space, 7):
                if x <= days[month]:
                    array[i][j] = x
                    x += 1
            space = 0
        for j in range(dayz):
            array[0][j] = array[5][j] = 0

        print("calender ", month, " ", year)
        print("----")
        print("", months[month], "    ", year)
        print("------")
        print("sun   mon   tue   wed   thu   fri   sat")
        print("")

        for i in range(5):
            for j in range(7):
                if array[i][j] != 0:
                    print(array[i][j], end="    ")
                else:
                    print(end="    ")
            print()
    except Exception as e:
        print(e)
