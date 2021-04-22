def add_time(start, duration,days=None):
  #Declarations of the variables
  new_time = "" #Variable of return

  #Variables of 
  indexOfStart       = start.find(":")
  indexOfDuration    = duration.find(":")


  listOfStartHour       = int(start[:indexOfStart])#11
  listOfStartMinutes    = int(start[indexOfStart+1:5])#6 
  
  listOfDurationHour    = int(duration[:indexOfDuration])#Las horas 2
  listOfDurationMinutes = int(duration[indexOfDuration+1:])#Los minutos 2

  intTotalOfMinutes = 0
  intTotalOfHour    = 0
  intTotalOfDays    = 0

  if start.find("A") != -1:
    strOfDayNight = "AM"
  else:
    strOfDayNight = "PM"  
  #End of the Declarations

  #Start the calculation of total of hour and determine the moment of the day
  
  intTotalOfMinutes = listOfStartMinutes + listOfDurationMinutes
  if intTotalOfMinutes >= 60:
    intTotalOfMinutes -= 60
    intTotalOfHour    += 1
    
  if listOfStartHour + intTotalOfHour == 12 and strOfDayNight == "PM":
    intTotalOfDays = 1
    strOfDayNight = "AM"
  
  intTotalOfHour += listOfStartHour + listOfDurationHour #35
  while intTotalOfHour > 24:
    intTotalOfHour -= 24
    intTotalOfDays += 1
    
  if intTotalOfHour > 12 and strOfDayNight == "PM":
    intTotalOfDays +=1
    
  if strOfDayNight == "AM" and intTotalOfDays == 0:
    if intTotalOfHour > 12:
      intTotalOfHour -= 12
      strOfDayNight = "PM"
    elif intTotalOfHour == 12:
      strOfDayNight = "PM"
  elif strOfDayNight == "PM":
    if intTotalOfHour < 12 and intTotalOfDays > 1:
      strOfDayNight = "AM"
    elif intTotalOfHour > 12:
      intTotalOfHour -= 12
      strOfDayNight = "AM"
  elif strOfDayNight == "AM" and intTotalOfDays > 1:
    if intTotalOfHour < 12 :
      strOfDayNight = "PM"
    elif intTotalOfHour > 12:
      intTotalOfHour -= 12
      strOfDayNight = "PM"
  
  if indexOfStart == 2 and indexOfDuration != 1:
    if intTotalOfHour < 10 :
      new_time = "0"+ str(intTotalOfHour)
    else:   
      new_time = str(intTotalOfHour)

    new_time += ":"

    if intTotalOfMinutes < 10:
      new_time += "0"+ str(intTotalOfMinutes)
    else:
      new_time += str(intTotalOfMinutes)
    new_time += " " + strOfDayNight
  else:
    new_time = str(intTotalOfHour)
    
    new_time += ":"

    if intTotalOfMinutes < 10:
      new_time += "0"+ str(intTotalOfMinutes)
    else:
      new_time += str(intTotalOfMinutes)
    new_time += " " + strOfDayNight
  #End the conversion

  #Start to showing the days of the week
  week = {
    "Monday" : 1,
    "Tuesday" : 2,
    "Wednesday" : 3,
    "Thursday" : 4,
    "Friday" : 5,
    "Saturday" : 6,
    "Sunday" : 7,
    1 : "Monday",
    2 : "Tuesday" ,
    3 : "Wednesday",
    4 : "Thursday",
    5 : "Friday",
    6 : "Saturday",
    7 : "Sunday"
  }

  intCountDays = 0
  
  if days == None:   
    if intTotalOfDays == 1:
      new_time += " (next day)" 
    elif intTotalOfDays > 1:
      new_time += " (" + str(intTotalOfDays) + " days later)"
  else:
    days = days.capitalize()
    intCountDays = week.get(days) + intTotalOfDays
    while intCountDays > 7:
      intCountDays -= 7
    new_time += ", " + week.get(intCountDays)
    if intTotalOfDays == 1:
      new_time += " (next day)" 
    elif intTotalOfDays > 1:
      new_time += " (" + str(intTotalOfDays) + " days later)"
  
  #End of showing
  return new_time