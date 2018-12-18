import coursePrices


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

def coursePriceGenerator(courseName, courseType, prices = coursePrices):
  """
  This function will take in 2 compulsory arguments, courseName and courseType.

  courseName is a string of the course name, ie. 'Fundamentals 1'.
  courseType is a string of the course type, ie. 'Weekend Weekly', 'Weekday Weekly', 'Holiday Camp'.

  The 3rd argument is an optional one, already set by default with coursePrices.py list of prices, so there isn't anything necessary to pass in as 3rd argument.

  This function will parse the given 2 strings, namely courseName and courseType and returns a dictionary, detailing 2 fields, 'normal' and 'earlyBird'.
  """
  price = {
    "normal": '',
    "earlyBird": ''
  }

  if courseName == 'FUNdamentals 1':
    if courseType == 'Weekend Weekly':
      price["normal"] = f"SGD{prices.fundamentals1['weekly']}"
      price["earlyBird"] = f"SGD{prices.fundamentals1['weekly'] - prices.earlyBirdDiscount}"
    elif courseType == 'Weekday Weekly':
      price["normal"] = f"SGD{prices.fundamentals1['weekly'] - prices.weekdayDiscount}"
      price["earlyBird"] = f"SGD{prices.fundamentals1['weekly'] - prices.weekdayDiscount - prices.earlyBirdDiscount}"
    elif courseType == 'Holiday Camp':
      price["normal"] = f"SGD{prices.fundamentals1['camp']}"
      price["earlyBird"] = f"SGD{prices.fundamentals1['camp'] - prices.earlyBirdDiscount}"


  elif courseName in ['FUNdamentals 2R', 'FUNdamentals 2G', 'FUNdamentals 2B']:
    if courseType == 'Weekend Weekly':
      price["normal"] = f"SGD{prices.fundamentals2['weekly']}"
      price["earlyBird"] = f"SGD{prices.fundamentals2['weekly'] - prices.earlyBirdDiscount}"
    elif courseType == 'Weekday Weekly':
      price["normal"] = f"SGD{prices.fundamentals2['weekly'] - prices.weekdayDiscount}"
      price["earlyBird"] = f"SGD{prices.fundamentals2['weekly'] - prices.weekdayDiscount - prices.earlyBirdDiscount}"
    elif courseType == 'Holiday Camp':
      price["normal"] = f"SGD{prices.fundamentals2['camp']}"
      price["earlyBird"] = f"SGD{prices.fundamentals2['camp'] - prices.earlyBirdDiscount}"

  elif courseName == 'Basics 1':
    if courseType == 'Weekend Weekly':
      price["normal"] = f"SGD{prices.basics1['weekly']}"
      price["earlyBird"] = f"SGD{prices.basics1['weekly'] - prices.earlyBirdDiscount}"
    elif courseType == 'Weekday Weekly':
      price["normal"] = f"SGD{prices.basics1['weekly'] - prices.weekdayDiscount}"
      price["earlyBird"] = f"SGD{prices.basics1['weekly'] - prices.weekdayDiscount - prices.earlyBirdDiscount}"
    elif courseType == 'Holiday Camp':
      price["normal"] = f"SGD{prices.basics1['camp']}"
      price["earlyBird"] = f"SGD{prices.basics1['camp'] - prices.earlyBirdDiscount}"

  elif courseName in ['Basics 2R', 'Basics 2G', 'Basics 2B']:
    if courseType == 'Weekend Weekly':
      price["normal"] = f"SGD{prices.basics2['weekly']}"
      price["earlyBird"] = f"SGD{prices.basics2['weekly'] - prices.earlyBirdDiscount}"
    elif courseType == 'Weekday Weekly':
      price["normal"] = f"SGD{prices.basics2['weekly'] - prices.weekdayDiscount}"
      price["earlyBird"] = f"SGD{prices.basics2['weekly'] - prices.weekdayDiscount - prices.earlyBirdDiscount}"
    elif courseType == 'Holiday Camp':
      price["normal"] = f"SGD{prices.basics2['camp']}"
      price["earlyBird"] = f"SGD{prices.basics2['camp'] - prices.earlyBirdDiscount}"

  elif courseName == 'Basics 3':
    if courseType == 'Weekend Weekly':
      price["normal"] = f"SGD{prices.basics3['weekly']}"
      price["earlyBird"] = f"SGD{prices.basics3['weekly'] - prices.earlyBirdDiscount}"
    elif courseType == 'Weekday Weekly':
      price["normal"] = f"SGD{prices.basics3['weekly'] - prices.weekdayDiscount}"
      price["earlyBird"] = f"SGD{prices.basics3['weekly'] - prices.weekdayDiscount - prices.earlyBirdDiscount}"
    elif courseType == 'Holiday Camp':
      price["normal"] = f"SGD{prices.basics3['camp']}"
      price["earlyBird"] = f"SGD{prices.basics3['camp'] - prices.earlyBirdDiscount}"
      
  elif courseName in ['Basics 4R', 'Basics 4G', 'Basics 4B']:
    if courseType == 'Weekend Weekly':
      price["normal"] = f"SGD{prices.basics4['weekly']}"
      price["earlyBird"] = f"SGD{prices.basics4['weekly'] - prices.earlyBirdDiscount}"
    elif courseType == 'Weekday Weekly':
      price["normal"] = f"SGD{prices.basics4['weekly'] - prices.weekdayDiscount}"
      price["earlyBird"] = f"SGD{prices.basics4['weekly'] - prices.weekdayDiscount - prices.earlyBirdDiscount}"
    elif courseType == 'Holiday Camp':
      price["normal"] = f"SGD{prices.basics4['camp']}"
      price["earlyBird"] = f"SGD{prices.basics4['camp'] - prices.earlyBirdDiscount}"
      
  elif courseName == 'Basics 5':
    if courseType == 'Weekend Weekly':
      price["normal"] = f"SGD{prices.basics5['weekly']}"
      price["earlyBird"] = f"SGD{prices.basics5['weekly'] - prices.earlyBirdDiscount}"
    elif courseType == 'Weekday Weekly':
      price["normal"] = f"SGD{prices.basics5['weekly'] - prices.weekdayDiscount}"
      price["earlyBird"] = f"SGD{prices.basics5['weekly'] - prices.weekdayDiscount - prices.earlyBirdDiscount}"
    elif courseType == 'Holiday Camp':
      price["normal"] = f"SGD{prices.basics5['camp']}"
      price["earlyBird"] = f"SGD{prices.basics5['camp'] - prices.earlyBirdDiscount}"
      
  elif courseName in ['Basics 6R', 'Basics 6G', 'Basics 6B']:
    if courseType == 'Weekend Weekly':
      price["normal"] = f"SGD{prices.basics6['weekly']}"
      price["earlyBird"] = f"SGD{prices.basics6['weekly'] - prices.earlyBirdDiscount}"
    elif courseType == 'Weekday Weekly':
      price["normal"] = f"SGD{prices.basics6['weekly'] - prices.weekdayDiscount}"
      price["earlyBird"] = f"SGD{prices.basics6['weekly'] - prices.weekdayDiscount - prices.earlyBirdDiscount}"
    elif courseType == 'Holiday Camp':
      price["normal"] = f"SGD{prices.basics6['camp']}"
      price["earlyBird"] = f"SGD{prices.basics6['camp'] - prices.earlyBirdDiscount}"
      
  elif courseName == 'Principles 1':
    if courseType == 'Weekend Weekly':
      price["normal"] = f"SGD{prices.principles1['weekly']}"
      price["earlyBird"] = f"SGD{prices.principles1['weekly'] - prices.earlyBirdDiscount}"
    elif courseType == 'Weekday Weekly':
      price["normal"] = f"SGD{prices.principles1['weekly'] - prices.weekdayDiscount}"
      price["earlyBird"] = f"SGD{prices.principles1['weekly'] - prices.weekdayDiscount - prices.earlyBirdDiscount}"
    elif courseType == 'Holiday Camp':
      price["normal"] = f"SGD{prices.principles1['camp']}"
      price["earlyBird"] = f"SGD{prices.principles1['camp'] - prices.earlyBirdDiscount}"
      
  elif courseName == 'Principles 2':
    if courseType == 'Weekend Weekly':
      price["normal"] = f"SGD{prices.principles2['weekly']}"
      price["earlyBird"] = f"SGD{prices.principles2['weekly'] - prices.earlyBirdDiscount}"
    elif courseType == 'Weekday Weekly':
      price["normal"] = f"SGD{prices.principles2['weekly'] - prices.weekdayDiscount}"
      price["earlyBird"] = f"SGD{prices.principles2['weekly'] - prices.weekdayDiscount - prices.earlyBirdDiscount}"
    elif courseType == 'Holiday Camp':
      price["normal"] = f"SGD{prices.principles2['camp']}"
      price["earlyBird"] = f"SGD{prices.principles2['camp'] - prices.earlyBirdDiscount}"
      
  elif courseName in ['Principles 3', 'Principles 3R', 'Principles 3G', 'Principles 3B']:
    if courseType == 'Weekend Weekly':
      price["normal"] = f"SGD{prices.principles3['weekly']}"
      price["earlyBird"] = f"SGD{prices.principles3['weekly'] - prices.earlyBirdDiscount}"
    elif courseType == 'Weekday Weekly':
      price["normal"] = f"SGD{prices.principles3['weekly'] - prices.weekdayDiscount}"
      price["earlyBird"] = f"SGD{prices.principles3['weekly'] - prices.weekdayDiscount - prices.earlyBirdDiscount}"
    elif courseType == 'Holiday Camp':
      price["normal"] = f"SGD{prices.principles3['camp']}"
      price["earlyBird"] = f"SGD{prices.principles3['camp'] - prices.earlyBirdDiscount}"
      
  elif courseName == 'Principles 4':
    if courseType == 'Weekend Weekly':
      price["normal"] = f"SGD{prices.principles4['weekly']}"
      price["earlyBird"] = f"SGD{prices.principles4['weekly'] - prices.earlyBirdDiscount}"
    elif courseType == 'Weekday Weekly':
      price["normal"] = f"SGD{prices.principles4['weekly'] - prices.weekdayDiscount}"
      price["earlyBird"] = f"SGD{prices.principles4['weekly'] - prices.weekdayDiscount - prices.earlyBirdDiscount}"
    elif courseType == 'Holiday Camp':
      price["normal"] = f"SGD{prices.principles4['camp']}"
      price["earlyBird"] = f"SGD{prices.principles4['camp'] - prices.earlyBirdDiscount}"
      
  elif courseName == 'Principles 5':
    if courseType == 'Weekend Weekly':
      price["normal"] = f"SGD{prices.principles5['weekly']}"
      price["earlyBird"] = f"SGD{prices.principles5['weekly'] - prices.earlyBirdDiscount}"
    elif courseType == 'Weekday Weekly':
      price["normal"] = f"SGD{prices.principles5['weekly'] - prices.weekdayDiscount}"
      price["earlyBird"] = f"SGD{prices.principles5['weekly'] - prices.weekdayDiscount - prices.earlyBirdDiscount}"
    elif courseType == 'Holiday Camp':
      price["normal"] = f"SGD{prices.principles5['camp']}"
      price["earlyBird"] = f"SGD{prices.principles5['camp'] - prices.earlyBirdDiscount}"
      
  elif courseName == 'Principles 6':
    if courseType == 'Weekend Weekly':
      price["normal"] = f"SGD{prices.principles6['weekly']}"
      price["earlyBird"] = f"SGD{prices.principles6['weekly'] - prices.earlyBirdDiscount}"
    elif courseType == 'Weekday Weekly':
      price["normal"] = f"SGD{prices.principles6['weekly'] - prices.weekdayDiscount}"
      price["earlyBird"] = f"SGD{prices.principles6['weekly'] - prices.weekdayDiscount - prices.earlyBirdDiscount}"
    elif courseType == 'Holiday Camp':
      price["normal"] = f"SGD{prices.principles6['camp']}"
      price["earlyBird"] = f"SGD{prices.principles6['camp'] - prices.earlyBirdDiscount}"
      
  elif courseName == 'Principles 7':
    if courseType == 'Weekend Weekly':
      price["normal"] = f"SGD{prices.principles7['weekly']}"
      price["earlyBird"] = f"SGD{prices.principles7['weekly'] - prices.earlyBirdDiscount}"
    elif courseType == 'Weekday Weekly':
      price["normal"] = f"SGD{prices.principles7['weekly'] - prices.weekdayDiscount}"
      price["earlyBird"] = f"SGD{prices.principles7['weekly'] - prices.weekdayDiscount - prices.earlyBirdDiscount}"
    elif courseType == 'Holiday Camp':
      price["normal"] = f"SGD{prices.principles7['camp']}"
      price["earlyBird"] = f"SGD{prices.principles7['camp'] - prices.earlyBirdDiscount}"
      
  elif courseName == 'Principles 8':
    if courseType == 'Weekend Weekly':
      price["normal"] = f"SGD{prices.principles8['weekly']}"
      price["earlyBird"] = f"SGD{prices.principles8['weekly'] - prices.earlyBirdDiscount}"
    elif courseType == 'Weekday Weekly':
      price["normal"] = f"SGD{prices.principles8['weekly'] - prices.weekdayDiscount}"
      price["earlyBird"] = f"SGD{prices.principles8['weekly'] - prices.weekdayDiscount - prices.earlyBirdDiscount}"
    elif courseType == 'Holiday Camp':
      price["normal"] = f"SGD{prices.principles8['camp']}"
      price["earlyBird"] = f"SGD{prices.principles8['camp'] - prices.earlyBirdDiscount}"

  elif courseName == 'Principles X':
    if courseType == 'Weekend Weekly':
      price["normal"] = f"SGD{prices.principlesX['weekly']}"
      price["earlyBird"] = f"SGD{prices.principlesX['weekly'] - prices.earlyBirdDiscount}"
    elif courseType == 'Weekday Weekly':
      price["normal"] = f"SGD{prices.principlesX['weekly'] - prices.weekdayDiscount}"
      price["earlyBird"] = f"SGD{prices.principlesX['weekly'] - prices.weekdayDiscount - prices.earlyBirdDiscount}"
    elif courseType == 'Holiday Camp':
      price["normal"] = f"SGD{prices.principlesX['camp']}"
      price["earlyBird"] = f"SGD{prices.principlesX['camp'] - prices.earlyBirdDiscount}"

  return price
