def isLeapYear(year):
  if(year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    return True
  else:
    return false
year = int(input("Enter a year:"))
if isleapyear(year):
  print ('{} is a Leap Year.'.format(year))
else:
  print('{} is a Leap Year.'.format(year))
