from dateutil.parser import parse

def EBToHTMLParser(data):
  courseName = ' '.join(data["name"]["text"].split(' ')[0:2])
  courseLocation = 'Marine Parade' if ('@MP' in data["name"]["text"].split(' ')) else 'Bukit Timah'
  courseID = data["id"]
  courseURL = data["url"]
  courseStartMonth = parse(data["start"]["local"]).month
  courseStartDay = parse(data["start"]["local"]).day
  courseEndMonth = parse(data["end"]["local"]).month
  courseEndDay = parse(data["end"]["local"]).day
  courseStartTime = parse(data["start"]["local"]).strftime('%I:%M%p').lstrip('0').lower()
  courseEndTime = parse(data["end"]["local"]).strftime('%I:%M%p').lstrip('0').lower()
  courseType = 'Holiday Camp' if ('Camp' in data["name"]["text"].split(' ')) else ('Weekend Weekly' if (('Weekly' in data["name"]["text"].split(' ')) and (parse(data["start"]["local"]).weekday() == 5 or parse(data["start"]["local"]).weekday() == 6)) else 'Weekday Weekly')
  courseDay = parse(data["start"]["local"]).weekday()

  if courseType == 'Holiday Camp':
    courseDay = 'Weekdays'
  else:
    day = parse(data["start"]["local"]).weekday()

    if day == 0:
      courseDay = 'Mondays'
    elif day == 1:
      courseDay = 'Tuesdays'
    elif day == 2:
      courseDay = 'Wednesdays'
    elif day == 3:
      courseDay = 'Thursdays'
    elif day == 4:
      courseDay = 'Fridays'
    elif day == 5:
      courseDay = 'Saturdays'
    elif day == 6:
      courseDay = 'Sundays'


  print(courseDay)