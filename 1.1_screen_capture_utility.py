# libraries
import os
import time
import schedule
import subprocess

# screenCAPTURE
def create_screenshots_folder():
    folder_path = '/Users/sudz4/Desktop/PROJECT FOLDER/screen_shot_program_logs' # where to save screenshots
    if not os.path.exists(folder_path): # check the folder path 
        os.makedirs(folder_path) # if no folder path, creates a new folder path
    return folder_path

def take_screenshot(folder_path):
    timestamp = time.strftime("%Y%m%d-%H%M%S") # get the time stamp and format
    client_name = 'COMPANY' # TOGGLE -> your client's name. this is done for data sorting and retrieval (easily human readable). Use CAPS, easier to read and find quickly with human eyes.
    screenshot_file = os.path.join(folder_path, f"{timestamp}_{client_name}.png") # joins the timestamp with the client name
    subprocess.run(["screencapture", "-x", screenshot_file]) # screencapture command line tool that comes with macOS
    print(f"Screenshot saved at {screenshot_file}") # save the screenshot (full screen capture) to the folder path

def main():
    folder_path = create_screenshots_folder() 
    schedule.every(10).seconds.do(take_screenshot, folder_path) # TOGGLE -> seconds to create more time in between screenshots

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

"""END OF PROGRAM"""


"""
USE CASES FOR SCREEN SHOT APP
1. Using auto-captured screen shots later for config docs - 
-(documents to refer to if we forget how to do something or need to do an update later)
2. Capturing requirements in the absence of zoom recordings. We might also be able -
- to make the case for it being more efficient to do screen capture. It can be tiring -
- and time consuming scrolling and buffering through recordings. For me and the reason - 
- that I created the program... well the reason I created it was for speed, accuracy, and efficeny.
But, for me I am okay with 500-1000 screen shots taken at timestamped intervals during a meeting - 
- or a dev session. I am okay with that even if I only grab 3-5 of those screenshots to add -
- to the formal project config doc folder (deliverable, probably with annoted notes, other -
- project data from the project manager etc.)

"""

# <br>

"""
BACKGROUND, NOTES, & FUTURE DEV IDEAS
*As a Solution Architect or Pre-Sales Engineer, requirements gathering is an important part of the role(s).
*Not all meetings are recorded or someone forgets to record.
*Leaving an SA or SE up late at night with no requirements, trying their best, educated guessing.
*The solution falls short of the client's expectations.
*Remember it is the SA / SE job to pull the requirements out of the Client,and help them help - 
- you connect the business outcomes with technical solutions (the area where you are the expert)

*I got the idea for this app from my cyber sec background and schooling. Some of these malware -
- programs get onto machines and just snap screenshots at intervals.
*When writing this program I was also thinking about how when a user enters a password -
- and then clicks "show password" to verify? To digress for a moment, usually I think the show -
- password feature is supposed to be a promoted good feature, and not increase vulnerability.

"""