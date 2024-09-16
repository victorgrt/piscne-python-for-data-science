# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vgoret <vgoret@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/11 16:07:41 by vgoret            #+#    #+#              #
#    Updated: 2024/09/12 15:34:43 by vgoret           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from time import time

time_since = time.time()
minutes_since = int(time_since / 60)
# print(minutes_since)
hour_since = int(minutes_since / 60)
# print(hour_since)
day_since = int(hour_since / 24)
# print(day_since)
year_since = int(day_since / 365)
# print(year_since)
print("Il s'est ecoule environ\033[92m", time_since, "\033[0msecondes depuis 1970, soit\033[92m", year_since, "\033[0mans !")

time_struct = time.localtime()
#time.struct_time(tm_year=2024, tm_mon=9, 
#tm_mday=10, tm_hour=16, tm_min=37, tm_sec=4, tm_wday=1, tm_yday=254, tm_isdst=1)


# DICTIONNARY FOR EACH MONTHS
str_month = { 1 : "Jan",
		2 : "Feb",
		3 : "Mar",
		4 : "Apr",
		5 : "May",
		6 : "Jun",
		7 : "Jul",
		8 : "Aug",
		9 : "Sep",
		10 : "Oct",
		11 : "Nov",
		12 : "Dec",
}

# PRINTING MONTHS
# for i in str_month :
# 	print(str_month[i])

month = time_struct[1]

day = time_struct[2]

year = time_struct[0]

print(str_month[month], day, year)