"""Auto-GPT: A GPT powered AI Assistant"""
import os
import sys
# add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path)

import autogpt.app.cli
from autogpt.app.main import run_auto_gpt

if __name__ == "__main__":
    question = "from typing import List\n\n\ndef has_close_elements(numbers: List[float], threshold: float) -> bool:\n    \"\"\" Check if in given list of numbers, are any two numbers closer to each other than\n    given threshold.\n    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)\n    False\n    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)\n    True\n    \"\"\"\n"
    task = f"""Finish the following function delimited by triple backticks:\n
        ```{question}```\n
        """
    print(task)
    # autogpt.app.cli.main(skip_reprompt=True, continuous=True, continuous_limit=5, gpt3only=True, ai_goal=task)
    run_auto_gpt(
        continuous=True,
        continuous_limit=5,
        ai_settings=None,
        prompt_settings="prompt_settings.yaml",
        skip_reprompt=False,
        speak=False,
        debug=False,
        gpt3only=True,
        gpt4only=False,
        memory_type="json_file",
        browser_name="chrome",
        allow_downloads=False,
        skip_news=False,
        working_directory=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        workspace_directory="workspace",
        install_plugin_deps=False,
        # ai_name="AutoGPT_Coder",
        # ai_role="coder",
        # ai_goals=[task]
    )
