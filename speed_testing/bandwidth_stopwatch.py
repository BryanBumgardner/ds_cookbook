# python 3.5
import pyspeedtest # sudo pip install pyspeedtest
import csv
import time
from time import localtime, strftime

header = ['Date and time', 'Download speed', 'Ping', 'Upload speed']

def loop_of_speed_tests(csvfile):

    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header)

    print("To end the program, simply close the Terminal window, or type Control + C. The data will be recorded in the Bandwidth_Stopwatch_data.csv in the same directory as this script.")

    while True:
        current_time = localtime()

        st = pyspeedtest.SpeedTest()

        try:
            download = st.download(),
            ping = st.ping(),
            upload = st.upload()
        except Exception as e:
            print(f'Exception encountered while attempting to record at {current_time} with message {e}')
            continue

        date_time = strftime("%Y-%m-%d %H:%M:%S", current_time)
        csv_writer.writerow([date_time, download, ping, upload])
        csvfile.flush()

        print("Speed data recorded: " + strftime("%Y-%m-%d %H:%M:%S", current_time))
        time.sleep(120) #two minute wait between pulls.

with open("Bandwidth_Stopwatch_data.csv", 'w') as csvfile:
    loop_of_speed_tests(csvfile)
