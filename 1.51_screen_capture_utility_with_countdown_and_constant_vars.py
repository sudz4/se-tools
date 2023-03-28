import os
import time
import schedule
import subprocess
import sys
from datetime import datetime
import time # need this for countdown feature

# define CONSTANT variables -> better to use CONSTANTS (usually UPPERCASE as best practice) instead of global variables.
CLIENT_NAME = 'BOBS_BUTCHER' # define the client name, or project you are working on, a name to be able to find or search for the screen capture files
CLIENT_NAME = CLIENT_NAME.upper() # just in case to keep thing uniform, evaluate always to UPPERCASE to promote uniformity and mitigate user error
COUNTDOWN_SECONDS = 5 # countdown to appear in the terminal as a scheduled screenshot is about to be incoming
INTERVAL = 10 # period between screenshots
RUNTIME_IN_MINUTES = 60 # how long the program should run for. could also be how long the meeting is, or the length of a deep work dev session
# also the user shall have the ability to quit the program manually at any time
# this is accomplished with a standard practice of ctrl+c to quit -> see logic down in the code

# screen CAPTURE
def create_screenshots_folder(client_name):
    top_folder_path = '/Users/sudz4/Desktop/PROJECTZ/screen_shot_program_logs' # where to save screenshots
    if not os.path.exists(top_folder_path): # check the top folder path
        os.makedirs(top_folder_path) # if no top folder path, creates a new top folder path

    # create daily subfolder
    current_date = datetime.now().strftime('%Y%m%d_%a') # stores current date as var
    subfolder_name = f"{current_date}" 
    subfolder_path = os.path.join(top_folder_path, subfolder_name) # create subfolder path
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)

    # create essential technical library subfolder
    essential_library_name = f"{current_date}_ESSENTIAL_TECHNICAL_LIBRARY" # also could be called a "Core Technical Library (CTL)"
    essential_library_path = os.path.join(subfolder_path, essential_library_name) # insert an (empty) ETL library folder -> user can drag KEEP captures here later
    if not os.path.exists(essential_library_path):
        os.makedirs(essential_library_path)

    # create client-specific subfolder
    client_folder_name = f"{current_date}_{client_name}" # create a client or project or sessions specific subfolder with proper uniform naming convention
    client_folder_path = os.path.join(subfolder_path, client_folder_name) # insert client subfolder
    if not os.path.exists(client_folder_path):
        os.makedirs(client_folder_path)
        
    return client_folder_path

def take_screenshot(folder_path, client_name):
    countdown(COUNTDOWN_SECONDS) # uses the constant variable -> toggle the constant variable at beginning to adjust
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    client_name = CLIENT_NAME # pass the CLIENT_NAME CONSTANT
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
    end_time = time.time() + RUNTIME_IN_MINUTES * 60 # 60 seconds in a minute
    folder_path = create_screenshots_folder(CLIENT_NAME) 
    schedule.every(INTERVAL).seconds.do(take_screenshot, folder_path, CLIENT_NAME)
    
    print(f"Machine screen capture in progress ({INTERVAL} second intervals) for {RUNTIME_IN_MINUTES} minutes...")
    print("Press control+c to quit or stop running program")

    while time.time() < end_time:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("\nScreen Captures SAVED!")
        print("Thanks for using sCrEeN cApTuRe!")
        print()

# think about using ASCII at launch, details on how to use program(s)
# sub directory in the sub directory with CLIENT NAME, check if, then create new directory, else (if exists) insert new image file
"""END OF PROGRAM"""
