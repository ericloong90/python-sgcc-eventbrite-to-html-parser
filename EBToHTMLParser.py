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
  courseStartDayOfTheWeek = intToDayOfTheWeek(parse(data["start"]["local"]).weekday())
  courseEndMonth = parse(data["end"]["local"]).month
  courseEndDay = parse(data["end"]["local"]).day
  courseEndDayOfTheWeek = intToDayOfTheWeek(parse(data["end"]["local"]).weekday())
  courseStartTime = parse(data["start"]["local"]).strftime('%I:%M%p').lstrip('0').lower()
  courseEndTime = parse(data["end"]["local"]).strftime('%I:%M%p').lstrip('0').lower()
  courseType = 'Holiday Camp' if ('Camp' in data["name"]["text"].split(' ')) else ('Weekend Weekly' if (('Weekly' in data["name"]["text"].split(' ')) and (parse(data["start"]["local"]).weekday() == 5 or parse(data["start"]["local"]).weekday() == 6)) else 'Weekday Weekly')
  courseDay = parse(data["start"]["local"]).weekday()

  finalHTMLString = 'hello'

  fundamentals1HolidayCampTemplateString = """

  <!-- FUNdamentals 1 Holiday Camp card - 1/2 -->
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
      <b>SGD395</b>
      <br>Early Bird*: SGD370
      <br>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
      <br>
      <small class="course-card-clause">*at least 14 days before the first class</small>
    </div>
  </div>
  <!-- End of FUNdamentals 1 Holiday Camp card - 1/2 -->

  <!-- FUNdamentals 1 Holiday Camp card - 2/2-->
  <tr class="fun1">
    <th scope="row">{} - {}
      <br>{} {} - {} {}
      <br>
      <div class="schedule-time">{} - {}</div>
    </th>
    <td>
      <a href="/courses/fundamentals1/index.html">FUNdamentals 1</a>
    </td>
    <td>
      <a href="#contact" class="enrol-block-text-holidaycamps">{}</a>
    </td>
    <td>7-8</td>
    <th class="visible-sm visible-md visible-lg">
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style-v2 btn-apply btn-hc-signup'>Sign Up</a>
      <a href="/courses/fundamentals1/index.html" target='_blank' rel="noopener" class='btn btn-info btn-style-v2 btn-foc btn-hc-desc'>Course Description</a>
    </th>
  </tr>
  <!-- End of FUNdamentals 1 Holiday Camp card - 2/2 -->
  """

  basics1HolidayCampTemplateString = """

  <!-- Basics 1 Holiday Camp card - 1/2 -->
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
  <!-- End of Basics 1 Holiday Camp card - 1/2 -->

  <!-- Basics 1 Holiday Camp card - 2/2-->
  <tr class="boc1">
    <th scope="row">{} - {}
      <br>{} {} - {} {}
      <br>
      <div class="schedule-time">{} - {}</div>
    </th>
    <td>
      <a href="/courses/boc1/index.html">Basics 1</a>
    </td>
    <td>
      <a href="#contact" class="enrol-block-text-holidaycamps">{}</a>
    </td>
    <td>9 - 10</td>
    <th class="visible-sm visible-md visible-lg">
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style-v2 btn-apply btn-hc-signup'>Sign Up</a>
      <a href="/courses/boc1/index.html" target='_blank' rel="noopener" class='btn btn-info btn-style-v2 btn-foc btn-hc-desc'>Course Description</a>
    </th>
  </tr>
  <!-- End of Basics 1 Holiday Camp card - 2/2 -->

  """

  basics2HolidayCampTemplateString = """

  <!-- Basics 2 Holiday Camp card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="holiday-schedule">Holiday Camp</div>4hrs x 4 Weekdays:
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
      <b>SGD725</b>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Basics 2 Holiday Camp card -->

  """

  basics3HolidayCampTemplateString = """

  <!-- Basics 3 Holiday Camp card - 1/2 -->
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
      <br>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
      <br>
    </div>
  </div>
  <!-- End of Basics 3 Holiday Camp card - 1/2 -->

  <!-- Basics 3 Holiday Camp card - 2/2 -->
  <tr class="boc3">
    <th scope="row">{} - {}
      <br>{} {} - {} {}
      <br>
      <div class="schedule-time">{} - {}</div>
    </th>
    <td>
      <a href="/courses/boc3/index.html">Basics 3</a>
    </td>
    <td>
      <a href="#contact" class="enrol-block-text-holidaycamps">{}</a>
    </td>
    <td>11 - 12</td>
    <th class="visible-sm visible-md visible-lg">
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style-v2 btn-apply btn-hc-signup'>Sign Up</a>
      <a href="/courses/boc3/index.html" target='_blank' rel="noopener" class='btn btn-info btn-style-v2 btn-foc btn-hc-desc'>Course Description</a>
    </th>
  </tr>
  <!-- End of Basics 3 Holiday Camp card - 2/2 -->

  """

  basics4HolidayCampTemplateString = """

  <!-- Basics 4 Holiday Camp card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="holiday-schedule">Holiday Camp</div>4hrs x 4 Weekdays:
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
      <b>SGD725</b>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Basics 4 Holiday Camp card -->

  """

  principles2HolidayCampTemplateString = """

  <!-- Principles 2 Holiday Camp card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="holiday-schedule">Holiday Camp</div>4hrs x 4 Weekdays:
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
      <b>SGD775</b>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Principles 2 Holiday Camp card -->

  """

  principles3HolidayCampTemplateString = """

  <!-- Principles 3 Holiday Camp card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="holiday-schedule">Holiday Camp</div>4hrs x 4 Weekdays:
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
      <b>SGD880</b>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Principles 3 Holiday Camp card -->

  """

  principles4HolidayCampTemplateString = """

  <!-- Principles 4 Holiday Camp card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="holiday-schedule">Holiday Camp</div>4hrs x 4 Weekdays:
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
      <b>SGD880</b>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Principles 4 Holiday Camp card -->

  """

  academics1HolidayCampTemplateString = """

  <!-- Academics 1 Holiday Camp card - 1/2 -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="holiday-schedule">Holiday Camp</div>4hrs x 4 Weekdays:
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
      <b>SGD790</b>
      <br>Early Bird*: SGD745
      <br>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
      <br>
      <small class="course-card-clause">*at least 14 days before the first class</small>
    </div>
  </div>
  <!-- End of Academics 1 Holiday Camp card - 1/2 -->

  <!-- Academics 1 Holiday Camp card - 2/2 -->
  <tr class="acad1">
    <th scope="row">{} - {}
      <br>{} {} - {} {}
      <br>
      <div class="schedule-time">{} - {}</div>
    </th>
    <td>
      <a href="/courses/academics/index.html">Java 1</a>
    </td>
    <td>
      <a href="#contact" class="enrol-block-text-holidaycamps">{}</a>
    </td>
    <td>15 - 18</td>
    <th class="visible-sm visible-md visible-lg">
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style-v2 btn-apply btn-hc-signup'>Sign Up</a>
      <a href="/courses/academics/index.html" target='_blank' rel="noopener" class='btn btn-info btn-style-v2 btn-foc btn-hc-desc'>Course Description</a>
    </th>
  </tr>
  <!-- End of Academics 1 Holiday Camp card - 2/2 -->

  """

  if courseType == 'Holiday Camp':
    courseDay = 'Weekdays'

    if courseName == 'FUNdamentals 1':
      finalHTMLString = fundamentals1HolidayCampTemplateString[:]
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

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, daysString, courseLocation, courseURL, courseStartDayOfTheWeek, courseEndDayOfTheWeek, courseStartDay, intToMonthParser(courseStartMonth), courseEndDay, intToMonthParser(courseEndMonth), courseStartTime, courseEndTime, courseLocation, courseURL)

      return finalHTMLString

    elif courseName == 'Basics 1':
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

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, daysString, courseLocation, courseURL, courseStartDayOfTheWeek, courseEndDayOfTheWeek, courseStartDay, intToMonthParser(courseStartMonth), courseEndDay, intToMonthParser(courseEndMonth), courseStartTime, courseEndTime, courseLocation, courseURL)

      return finalHTMLString

    elif courseName == 'Basics 2R' or courseName == 'Basics 2G' or courseName == 'Basics 2B':
      finalHTMLString = basics2HolidayCampTemplateString[:]
      listAllEventDays = list(rrule(DAILY, interval=1, count=4, dtstart=parse(data["start"]["local"])))
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

    elif courseName == 'Basics 3':
      finalHTMLString = basics3HolidayCampTemplateString[:]
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

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, daysString, courseLocation, courseURL, courseStartDayOfTheWeek, courseEndDayOfTheWeek, courseStartDay, intToMonthParser(courseStartMonth), courseEndDay, intToMonthParser(courseEndMonth), courseStartTime, courseEndTime, courseLocation, courseURL)

      return finalHTMLString

    elif courseName == 'Basics 4R' or courseName == 'Basics 4G' or courseName == 'Basics 4B':
      finalHTMLString = basics4HolidayCampTemplateString[:]
      listAllEventDays = list(rrule(DAILY, interval=1, count=4, dtstart=parse(data["start"]["local"])))
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

    elif courseName == 'Java 1':
      finalHTMLString = academics1HolidayCampTemplateString[:]
      listAllEventDays = list(rrule(DAILY, interval=1, count=4, dtstart=parse(data["start"]["local"])))
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

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, daysString, courseLocation, courseURL, courseStartDayOfTheWeek, courseEndDayOfTheWeek, courseStartDay, intToMonthParser(courseStartMonth), courseEndDay, intToMonthParser(courseEndMonth), courseStartTime, courseEndTime, courseLocation, courseURL)

      return finalHTMLString

    elif courseName == 'Principles 2':
      finalHTMLString = principles2HolidayCampTemplateString[:]
      listAllEventDays = list(rrule(DAILY, interval=1, count=4, dtstart=parse(data["start"]["local"])))
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

    elif courseName == 'Principles 3':
      finalHTMLString = principles3HolidayCampTemplateString[:]
      listAllEventDays = list(rrule(DAILY, interval=1, count=4, dtstart=parse(data["start"]["local"])))
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

    elif courseName == 'Principles 4':
      finalHTMLString = principles4HolidayCampTemplateString[:]
      listAllEventDays = list(rrule(DAILY, interval=1, count=4, dtstart=parse(data["start"]["local"])))
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
      return 'Event name not found, please check {}'.format(courseName)

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
