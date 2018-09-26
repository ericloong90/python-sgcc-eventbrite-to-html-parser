from dateutil.parser import *
from dateutil.rrule import *
from datetime import *
from utility import *

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

  finalHTMLString = 'hello'

  basics1HolidayCampTemplateString = """

  <!-- Basics 1 Holiday Camp card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="holiday-schedule">Holiday Camp</div>2hrs x 5 Weekdays:
        <br>
        <span class="hlHint">
          <b>
            {}
          </b>
        </span>
      </div>
      <div class="col-xs-4 col-sm-4 col-md-3 enrol-block">
        <b class="enrol-block-location">Location</b>
      </div>
      <div class="col-xs-8 col-sm-8 col-md-9 enrol-block">
        <a href="#contact" class="enrol-block-text">{} Campus</a>
      </div>
    </div>
    <div class="col-xs-12 col-sm-12 col-md-4 col-lg-3 text-center enrol-block enrol-price">
      <b>SGD455</b>
      <br>Early Bird*: SGD430
      <br>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
      <br>
      <small class="course-card-clause">*at least 14 days before the first class</small>
    </div>
  </div>
  <!-- End of Basics 1 Holiday Camp card -->

  """

  if courseType == 'Holiday Camp':
    courseDay = 'Weekdays'

    if courseName == 'Basics 1':
      finalHTMLString = basics1HolidayCampTemplateString[:]
      listAllEventDays = list(rrule(DAILY, interval=1, count=5, dtstart=parse(data["start"]["local"])))
      daysString = intToMonthParser(courseStartMonth)
      currentMonth = courseStartMonth

      for date in listAllEventDays:
        if date.month == currentMonth:
          daysString += ' {},'.format(date.day)
        elif date.month != currentMonth:
          currentMonth = date.month
          daysString = daysString[:-1]
          daysString += '<br>{} {},'.format(intToMonthParser(date.month), date.day)
      
      daysString = daysString[:-1]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, daysString, courseLocation, courseURL)

      return finalHTMLString

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
