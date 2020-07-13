import datetime

dt = datetime.datetime.now()
print ('dt = ',dt) 
print ("dt type = ",type(dt))
date_string = dt.strftime('%y-%m-%d')
print ('date_string = ', date_string)
print ('date_string type = ',type(date_string))
