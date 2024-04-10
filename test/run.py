from openai import OpenAI
from dotenv import load_dotenv
from prompts import (
    PLANNING_PROMPT_V2,
    CODING_PROMPT_V2
)

import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_gpt(prompt=None, temperature=0.3, top_p=0.5, frequency_penalty=1, presence_penalty=1, max_tokens=1500):
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )

    content = response.choices[0].message.content
    return content

def get_code(history, request):
    prompt = CODING_PROMPT_V2.format(chat_history=history, request=request)
    code = call_gpt(prompt=prompt)
    with open("code.md", "w") as file:
        file.write(code)
    return code

def code_postprocessing(response):
    response = response.strip()
    if "~~~" not in response:
        return False

    result = []
    current_file = None
    current_code = []
    code_block = False

    for line in response.splitlines():
        if line.startswith("File: "):
            if current_file:
                result.append({"file": current_file, "code": "\n".join(current_code)})
            current_file, current_code, code_block = ((line.split("`")[1]).strip(), [], False)
        elif line.startswith("```"):
            code_block = not code_block
        elif code_block:
            current_code.append(line)

    if current_file and current_code:
        result.append({"file": current_file, "code": "\n".join(current_code)})

    return result


def save_code_to_project(response):
        file_path_dir = None

        for file in response:
            file_path = f"projects/{file['file']}"
            file_path_dir = file_path[:file_path.rfind("/")]
            os.makedirs(file_path_dir, exist_ok=True)

            with open(file_path, "w") as f:
                f.write(file["code"])
    
        return file_path_dir


if __name__ == '__main__':
    code = get_code()
    code_files = code_postprocessing(code)

    if code_files:
        save_code_to_project(code_files)

# response = get_plan()
# plan = plan_postprocessing(response)

# def get_plan():
#     user_query = input("Input task: ")
#     prompt = PLANNING_PROMPT_V2.format(prompt = user_query)
#     plan = call_gpt(prompt=prompt)
#     with open("plan.md", "w") as file:
#         file.write(plan)
#     return plan

# def plan_postprocessing(response):
#     result = {"project": "", "reply": "", "focus": "", "plans": {}, "summary": ""}
#     current_section = None
#     current_step = None

#     for line in response.split("\n"):
#         line = line.strip()
#         if line.startswith(("Project Name:", "Reply:", "Focus:")):
#             current_section = line.split(":")[0].lower()
#             result[current_section] = line.split(":", 1)[1].strip()
#         elif line.startswith("Plan:"):
#             current_section = "plans"
#         elif current_section == "plans":
#             if line.startswith("- [ ] Step"):
#                 current_step = line.split(":")[0].strip().split()[-1]
#                 try:
#                     result["plans"][int(current_step)] = line.split(":")[1].strip()
#                 except:
#                     print("Skipping: ", line)
#             elif current_step:
#                 try:
#                     result["plans"][int(current_step)] += " " + line
#                 except:
#                     continue

#         elif current_section == "summary":
#             result["summary"] += " " + line.replace("```", "")

#     for key in ("project", "reply", "focus", "summary"):
#         result[key] = result[key].strip()

#     return result
