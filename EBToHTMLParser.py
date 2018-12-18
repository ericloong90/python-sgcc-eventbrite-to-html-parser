from dateutil.parser import *
from dateutil.rrule import *
from datetime import *
from utility import *

def EBToHTMLParser(data, holidaysDateString):
  courseName = ' '.join(data["name"]["text"].split(' ')[0:2])
  courseLocation = 'Marine Parade' if ('@MP' in data["name"]["text"].split(' ')) else 'Bukit Timah'
  courseID = data["id"]
  courseURL = data["url"]
  courseStartDateTimeObject = parse(data["start"]["local"])
  cleanCourseStartDateTimeObject = datetime.combine(courseStartDateTimeObject.date(), courseStartDateTimeObject.min.timetz())
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
  coursePrice = coursePriceGenerator(courseName, courseType)
  coursePriceNormal = coursePrice["normal"]
  coursePriceEarlyBird = coursePrice["earlyBird"]

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
      <b>{}</b>
      <br>Early Bird*: {}
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

  fundamentals1WeeklyTemplateString = """

  <!-- Fundamentals 1 Weekly Card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="weekly-schedule">{}</div>2hrs x 8 {}:
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
      <b>{}</b>
      <br>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Fundamentals 1 Weekly Card -->

  """

  fundamentals2WeeklyTemplateString = """

  <!-- Fundamentals 2 Weekly Card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="weekly-schedule">{} ({})</div>2hrs x 8 {}:
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
      <b>{}</b>
      <br>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Fundamentals 2 Weekly Card -->

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
      <b>{}</b>
      <br>Early Bird*: {}
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

  basics1WeeklyTemplateString = """

  <!-- Basics 1 Weekly Card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="weekly-schedule">{}</div>2hrs x 5 {}:
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
      <b>{}</b>
      <br>Early Bird*: {}
      <br>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
      <small class="course-card-clause">*at least 14 days before the first class</small>
    </div>
  </div>
  <!-- End of Basics 1 Weekly Card -->

  """

  basics2HolidayCampTemplateString = """

  <!-- Basics 2 Holiday Camp card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="holiday-schedule">Holiday Camp ({})</div>4hrs x 4 Weekdays:
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
      <b>{}</b>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Basics 2 Holiday Camp card -->

  """

  basics2WeeklyTemplateString = """

  <!-- Basics 2 Weekly Card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="weekly-schedule">{} ({})</div>2hrs x 8 {}:
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
      <b>{}</b>
      <br>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Basics 2 Weekly Card -->

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
      <b>{}</b>
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

  basics3WeeklyTemplateString = """

  <!-- Basics 3 Weekend Weekly Card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="weekly-schedule">{}</div>2hrs x 5 {}:
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
      <b>{}</b>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Basics 3 Weekend Weekly Card -->

  """

  basics4HolidayCampTemplateString = """

  <!-- Basics 4 Holiday Camp card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="holiday-schedule">Holiday Camp ({})</div>4hrs x 4 Weekdays:
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
      <b>{}</b>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Basics 4 Holiday Camp card -->

  """

  basics4WeeklyTemplateString = """

  <!-- Basics 4 Weekly Card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="weekly-schedule">{} ({})</div>2hrs x 8 {}:
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
      <b>{}</b>
      <br>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Basics 4 Weekly Card -->

  """

  basics5HolidayCampTemplateString = """

  <!-- Basics 5 Holiday Camp card 1/2 -->
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
      <b>{}</b>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Basics 5 Holiday Camp card 1/2 -->

  <!-- Basics 5 Holiday Camp card - 2/2 -->
  <tr class="boc5">
    <th scope="row">{} - {}
      <br>{} {} - {} {}
      <br>
      <div class="schedule-time">{} - {}</div>
    </th>
    <td>
      <a href="/courses/boc5/index.html">Basics 5</a>
    </td>
    <td>
      <a href="#contact" class="enrol-block-text-holidaycamps">{}</a>
    </td>
    <td>11 - 12</td>
    <th class="visible-sm visible-md visible-lg">
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style-v2 btn-apply btn-hc-signup'>Sign Up</a>
      <a href="/courses/boc5/index.html" target='_blank' rel="noopener" class='btn btn-info btn-style-v2 btn-foc btn-hc-desc'>Course Description</a>
    </th>
  </tr>
  <!-- End of Basics 5 Holiday Camp card - 2/2 -->

  """

  basics5WeeklyTemplateString = """

  <!-- Basics 5 Weekly Card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="weekly-schedule">{}</div>2hrs x 8 {}:
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
      <b>{}</b>
      <br>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Basics 5 Weekly Card -->

  """

  basics6WeeklyTemplateString = """

  <!-- Basics 6 Weekend Weekly Card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="weekly-schedule">{} ({})</div>2hrs x 8 {}:
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
      <b>{}</b>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Basics 6 Weekend Weekly Card -->

  """

  principles1HolidayCampTemplateString = """

  <!-- Principles 1 Holiday Camp card - 1/2 -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="holiday-schedule">Holiday Camp</div>{}hrs x {} Weekdays:
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
      <b>{}</b>
      <br>Early Bird*: {}
      <br>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
      <br>
      <small class="course-card-clause">*at least 14 days before the first class</small>
    </div>
  </div>
  <!-- End of Principles 1 Holiday Camp card - 1/2 -->

  <!-- Principles 1 Holiday Camp card - 2/2-->
  <tr class="poc1">
    <th scope="row">{} - {}
      <br>{} {} - {} {}
      <br>
      <div class="schedule-time">{} - {}</div>
    </th>
    <td>
      <a href="/courses/poc1/index.html">Principles 1</a>
    </td>
    <td>
      <a href="#contact" class="enrol-block-text-holidaycamps">{}</a>
    </td>
    <td>13 - 18</td>
    <th class="visible-sm visible-md visible-lg">
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style-v2 btn-apply btn-hc-signup'>Sign Up</a>
      <a href="/courses/poc1/index.html" target='_blank' rel="noopener" class='btn btn-info btn-style-v2 btn-foc btn-hc-desc'>Course Description</a>
    </th>
  </tr>
  <!-- End of Principles 1 Holiday Camp card - 2/2 -->
  
  """

  principles1WeeklyTemplateString = """

  <!-- Principles 1 Weekly Card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="weekly-schedule">{}</div>2hrs x 5 {}:
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
      <b>{}</b>
      <br>Early Bird*: {}
      <br>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
      <small class="course-card-clause">*at least 14 days before the first class</small>
    </div>
  </div>
  <!-- End of Principles 1 Weekly Card -->

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
      <b>{}</b>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Principles 2 Holiday Camp card -->

  """

  principles2WeeklyTemplateString = """

  <!-- Principles 2 Weekend Weekly Card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="weekly-schedule">{}</div>2hrs x 8 {}:
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
      <b>{}</b>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Principles 2 Weekend Weekly Card -->

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
      <b>{}</b>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Principles 3 Holiday Camp card -->

  """

  principles3WeeklyTemplateString = """

  <!-- Principles 3 Weekend Weekly Card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="weekly-schedule">{} {}</div>2hrs x {} {}:
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
      <b>{}</b>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Principles 3 Weekend Weekly Card -->

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
      <b>{}</b>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Principles 4 Holiday Camp card -->

  """

  principles4WeeklyTemplateString = """

  <!-- Principles 4 Weekend Weekly Card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="weekly-schedule">{}</div>2hrs x 8 {}:
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
      <b>{}</b>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Principles 4 Weekend Weekly Card -->

  """

  principles5HolidayCampTemplateString = """

  <!-- Principles 5 Holiday Camp card -->
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
      <b>{}</b>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Principles 5 Holiday Camp card -->

  """

  principles5WeeklyTemplateString = """

  <!-- Principles 5 Weekend Weekly Card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="weekly-schedule">{}</div>2hrs x 8 {}:
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
      <b>{}</b>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Principles 5 Weekend Weekly Card -->

  """

  principles6WeeklyTemplateString = """

  <!-- Principles 6 Weekend Weekly Card -->
  <div class="flexWrap sessionCard">
    <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 flexWrap">
      <div class="row col-xs-5 col-sm-5 col-md-5 col-lg-4 enrol-block enrol-date">
        <b>{} - {}</b>
      </div>
      <div class="col-xs-7 col-sm-7 co-md-7 col-lg-8 enrol-block">
        <div class="weekly-schedule">{}</div>2hrs x 8 {}:
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
      <b>{}</b>
      <a href='{}' target='_blank' rel="noopener"
        class='btn btn-danger btn-style btn-apply'>Sign Up</a>
    </div>
  </div>
  <!-- End of Principles 6 Weekend Weekly Card -->

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
      <b>{}</b>
      <br>Early Bird*: {}
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
    set = rruleset()
    set.rrule(rrule(DAILY, interval=1, until=parse(data["end"]["local"]),dtstart=cleanCourseStartDateTimeObject))

    for day in holidaysDateString.split(' '):
      set.exdate(parse(day, dayfirst=True))

    listAllEventDays = list(set)
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

    if courseName == 'FUNdamentals 1':
      finalHTMLString = fundamentals1HolidayCampTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, daysString, courseLocation, coursePriceNormal, coursePriceEarlyBird, courseURL, courseStartDayOfTheWeek, courseEndDayOfTheWeek, courseStartDay, intToMonthParser(courseStartMonth), courseEndDay, intToMonthParser(courseEndMonth), courseStartTime, courseEndTime, courseLocation, courseURL)

      return finalHTMLString

    elif courseName == 'Basics 1':
      finalHTMLString = basics1HolidayCampTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, daysString, courseLocation, coursePriceNormal, coursePriceEarlyBird, courseURL, courseStartDayOfTheWeek, courseEndDayOfTheWeek, courseStartDay, intToMonthParser(courseStartMonth), courseEndDay, intToMonthParser(courseEndMonth), courseStartTime, courseEndTime, courseLocation, coursePriceNormal, coursePriceEarlyBird, courseURL)

      return finalHTMLString

    elif courseName in ['Basics 2R', 'Basics 2G', 'Basics 2B']:
      finalHTMLString = basics2HolidayCampTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, courseName, daysString, courseLocation, coursePriceNormal, courseURL)

      return finalHTMLString

    elif courseName == 'Basics 3':
      finalHTMLString = basics3HolidayCampTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, daysString, courseLocation, coursePriceNormal, courseURL, courseStartDayOfTheWeek, courseEndDayOfTheWeek, courseStartDay, intToMonthParser(courseStartMonth), courseEndDay, intToMonthParser(courseEndMonth), courseStartTime, courseEndTime, courseLocation, courseURL)

      return finalHTMLString

    elif courseName in ['Basics 4R', 'Basics 4G', 'Basics 4B']:
      finalHTMLString = basics4HolidayCampTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, courseName, daysString, courseLocation, coursePriceNormal, courseURL)

      return finalHTMLString

    elif courseName == 'Basics 5':
      finalHTMLString = basics5HolidayCampTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, daysString, courseLocation, coursePriceNormal, courseURL, courseStartDayOfTheWeek, courseEndDayOfTheWeek, courseStartDay, intToMonthParser(courseStartMonth), courseEndDay, intToMonthParser(courseEndMonth), courseStartTime, courseEndTime, courseLocation, courseURL)

      return finalHTMLString

    elif courseName == 'Java 1':
      finalHTMLString = academics1HolidayCampTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, daysString, courseLocation, coursePriceNormal, coursePriceEarlyBird, courseURL, courseStartDayOfTheWeek, courseEndDayOfTheWeek, courseStartDay, intToMonthParser(courseStartMonth), courseEndDay, intToMonthParser(courseEndMonth), courseStartTime, courseEndTime, courseLocation, courseURL)

      return finalHTMLString

    elif courseName == 'Principles 1':
      finalHTMLString = principles1HolidayCampTemplateString[:]

      if (courseEndDay - courseStartDay) == 3:
        hoursPerLesson = 2.5
        numberOfCourseDays = len(listAllEventDays)
      else:
        hoursPerLesson = 2
        numberOfCourseDays = len(listAllEventDays)

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, hoursPerLesson, numberOfCourseDays, daysString, courseLocation, coursePriceNormal, coursePriceEarlyBird, courseURL, courseStartDayOfTheWeek, courseEndDayOfTheWeek, courseStartDay, intToMonthParser(courseStartMonth), courseEndDay, intToMonthParser(courseEndMonth), courseStartTime, courseEndTime, courseLocation, courseURL)

      return finalHTMLString

    elif courseName == 'Principles 2':
      finalHTMLString = principles2HolidayCampTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, daysString, courseLocation, coursePriceNormal, courseURL)

      return finalHTMLString

    elif courseName == 'Principles 3':
      finalHTMLString = principles3HolidayCampTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, daysString, courseLocation, coursePriceNormal, courseURL)

      return finalHTMLString

    elif courseName == 'Principles 4':
      finalHTMLString = principles4HolidayCampTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, daysString, courseLocation, coursePriceNormal, courseURL)

      return finalHTMLString

    elif courseName == 'Principles 5':
      finalHTMLString = principles5HolidayCampTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, daysString, courseLocation, coursePriceNormal, courseURL)

      return finalHTMLString
    
    else:
      return 'Event name not found, please check {}'.format(courseName)

  else:
    # This part parses the weekly events
    day = parse(data["start"]["local"]).weekday()
    courseDay = intToFullDayOfTheWeek(day)
    set = rruleset()
    set.rrule(rrule(DAILY, interval=7, until=parse(data["end"]["local"]),dtstart=cleanCourseStartDateTimeObject))

    for day in holidaysDateString.split(' '):
      set.exdate(parse(day, dayfirst=True))

    listAllEventDays = list(set)
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

    if courseName == 'FUNdamentals 1':
      finalHTMLString = fundamentals1WeeklyTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, courseType, courseDay, daysString, courseLocation, coursePriceNormal, courseURL)

      return finalHTMLString

    elif courseName in ['FUNdamentals 2R', 'FUNdamentals 2G', 'FUNdamentals 2B']:
      finalHTMLString = fundamentals2WeeklyTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, courseType, courseName, courseDay, daysString, courseLocation, coursePriceNormal, courseURL)

      return finalHTMLString

    elif courseName == 'Basics 1':
      finalHTMLString = basics1WeeklyTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, courseType, courseDay, daysString, courseLocation, coursePriceNormal, coursePriceEarlyBird, courseURL)

      return finalHTMLString

    elif courseName in ['Basics 2R', 'Basics 2G', 'Basics 2B']:
      finalHTMLString = basics2WeeklyTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, courseType, courseName, courseDay, daysString, courseLocation, coursePriceNormal, courseURL)

      return finalHTMLString

    elif courseName == 'Basics 3':
      finalHTMLString = basics3WeeklyTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, courseType, courseDay, daysString, courseLocation, coursePriceNormal, courseURL)

      return finalHTMLString

    elif courseName in ['Basics 4R', 'Basics 4G', 'Basics 4B']:
      finalHTMLString = basics4WeeklyTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, courseType, courseName, courseDay, daysString, courseLocation, coursePriceNormal, courseURL)

      return finalHTMLString

    elif courseName == 'Basics 5':
      finalHTMLString = basics5WeeklyTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, courseType, courseDay, daysString, courseLocation, coursePriceNormal, courseURL)

      return finalHTMLString

    elif courseName in ['Basics 6R', 'Basics 6G', 'Basics 6B']:
      finalHTMLString = basics6WeeklyTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, courseType, courseName, courseDay, daysString, courseLocation, coursePriceNormal, courseURL)

      return finalHTMLString

    elif courseName == 'Principles 1':
      finalHTMLString = principles1WeeklyTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, courseType, courseDay, daysString, courseLocation, coursePriceNormal, coursePriceEarlyBird, courseURL)

      return finalHTMLString

    elif courseName == 'Principles 2':
      finalHTMLString = principles2WeeklyTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, courseType, courseDay, daysString, courseLocation, coursePriceNormal, courseURL)

      return finalHTMLString

    elif courseName in ['Principles 3', 'Principles 3R', 'Principles 3G', 'Principles 3B']:
      finalHTMLString = principles3WeeklyTemplateString[:]

      if courseName == 'Principles 3':
        courseNumberOfLessons = 8
      else:
        courseNumberOfLessons = 4

      if courseName == 'Principles 3':
        courseName3RGB = ''
      else:
        courseName3RGB = '({})'.format(courseName)

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, courseType, courseName3RGB, courseNumberOfLessons, courseDay, daysString, courseLocation, coursePriceNormal, courseURL)

      return finalHTMLString

    elif courseName == 'Principles 4':
      finalHTMLString = principles4WeeklyTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, courseType, courseDay, daysString, courseLocation, coursePriceNormal, courseURL)

      return finalHTMLString

    elif courseName == 'Principles 5':
      finalHTMLString = principles5WeeklyTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, courseType, courseDay, daysString, courseLocation, coursePriceNormal, courseURL)

      return finalHTMLString

    elif courseName == 'Principles 6':
      finalHTMLString = principles6WeeklyTemplateString[:]

      finalHTMLString = finalHTMLString.format(courseStartTime, courseEndTime, courseType, courseDay, daysString, courseLocation, coursePriceNormal, courseURL)

      return finalHTMLString