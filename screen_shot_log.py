# libraries
import os
import time
import schedule
import subprocess

# screenCAPTURE
def create_screenshots_folder():
    folder_path = '/Users/sudz4/Desktop/PROJECT FOLDER/screen_shot_program_logs'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def take_screenshot(folder_path):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_file = os.path.join(folder_path, f"screenshot_{timestamp}.png")
    subprocess.run(["screencapture", "-x", screenshot_file])
    print(f"Screenshot saved at {screenshot_file}")

def main():
    folder_path = create_screenshots_folder()
    schedule.every(10).seconds.do(take_screenshot, folder_path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

"""END OF PROGRAM"""

# NOTES and Practice Code
# # screenSHOT
# def create_screenshots_folder():
#     folder_path = '/Users/sudz4/Desktop/PROJECT FOLDER/screen_shot_program_logs'
#     if not os.path.exists(folder_path):
#         os.makedirs(folder_path)
#     return folder_path

# def get_main_screen_dimensions():
#     main_display = CGDisplayBounds(CGMainDisplayID())
#     return main_display.origin.x, main_display.origin.y, main_display.size.width, main_display.size.height

# def take_screenshot(folder_path):
#     timestamp = time.strftime("%Y%m%d-%H%M%S")
#     screenshot_file = os.path.join(folder_path, f"screenshot_{timestamp}.png")

#     x, y, width, height = get_main_screen_dimensions()
#     screenshot = pyautogui.screenshot(region=(x, y, width, height))
#     screenshot.save(screenshot_file)
#     print(f"Screenshot saved at {screenshot_file}")

# def main():
#     folder_path = create_screenshots_folder()
#     schedule.every(10).seconds.do(take_screenshot, folder_path)

#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# if __name__ == "__main__":
#     main()
