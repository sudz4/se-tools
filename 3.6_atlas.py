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
            {"role": "system", "content": "You are a helpful assistant that writes notes for your boss and categorizes, corrects, completes, and adds to short form notes (inputs)"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        n=3,
        stop=["."],
        temperature=0.5,
    )
    return completions.choices[0].message['content'].strip()

def update_text_file(filename, objectives, accomplishments):
    content = f"Daily Objectives:\n{objectives}\n\nDaily Accomplishments:\n{accomplishments}\n"
    with open(filename, "a") as f:
        f.write(content)

"""START OF TESTING AREA"""
# uncomment this section for testing
test_inputs = [
    "Objective: Define project scope for ServiceNow ITSM deployment",
    "Accomplishment: Completed ServiceNow ITSM deployment project charter",
    "Objective: Set up a project kick-off meeting with stakeholders",
    "Accomplishment: Finalized project timeline for ServiceNow ITSM deployment",
    "Objective: Develop a communication plan for ServiceNow ITSM deployment",
    "Accomplishment: Identified and resolved key risks in the ServiceNow ITSM deployment",
]

def test_function():
    today_date = datetime.now().strftime("%Y-%m-%d")
    log_filename = f"TESTING_log_{today_date}.txt"
    all_objectives = []  # Store all entered objectives
    all_accomplishments = []  # Store all entered accomplishments

    for task in test_inputs:
        corrected_task = complete_prompt(f"Correct, complete, and perform sentence completion for the following sentence: {task}.")
        prompt = f"Categorize the following task as either an objective or accomplishment: {corrected_task}"
        category = complete_prompt(prompt).lower()

        if "objective" in category:
            all_objectives.append(corrected_task)
        elif "accomplishment" in category:
            all_accomplishments.append(corrected_task)

    objectives = "\n".join(f"- {point}" for point in all_objectives)
    accomplishments = "\n".join(f"- {point}" for point in all_accomplishments)

    # Add creative context
    objectives_prompt = "Perform sentence completion for the following daily objectives, REMEMBER that you are writing this on behalf of me, so you are using I as your pronoun. If you are thinking of say You did x,y,z remember that you are me, so you need to write like.. I have x objective and I accomplished y:\n" + objectives
    accomplishments_prompt = "Perform sentence completion for the following daily accomplishments, again remembering to output text as if you are me writing about my day's objectives and accomplishments:\n" + accomplishments
    creative_objectives = complete_prompt(objectives_prompt).strip()
    creative_accomplishments = complete_prompt(accomplishments_prompt).strip()

    # Clear the existing output file before regenerating the content
    with open(log_filename, "w") as f:
        f.write("")

    update_text_file(log_filename, creative_objectives, creative_accomplishments)
    print("Summary generated and added to the log file.")

test_function()

"""END OF TESTING AREA"""
