def intToMonthParser(number):
  if number == 1:
    return 'Jan'
  elif number == 2:
    return 'Feb'
  elif number == 3:
    return 'Mar'
  elif number == 4:
    return 'Apr'
  elif number == 5:
    return 'May'
  elif number == 6:
    return 'Jun'
  elif number == 7:
    return 'July'
  elif number == 8:
    return 'Aug'
  elif number == 9:
    return 'Sep'
  elif number == 10:
    return 'Oct'
  elif number == 11:
    return 'Nov'
  elif number == 12:
    return 'Dec'

def intToDayOfTheWeek(number):
  if number == 0:
    return 'Mon'
  elif number == 1:
    return 'Tue'
  elif number == 2:
    return 'Wed'
  elif number == 3:
    return 'Thu'
  elif number == 4:
    return 'Fri'
  elif number == 5:
    return 'Sat'
  elif number == 6:
    return 'Sun'

def intToFullDayOfTheWeek(number):
  courseDays = ['Mondays', 'Tuesdays', 'Wednesdays', 'Thursdays', 'Fridays', 'Saturdays', 'Sundays']

  return courseDays[number]