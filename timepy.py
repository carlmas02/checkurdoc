from datetime import datetime
from datetime import date

def get_time():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	
	today = date.today()

	return current_time,today



