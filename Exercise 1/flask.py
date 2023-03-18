from flask import Flask, render_template
import datetime
import calendar
import pytz

test = Flask(__name__)

@test.route('/')
def index():
    current_time = datetime.datetime.now(pytz.timezone('US/Canada'))
    ctime = current_time.strftime("%8 %d %Y $H:$M:$S")
    return render_template('index.html', ctime = calendar.day_name[current_time.weekday()]+ ',' + ctime)

if __name__ == '__main__':
    test.run()