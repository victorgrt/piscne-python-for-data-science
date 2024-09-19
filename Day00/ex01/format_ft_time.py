import time

time_since = time.time()
minutes_since = int(time_since / 60)
hour_since = int(minutes_since / 60)
day_since = int(hour_since / 24)
year_since = int(day_since / 365)
print("Il s'est ecoule environ\033[92m", time_since,
      "\033[0msecondes depuis 1970, soit\033[92m", year_since, "\033[0mans !")

time_struct = time.localtime()

# DICTIONNARY FOR EACH MONTHS
str_month = {1: "Jan",
             2: "Feb",
             3: "Mar",
             4: "Apr",
             5: "May",
             6: "Jun",
             7: "Jul",
             8: "Aug",
             9: "Sep",
             10: "Oct",
             11: "Nov",
             12: "Dec"
             }

# PRINTING MONTHS
# for i in str_month :
# 	print(str_month[i])

month = time_struct[1]

day = time_struct[2]

year = time_struct[0]

print(str_month[month], day, year)
