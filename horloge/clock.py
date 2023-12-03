import time
import sys

def print_clock():
    try:
        while True:
            # Get current time
            current_time = time.localtime()
            hours = current_time.tm_hour
            minutes = current_time.tm_min
            seconds = current_time.tm_sec

            # Format the time
            formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

            # Get current date
            month = current_time.tm_mon
            day = current_time.tm_mday
            year = current_time.tm_year

            # Format the date
            formatted_date = f"{month:02d}/{day:02d}/{year}"

            # Print the clock and date on the same line, move cursor to the beginning
            sys.stdout.write("\r" + formatted_time + " // " + formatted_date)
            sys.stdout.flush()

            # Wait for 1 second
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nClock stopped.")

if __name__ == "__main__":
    print_clock()

