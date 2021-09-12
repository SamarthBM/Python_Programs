"""
* @Author: Samarth BM.
* @Date: 2021-09-12 23:47  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-12 23:47 
* @Title: :To simulate stop watch.
"""

import time

def stop_watch():
    """
    Description:
        This function is used to simulate stop watch.
        When user presses Enter button for the first time,
        time function is used to note the present time.
        Whn user presses Enter for second time, the time interval is printed.

    """    

    # To start the timer.
    input("Press Enter to start the timer")
    initial_time = time.time()

    # To end the timer.
    input("Press Enter to stop the timer")
    final_time = time.time()

    # To get the total elapsed time.
    print("Total elapsed time is: ",final_time-initial_time, " sec ")

if __name__ == "__main__":
    stop_watch()