from typing import Optional

from openai import OpenAI
from dotenv import load_dotenv
import os
import json

from rich.console import Console
from prompts import (
    PLANNING_PROMPT_V2,
    CODING_PROMPT_V2,
    CODING_PROMPT_TAILWIND,
    PLANNING_PROMPT_TAILWIND,
)

load_dotenv()
console = Console()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
tailwind = True


def call_gpt(
    prompt=None,
    temperature=0,
    top_p=1,
    experimental=False,
    max_tokens=2000,
    system_message_path: Optional[str] = None,
):
    if system_message_path:
        with open(system_message_path, "r") as file:
            system_message = file.read()
    else:
        system_message = "You are a helpful assistant that is here to help the user with their queries."

    # console.log(f"# System Message: \n{system_message}\n")
    # console.log(f"# Prompt: \n{prompt}\n")
    if experimental:
        model = "gpt-4-turbo-2024-04-09"
    else:
        model = "gpt-4-1106-preview"

    response = client.chat.completions.create(
        model=model,
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
    )

    content = response.choices[0].message.content
    return content


def get_breakdown(history):
    if tailwind:
        prompt = PLANNING_PROMPT_TAILWIND.format(
            clarifying_question=history[-1], chat_history=history[:-1]
        )
    else:
        prompt = PLANNING_PROMPT_V2.format(
            clarifying_question=history[-1], chat_history=history[:-1]
        )

    plan = call_gpt(prompt=prompt)
    with open("output/plan.md", "w") as file:
        file.write(plan)
    console.log("[bold yellow]Plan generated and saved successfully!")
    return plan


def get_code(component_wise_breakdown, messages, key_details):
    if tailwind:
        prompt = CODING_PROMPT_TAILWIND.format(
            component_wise_breakdown=component_wise_breakdown,
            clarifying_question=messages[-1],
            key_details=key_details,
        )
    else:
        prompt = CODING_PROMPT_V2.format(
            component_wise_breakdown=component_wise_breakdown,
            clarifying_question=messages[-1],
            key_details=key_details,
        )

    # print("component_wise_breakdown: ", component_wise_breakdown)
    code = call_gpt(prompt=prompt)
    with open("output/code.md", "w") as file:
        file.write(code)
    console.log("[bold green]Code generated and saved successfully!")
    return code


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
            if line.startswith("# [$] Component"):
                current_step = line.split("# [$] ")[1].strip().split(":")[0]
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


def code_postprocessing(response):
    # Split the response into the different sections
    sections = response.split("##")
    sections = [section.strip() for section in sections]

    # Parse the sections
    parsed_response = {}
    for section in sections:
        if section.startswith("**HTML**"):
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
        elif not tailwind and section.startswith("**CSS**"):
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
        console.log("[green]HTML saved in output/index.html")

        if not tailwind:
            with open("output/style.css", "w") as file:
                file.write(parsed_response["css"])
            console.log("[green]CSS saved in output/style.css")

        with open("output/script.js", "w") as file:
            file.write(parsed_response["js"])
        console.log("[green]Javascript saved in output/script.js")
    except KeyError as e:
        console.log("[bold red]Something went wrong while saving the generated code...: ", e)

    return parsed_response


def run():
    # Read the messages
    with open("chat/chat.json", "r") as file:
        messages = json.load(file)

    # Create plans
    console.log("[bold purple]Step 1: Create a component-wise breakdown plan...")
    with console.status("[bold red]Generating plan..."):
        response = get_breakdown(messages["messages"])
        components = breakdown_postprocessing(response)

    if components["requirements"] == "False":
        console.log("[bold red]No renderable required. Skipping code generation...")
        return

    # Convert plan to code
    console.log("[bold purple]Step 2: Generate code using the previously generated breakdown plan...")
    with console.status("[bold green]Generating code..."):
        response = get_code(
            components["components"], messages["messages"], components["key_details"]
        )

    # Parse the response
    code_postprocessing(response)

    console.log(
        "[bold purple]Code generation completed successfully and saved into respective files!"
    )


if __name__ == "__main__":
    run()
