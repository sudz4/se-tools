import openai
import os
from datetime import datetime

# config
from X_config4 import OPENAI_API_TOKEN

# using -> gpt-3.5-turbo
openai.api_key = OPENAI_API_TOKEN

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

def update_text_file(filename, objectives, accomplishments):
    content = f"Daily Objectives:\n{objectives}\n\nDaily Accomplishments:\n{accomplishments}\n"
    with open(filename, "a") as f:
        f.write(content)

def main():
    today_date = datetime.now().strftime("%Y-%m-%d")
    log_filename = f"TESTING_log_{today_date}.txt"
    all_objectives = []  # Store all entered objectives
    all_accomplishments = []  # Store all entered accomplishments

    while True:
        print("Choose an option:")
        print("1. Add a task")
        print("2. Generate Summary")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            task = input("Enter your task: ")
            prompt = f"Categorize the following task as either an objective or accomplishment: {task}"
            category = complete_prompt(prompt).lower()

            if "objective" in category:
                all_objectives.append(task)  # Add the task to all_objectives
                print("Task added to Daily Objectives.")
            elif "accomplishment" in category:
                all_accomplishments.append(task)  # Add the task to all_accomplishments
                print("Task added to Daily Accomplishments.")
            else:
                print("Unable to categorize the task. Please try again.")
                continue
        elif choice == 2:
            objectives = "\n".join(f"- {point}" for point in all_objectives)
            accomplishments = "\n".join(f"- {point}" for point in all_accomplishments)

            # Clear the existing output file before regenerating the content
            with open(log_filename, "w") as f:
                f.write("")

            update_text_file(log_filename, objectives, accomplishments)
            print("Summary generated and added to the log file.")
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

    print("Exiting the program. Goodbye!")


if __name__ == "__main__":
    main()
