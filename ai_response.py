import ollama
from text_dectetion import mix_detect

from dotenv import load_dotenv
import os

load_dotenv()
ai_model = os.environ.get("MY_AI_MODEL")

#text = "在今天 13:00 前去 T203教室考試"
#text = "remember to upload your report to tronclass before 5/31 11:59PM"

def ai_process(text):

    lang = mix_detect(text)
    timing = None


    charter = "You are a helpful assistant who speaks like a warm, concise friend. follow these rule below and responce"

    rule =f"""
            read this text and extract these as a one line summary,
            and you MUST follow these rule:
            1. the only language you can use is: {lang}.
            2. Maintain clarity and readability
            3. Do not change the language of the output
            4. delete every !, #, $, %, ^, &, *, (, ), [, ] in the reply
            5. you only need to send the time for once
            6. keeping the original meaning and point
            7. only reply with summary, no extra addup
        """
    
    need_data = f"""

                """

    pre_text="""
                The text you need to summary: 
                """

    final_prompt = charter + rule + need_data + pre_text + text
    response = ollama.generate(
        model=ai_model,
        prompt=final_prompt
    )

    return response["response"]
