"""
* @Author: Samarth BM.
* @Date: 2021-09-10 22:03  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-10 22:03   
* @Title: :To find the wind chill using temperature and wind speed.
"""

import math as m

def wind_chill():

    """
    Description:
        This function is used to find the wind chill.
        Temperature and wind speed are the two inputs given.
        To find the wind chill temperature should not be greater than 50,
        and wind speed should be in between 3-120.

    """    

    temperature = float(input("Enter temperature in fahrenheit in between the range 0 to 50: "))
    wind_speed = float(input( "Enter wind speed in between the range 3 to 120: "))

    if(temperature > 50 or wind_speed < 3 or wind_speed > 120):
        print("Wind chill cannot be found for the entered condition")

    else:
        windChill = 35.74 + 0.6215 * temperature +(0.4275*temperature + 35.75)*m.pow(wind_speed,0.16)
        print("Wind chil for the given temperature and wind speed is: ",windChill)

if __name__ == "__main__":
    wind_chill()    