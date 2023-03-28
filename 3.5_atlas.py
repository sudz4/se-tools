import openai
import os
from datetime import datetime

# config
from X_config4 import OPENAI_API_TOKEN

# using -> gpt-3.5-turbo
openai.api_key = OPENAI_API_TOKEN

def complete_prompt(prompt):
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", # specify the language model
        messages=[ # array of message objects, including a system message that sets the behavior of the assistant, and one or more user messages containing the input prompts.
            {"role": "system", "content": "You are an elite executive assistant. You are great at organizing, completing, editing, and adding to partially written notes on your executives behalf (as if you were them)"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100, # increase this value to allow for longer responses, but be careful not to set it too high
        n=3,# number of responses you want to generate for each input. if you want more options to choose from, increase the value of n.
        stop=None, # stop when a period is encountered
        temperature=0.5, # controls the randomness of the generated text -> 
        ### higher temperature (e.g., 1.0) will produce more random output -> 
        ### while a lower temperature (e.g., 0.2) will make the output more focused and deterministic. 
        ### Adjust this value to find a balance between creativity and accuracy.
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
            corrected_task = complete_prompt(f"Correct spelling errors and perform sentence completion for the prompt: {task}.")
            prompt = f"Categorize the following task as either an objective or accomplishment: {corrected_task}"
            category = complete_prompt(prompt).lower()

            if "objective" in category:
                all_objectives.append(corrected_task)  # Add the corrected_task to all_objectives
                print("Task added to Daily Objectives.")
            elif "accomplishment" in category:
                all_accomplishments.append(corrected_task)  # Add the corrected_task to all_accomplishments
                print("Task added to Daily Accomplishments.")
            else:
                print("Unable to categorize the task. Please try again.")
                continue
        elif choice == 2:
            objectives = "\n".join(f"- {point}" for point in all_objectives)
            accomplishments = "\n".join(f"- {point}" for point in all_accomplishments)
            
            # Add creative context
            objectives_prompt = ("Perform sentence completion\n"+ objectives)
            accomplishments_prompt = ("Perform sentence completion"+ accomplishments)
            creative_objectives = complete_prompt(objectives_prompt).strip()
            creative_accomplishments = complete_prompt(accomplishments_prompt).strip()

            # Clear the existing output file before regenerating the content
            with open(log_filename, "w") as f:
                f.write("")

            update_text_file(log_filename, creative_objectives, creative_accomplishments)
            print("Summary generated and added to the log file.")
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

    print("Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()
