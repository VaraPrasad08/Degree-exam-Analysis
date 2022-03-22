import datetime
from fastapi import FastAPI
app=FastAPI()
# Function to convert string to datetime
@app.get("/")
def convert(date_time):
    format = '%b %d %Y %I:%M%p' # The format
    datetime_str = datetime.datetime.strptime(date_time, format)
   
    return datetime_str
   
# Driver code
date_time = 'Dec 4 2018 10:07AM'
print(convert(date_time))
