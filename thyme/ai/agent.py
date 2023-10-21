import openai
from thyme.ops import parse_fenced_code_blocks
from thyme import logger


def build_namespace(path, model="gpt-4"):
    path = path.rstrip("/")

    with open(f"{path}/diagram.drawio.svg") as diagram:
        diagram_svg = diagram.read()

    with open(f"{path}/__init__.py") as context:
        context_text = context.read()

    messages = [
        {
            "role": "system",
            "content": f"""You are a Pydantic code generator. You will be given an SVG diagram that describes types and relationships. 
            You can use these to generate Pydantic objects. You will also be given extra context about the classes to add comments, doc strings and validators to the Pydantic objects
            Add example data per class in the pydantic Config as a schema_extra dictionary.
                SVG Diagram:
                ```svg
                 {diagram_svg}
                ```
                Context:
                {context_text}
                """,
        },
        {
            "role": "user",
            "content": "please generate the Pydantic code without any preamable or commentary, just the python code as text",
        },
    ]

    logger.debug(f"Generating types in {path}. Please wait a moment...")
    response = openai.ChatCompletion.create(model=model, messages=messages)

    code = response["choices"][0]["message"]["content"]

    code = parse_fenced_code_blocks(code, select_type="python")

    if isinstance(code, list):
        code = f"\n\n".join(code)

    with open(f"{path}/generated.py", "w") as f:
        f.write(code)

    logger.debug(f"Generated types in {path}/generated.py.")
