import os
import time
import schedule
import subprocess
from datetime import datetime

# screen CAPTURE
def create_screenshots_folder():
    top_folder_path = '/Users/sudz4/Desktop/PROJECTZ/screen_shot_program_logs' # where to save screenshots
    if not os.path.exists(top_folder_path): # check the top folder path
        os.makedirs(top_folder_path) # if no top folder path, creates a new top folder path

    # Create daily subfolder
    current_date = datetime.now().strftime('%Y%m%d_%a')
    subfolder_name = f"{current_date}"
    subfolder_path = os.path.join(top_folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    
    return subfolder_path

def take_screenshot(folder_path):
    timestamp = time.strftime("%Y%m%d-%H%M%S") # get the time stamp and format
    client_name = 'COMPANY' # TOGGLE -> your client's name. this is done for data sorting and retrieval (easily human readable). Use CAPS, easier to read and find quickly with human eyes.
    screenshot_file = os.path.join(folder_path, f"{timestamp}_{client_name}.png") # joins the timestamp with the client name
    subprocess.run(["screencapture", "-x", screenshot_file]) # screencapture command line tool that comes with macOS
    print(f"Screenshot saved at {screenshot_file}") # save the screenshot (full screen capture) to the folder path

def main():
    interval = 10 # TOGGLE -> specify the image capture intervals in SECONDS (period between image captures)
    print(f"Machine screen capture in progress ({interval} second intervals) ...")
    print("Press control+c to quit or stop running program")
    folder_path = create_screenshots_folder() 
    schedule.every(interval).seconds.do(take_screenshot, folder_path) # TOGGLE -> seconds to create more time in between screenshots

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

"""END OF PROGRAM"""
