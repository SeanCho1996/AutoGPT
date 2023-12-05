"""Auto-GPT: A GPT powered AI Assistant"""
import os
import json
import errno
import sys
# add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path)

import autogpt.app.cli
from autogpt.app.main import run_auto_gpt

if __name__ == "__main__":
    dataset = "HE"

    # choose dataset, get corresponding dataset config
    if dataset == "HE":
        dataset_file = "./dataset/HumanEval.jsonl"
        question_key = "prompt"
        test_key = "test"
        task_id_key = "task_id"
    elif dataset == "HE-E":
        dataset_file = "./dataset/HumanEval_Extend.jsonl"
        question_key = "prompt"
        test_key = "test"
        task_id_key = "task_id"
    elif dataset == "MBPP":
        dataset_file = "./dataset/MBPP.jsonl"
    elif dataset == "MBPP-E":
        dataset_file = "./dataset/MBPP_Extend.jsonl"
    else:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), dataset)

    # load all questions
    questions = []
    with open(dataset_file, "r") as f:
        for line in f:
            data = json.loads(line)
            questions.append(data)

    for i in questions[:2]:
        question = i[question_key]
        test_cases = i[test_key]
        task_id = i[task_id_key].split("/")[-1]
        print(question)
        print(test_cases)

        task = f"""Finish the following python function delimited by triple backticks:\n
        ```{question}```\n
        """
        # autogpt.app.cli.main(skip_reprompt=True, continuous=True, continuous_limit=5, gpt3only=True, ai_goal=task)
        run_auto_gpt(
            continuous=True,
            continuous_limit=2,
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
            workspace_directory=f"workspace_{task_id}",
            install_plugin_deps=False,
            # ai_name="AutoGPT_Coder",
            # ai_role="coder",
            # ai_goals=[task],
            task=task,
        )
