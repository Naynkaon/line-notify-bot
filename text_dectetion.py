import re
from langdetect import detect, DetectorFactory
from datetime import datetime

DetectorFactory.seed = 0

def check_calling(startword,text):
    return bool(re.search(startword, text))

def convert_to_number(text):
    # Fullwidth digits
    text = re.sub(r'[\uFF10-\uFF19]', lambda x: chr(ord(x.group()) - 0xFF00 + 0x30), text)
    # Chinese numerals
    chinese_numerals = {
        '一': '1', '二': '2', '三': '3', '四': '4', '五': '5',
        '六': '6', '七': '7', '八': '8', '九': '9', '零': '0'
    }
    for cn, ascii in chinese_numerals.items():
        text = text.replace(cn, ascii)
    return text

def mix_detect(text):
    # Count CJK characters (Traditional Chinese range)
    cjk_count = len(re.findall(r'[\u4E00-\u9FFF]', text))
    total_chars = len(re.sub(r'[\s\d\W]', '', text))  # Ignore spaces, numbers, punctuation
    
    if total_chars == 0:
        return None
    
    cjk_ratio = cjk_count / total_chars
    
    # If >30% CJK characters, assume Traditional Chinese
    if cjk_ratio > 0.3:
        return "zh-tw"
    
    # Otherwise, use langdetect
    return detect(text)

def replace_format(text):
    pattern = r'(\d{1,2})/(\d{1,2})\s+(\d{1,2}):(\d{2})\s*(AM|PM)'
    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        month, day, hour, minute, ampm = match.groups()
        month, day, hour, minute = map(int, (month, day, hour, minute))

        if ampm.upper() == "PM" and hour != 12:
            hour += 12
        elif ampm.upper() == "AM" and hour == 12:
            hour = 0

        result = datetime.now().replace(
            month=month, day=day, hour=hour, minute=minute-10,
            second=0, microsecond=0
        )
        return result
    