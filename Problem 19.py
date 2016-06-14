dayOfWeekIndex = 1
dayCounter = 1
dayArray = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
year = 1900
monthIndex = 0
monthArray = ['January','February','March',
              'April','May','June','July',
              'August','September','October',
              'November','December']
monthDurationArray = [31,28,31,30,31,30,31,31,30,31,30,31]
monthDurationLeapArray = [31,29,31,30,31,30,31,31,30,31,30,31]
resultsSum = 0

def is_leap_year(year):
    if (year/4) == 0:
        #divisible by 4
        if (year/100) == 0:
            #century
            if(year/400) == 0:
                #century Divisible by 400
                return True
            else:
                #century not divisible by 400
                return False
        else:
            #not a century but divisible by 400
            return False
    else:
        return False

while year<2001:
    if is_leap_year(year):
        monthDuration = monthDurationLeapArray[monthIndex]
    else:
        monthDuration = monthDurationArray[monthIndex]

    #check if first of the month
    if year >= 1901:
        if dayCounter == 1:
            #check if day = sunday
            if dayArray[dayOfWeekIndex] == 'Sunday':
                resultsSum = resultsSum + 1
                #year = 1903
                print(dayArray[dayOfWeekIndex], dayOfWeekIndex)
                print(monthIndex+1,'/',dayCounter,'/',year)

    #print(dayArray[dayOfWeekIndex],'  ',monthIndex+1,'/',dayCounter,'/',year)
    #print(dayArray[dayOfWeekIndex])
    #increment day
    dayCounter = dayCounter+1
    dayOfWeekIndex = dayOfWeekIndex + 1
    
    if dayOfWeekIndex > len(dayArray)-1:
        dayOfWeekIndex = 0
        
    if dayCounter > monthDuration:
        #increment to the next month
        dayCounter = 1
        monthIndex = monthIndex + 1
        #print(monthIndex)
        if monthIndex > len(monthArray)-1:
            #increment to the next year
            monthIndex = 0
            year = year+1
    
print (resultsSum)
