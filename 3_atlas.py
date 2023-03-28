# libs
import openai
import os

# config
from X_config4 import OPENAI_API_TOKEN

# using -> gpt-3.5-turbo
openai.api_key = OPENAI_API_TOKEN # store token as api key var

def complete_prompt(prompt):
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.8,
    )
    return completions.choices[0].message['content'].strip()

def update_text_file(filename, section, content):
    with open(filename, "a") as f:
        f.write(f"{section}\n{content}\n\n")

def update_text_file(filename, section, content):
    with open(filename, "a") as f:
        f.write(f"{section}\n{content}\n\n")

def main():
    log_filename = "daily_log.txt"
    while True:
        print("Choose an option:")
        print("1. Update Daily Objectives")
        print("2. Update Daily Accomplishments")
        print("3. Generate Summary")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            section = "Daily Objectives:"
        elif choice == 2:
            section = "Daily Accomplishments:"
        elif choice == 3:
            with open(log_filename, "r") as f:
                text = f.read()
            prompt = f"Summarize the following text and add color and context: {text}"
            summary = complete_prompt(prompt)
            update_text_file(log_filename, "Summary:", summary)
            print("Summary generated and added to the log file.")
            continue
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        raw_input = input(f"Enter your {section[:-1].lower()} (use '|' to separate bullet points): ")
        bullet_points = raw_input.split("|")
        corrected_bullet_points = []

        for point in bullet_points:
            prompt = f"Correct and complete the following bullet point: {point.strip()}"
            corrected_point = complete_prompt(prompt)
            corrected_bullet_points.append(corrected_point)

        content = "\n".join(f"- {point}" for point in corrected_bullet_points)
        update_text_file(log_filename, section, content)
        print(f"{section[:-1]} updated in the log file.")
    print("Exiting the program. Goodbye!")


# if you are running .py
if __name__ == "__main__":
    main()