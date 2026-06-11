import ollama

def ai_process(text):
    pre_prompt ="""
                read this text and extract these only in json format,
                No markdown, no explanation,
                and only extract these requirement,
                Month,
                Date,
                Time,
                a summary of the text mainly about.
                """
    format_require="""
                The json format should look like this:
                {
                "Month": "",
                "Date": "",
                "Time": "",
                "summary": ""
                            }
                Analyze the input. 
                - If ALL items meet requirements: respond with exactly "" (empty, no explanation).
                - If ANY items do NOT meet requirements: list only the non-compliant items.
                Do not add commentary, summaries, or filler text.
                """

    final_prompt = pre_prompt + format_require + text
    response = ollama.generate(
        model="qwen2.5:1.5b",
        prompt=final_prompt
    )

    return response["response"]
