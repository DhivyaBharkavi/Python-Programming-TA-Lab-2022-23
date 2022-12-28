"""
Light travels at 3 * 10 8 meters per second.
A light-year is the distance a light beam travel in one year. 
Write a program that calculates and displays the value of a lightyear.
[Light year = speed of light * number of seconds in a year]
"""
#light_speed = 3 * 10^8 milliseconds = 3 * 100000000 m/s // speed of light
light_speed = 300000000 
#total_seconds = 365 * 24 * 60 * 60 // no of days in one year * no of hours in one day * no of minutes in one hour * no of minutes in one seconds = number of seconds in one year 
total_seconds = 365 * 24 * 60 * 60
light_year = light_speed * total_seconds
print("Light year ",light_year,"meters in the year")
