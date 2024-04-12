from typing import Optional

from openai import OpenAI
from dotenv import load_dotenv
import os
import json

from rich.console import Console
from prompts import PLANNING_PROMPT_V2, CODING_PROMPT_V2

load_dotenv()
console = Console()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def call_gpt(
    prompt=None,
    temperature=0.3,
    top_p=0.5,
    frequency_penalty=1,
    presence_penalty=1,
    max_tokens=1432,
    system_message_path: Optional[str] = None,
):
    if system_message_path:
        with open(system_message_path, "r") as file:
            system_message = file.read()
    else:
        system_message = "You are a helpful assistant that is here to help the user with their queries."

    # console.log(f"# System Message: \n{system_message}\n")
    # console.log(f"# Prompt: \n{prompt}\n")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": system_message,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )

    content = response.choices[0].message.content
    return content


def get_breakdown(history):
    prompt = PLANNING_PROMPT_V2.format(
        clarifying_question=history[-1], chat_history=history[:-1]
    )
    plan = call_gpt(prompt=prompt)
    with open("plan.md", "w") as file:
        file.write(plan)
    return plan


def get_code(component_wise_breakdown, messages, key_details):
    prompt = CODING_PROMPT_V2.format(
        component_wise_breakdown=component_wise_breakdown,
        clarifying_question=messages[-1],
        # chat_history=messages[:-1],
        key_details=key_details,
    )

    # print("component_wise_breakdown: ", component_wise_breakdown)
    code = call_gpt(prompt=prompt)
    # code = "N"
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
            current_file, current_code, code_block = (
                (line.split("`")[1]).strip(),
                [],
                False,
            )
        elif line.startswith("```"):
            code_block = not code_block
        elif code_block:
            current_code.append(line)

    if current_file and current_code:
        result.append({"file": current_file, "code": "\n".join(current_code)})

    return result


def breakdown_postprocessing(response):
    result = {
        "requirements": "",
        "focus": "",
        "components": {},
        "key_details": "",
    }
    current_section = None
    current_step = None

    for line in response.split("\n"):
        line = line.strip()
        if line.startswith(("Current Focus:")) or line.startswith(("Focus:")):
            current_section = line.split(":")[0].lower()
            result[current_section] = line.split(":")[1].strip()
        elif line.startswith("Component breakdown:"):
            current_section = "components"
        elif line.startswith("Requirements:"):
            result["requirements"] = line.split(":")[1].strip()
        elif line.startswith("Key Details:"):
            current_section = "key_details"
        elif current_section == "components":
            if line.startswith("- [ ] Component"):
                current_step = line.split("- [ ] ")[1].strip().split(":")[0]
                try:
                    result["components"][current_step] = line.split(":")[1].strip()
                except:
                    print("Skipping: ", line)
            elif current_step:
                try:
                    result["components"][int(current_step)] += " " + line
                except:
                    continue
        elif current_section == "key_details":
            result["key_details"] += " " + line

    for key in ("focus", "requirements", "key_details"):
        result[key] = result[key].strip()

    return result


def parse_response(response):
    """
    The response would be a markdown of the following format:
    ```markdown
      ## **Requirement**
      {describe here if a renderable is required. If not, skip the rest of the sections}

      ## **HTML**
      {html content here}

      ## **CSS**
      {css content here}

      ## **Javascript**
      {js code here}
    ```

    Parse the response into a dictionary of the following format:
    {
        "requirement": str,
        "html": str,
        "css": str,
        "js": str
    }
    Also make an output directory and save the html, css, and js files there.

    :param response:
    :return: list[dict]
    """
    # Split the response into the different sections
    sections = response.split("##")
    sections = [section.strip() for section in sections]

    # Parse the sections
    parsed_response = {}
    for section in sections:
        if section.startswith("**Requirement**"):
            parsed_response["requirement"] = section.split("**Requirement**")[1].strip()
        elif section.startswith("**HTML**"):
            parsed_response["html"] = section.split("**HTML**")[1].strip()
            # check if it starts with a code block and ends with a code block
            if parsed_response["html"].startswith("```html"):
                parsed_response["html"] = (
                    parsed_response["html"].split("```html")[1].strip()
                )
            if parsed_response["html"].endswith("```"):
                parsed_response["html"] = (
                    parsed_response["html"].split("```")[0].strip()
                )
        elif section.startswith("**CSS**"):
            parsed_response["css"] = section.split("**CSS**")[1].strip()
            if parsed_response["css"].startswith("```css"):
                parsed_response["css"] = (
                    parsed_response["css"].split("```css")[1].strip()
                )
            if parsed_response["css"].endswith("```"):
                parsed_response["css"] = parsed_response["css"].split("```")[0].strip()
        elif section.startswith("**Javascript**"):
            parsed_response["js"] = section.split("**Javascript**")[1].strip()
            if parsed_response["js"].startswith("```javascript"):
                parsed_response["js"] = (
                    parsed_response["js"].split("```javascript")[1].strip()
                )
            if parsed_response["js"].endswith("```") or parsed_response["js"].endswith(
                "~~~"
            ):
                parsed_response["js"] = parsed_response["js"].split("```")[0].strip()

    if not os.path.exists("output"):
        os.makedirs("output")

    try:
        # Save the files
        with open("output/index.html", "w") as file:
            file.write(parsed_response["html"])
        console.log("HTML saved in output/index.html")

        with open("output/style.css", "w") as file:
            file.write(parsed_response["css"])
        console.log("CSS saved in output/style.css")

        with open("output/script.js", "w") as file:
            file.write(parsed_response["js"])
        console.log("Javascript saved in output/script.js")
    except KeyError:
        console.log("Something went wrong with the code generation...")

    return parsed_response


def run():
    # Read the messages
    with open("chat.json", "r") as file:
        messages = json.load(file)

    # Create plans
    console.log("[bold purple]Calling the GPT model...")
    with console.status("[bold red]Generating plan..."):
        response = get_breakdown(messages["messages"])
        components = breakdown_postprocessing(response)
    console.log("[bold yellow]Plan generated successfully!")

    if components["requirements"] == "False":
        console.log("[bold red]No renderable required. Skipping code generation.")
        return

    # Convert plan to code
    console.log("[bold purple]Calling the GPT model...")
    with console.status("[bold green]Generating code..."):
        response = get_code(
            components["components"], messages["messages"], components["key_details"]
        )
    console.log("[bold green]Code generated successfully!")

    # Save the response
    with open("response.md", "w") as file:
        file.write(response)
    console.log("Response saved successfully!")

    # Parse the response
    parsed_response = parse_response(response)


if __name__ == "__main__":
    run()
