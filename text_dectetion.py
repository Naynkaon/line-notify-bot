import re
from langdetect import detect, DetectorFactory
from datetime import datetime

DetectorFactory.seed = 0

def check_calling(startword,text):
    return bool(re.search(startword, text))

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

def detect_time_format(text):
    pattern = r'\d{1,2}:\d{2}\s*(?:AM|PM|am|pm)?'
    times = re.findall(pattern,text)
    return times
