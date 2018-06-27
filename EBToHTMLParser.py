from dateutil.parser import parse

def EBToHTMLParser(data):
  courseName = ' '.join(data["name"]["text"].split(' ')[0:2])
  courseLocation = 'Marine Parade' if ('@MP' in data["name"]["text"].split(' ')[2:3]) else 'Bukit Timah'
  courseID = data["id"]
  courseURL = data["url"]
  courseStartMonth = parse(data["start"]["local"]).month
  courseStartDay = parse(data["start"]["local"]).day
  courseEndMonth = parse(data["end"]["local"]).month
  courseEndDay = parse(data["end"]["local"]).day
  courseStartTime = parse(data["start"]["local"]).strftime('%I:%M%p').lstrip('0').lower()
  courseEndTime = parse(data["end"]["local"]).strftime('%I:%M%p').lstrip('0').lower()

  print(courseLocation)