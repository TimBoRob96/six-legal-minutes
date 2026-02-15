import ui
import math
import datetime

def roundDown6(dt):
	dt = dt.replace(second=0, microsecond=0)
	minutes = dt.hour * 60 + dt.minute
	rounded = math.floor(minutes / 6) * 6
	return dt.replace(hour=0, minute=0) + datetime.timedelta(minutes=rounded)

def roundUp6(dt):
	dt = dt.replace(second=0, microsecond=0)
	minutes = dt.hour * 60 + dt.minute
	rounded = math.ceil(minutes / 6) * 6
	return dt.replace(hour=0, minute=0) + datetime.timedelta(minutes=rounded)
	
def calc(sender):
	startTimePick = sender.superview['startPicker']
	endTimePick = sender.superview['endPicker']
	startTimeResult = sender.superview['startResultLabel']
	endTimeResult = sender.superview['endResultLabel']
	totalResult = sender.superview['totalResult']
	totalMinResult = sender.superview['totalMinResult']
	
	endTimeRounded = roundUp6(endTimePick.date)
	startTimeRounded = roundDown6(startTimePick.date)
	
	print(startTimeRounded)
	print(endTimeRounded)
	startTimeResult.text = startTimeRounded.strftime("%H:%M")
	endTimeResult.text = endTimeRounded.strftime("%H:%M")
	
	print(endTimeRounded - startTimeRounded)
	totalResult.text = str(endTimeRounded - startTimeRounded)
	totalMinResult.text = str(int((endTimeRounded - startTimeRounded).total_seconds() / 60))

v = ui.load_view()


	
v.present('sheet')


