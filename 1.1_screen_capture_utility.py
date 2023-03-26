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
