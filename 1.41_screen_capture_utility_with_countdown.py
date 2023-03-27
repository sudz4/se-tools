import os
import time
import schedule
import subprocess
import sys
from datetime import datetime
import time # need this for countdown feature

# screen CAPTURE
def create_screenshots_folder():
    top_folder_path = '/Users/sudz4/Desktop/PROJECTZ/screen_shot_program_logs' # where to save screenshots
    if not os.path.exists(top_folder_path): # check the top folder path
        os.makedirs(top_folder_path) # if no top folder path, creates a new top folder path

    # create daily subfolder
    current_date = datetime.now().strftime('%Y%m%d_%a')
    subfolder_name = f"{current_date}"
    subfolder_path = os.path.join(top_folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)

    # create essential technical library subfolder
    essential_library_name = f"{current_date}_ESSENTIAL_TECHNICAL_LIBRARY" # also could be called a "Core Technical Library (CTL)"
    essential_library_path = os.path.join(subfolder_path, essential_library_name)
    if not os.path.exists(essential_library_path):
        os.makedirs(essential_library_path)
    return subfolder_path

# def take_screenshot(folder_path):
#     countdown(3)  # TOGGLE - COUNTDOWN BEFORE INCOMING SCREEN CAPTURE
#     timestamp = time.strftime("%Y%m%d-%H%M%S")
#     client_name = 'INFOCENTER'
#     screenshot_file = os.path.join(folder_path, f"{timestamp}_{client_name}.png")
#     subprocess.run(["screencapture", "-x", screenshot_file])
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print(f"{client_name} screen capture SAVED AS {screenshot_file} @ {current_time}")

def take_screenshot(folder_path):
    countdown(3) # TOGGLE COUNTDOWN TO INCOMING SCREEN CAPTURE
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    client_name = 'INFOCENTER'
    screenshot_file = os.path.join(folder_path, f"{timestamp}_{client_name}.png")
    subprocess.run(["screencapture", "-x", screenshot_file])
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{client_name} screen capture SAVED AS {screenshot_file} @ {current_time}")
    return True

def countdown(seconds):
    for i in range(seconds, 0, -1):
        sys.stdout.write(f"\r{i}<----headless screen {i} capture incoming---->{i}")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r")  # Clear the line after the countdown is done
    sys.stdout.flush()

def main():
    interval = 10 # TOGGLE THE PERIOD BETWEEN IMAGE CAPTURES
    runtime_in_minutes = 60 # TOGGLE RUNTIME BEFORE AUTO-STOPPING PROGRAM
    end_time = time.time() + runtime_in_minutes * 60 # 60 seconds in a minute

    print(f"Machine screen capture in progress ({interval} second intervals) for {runtime_in_minutes} minutes...")
    print("Press control+c to quit or stop running program") # at any time the user can manually and safely stop the program.
    folder_path = create_screenshots_folder() 
    schedule.every(interval).seconds.do(take_screenshot, folder_path)

    while time.time() < end_time:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # print("\nProgram terminated by user.")
        print()
        print("\nScreen Captures SAVED!")
        print("Thanks for using sCrEeN cApTuRe!") # make this ASCII text think about using ASCII at launch, details on how to use program(s)
        print()

# think about using ASCII at launch, details on how to use program(s)
"""END OF PROGRAM"""
