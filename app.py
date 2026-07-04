#flask 套件，建立 Webhook 伺服器
from flask import Flask, request

# 載入 json 標準函式庫，處理回傳的資料格式
import json

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# 載入 dotenv 套件，讀取 .env 檔案中的環境變數
from dotenv import load_dotenv
import os

# 載入 ai 的預設提示詞
from ai_response import ai_process
# 載入 偵測 ai 啟動詞跟時間函式
from text_dectetion import check_calling

# 載入排程功能
from Schedule import set_schedule


Startword = "@Notify_bot"   # 用 @Notify_bot 做為啟動詞

load_dotenv()
token = os.environ.get("MY_TOKEN")
secret_number = os.environ.get("MY_SECRET")

# 建立 line Bot 的 Token 跟 secret_number
line_bot_api = LineBotApi(token)
handler = WebhookHandler(secret_number)

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)                    # 取得收到的訊息內容
    try:
        json_data = json.loads(body)                         # json 格式化訊息內容
        signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
        handler.handle(body, signature)                      # 綁定訊息回傳的相關資訊

        tk = json_data['events'][0]['replyToken']            # 取得回傳訊息的 Token
        user_id = json_data['events'][0]['source']['userId'] # 取得使用者 ID 
        text = json_data['events'][0]['message']['text']    # lineʼs message text
        reply = None

        if check_calling(Startword, text): # check startword
            cleaned = text.replace(Startword,"")
            reply = ai_process(cleaned)

        if reply:
            line_bot_api.reply_message(tk, TextSendMessage(text=reply))  # 回傳訊息   
    except Exception as e:
        print("Error:", e)
        print(body)                                          # 如果發生錯誤，印出收到的內容
        
    return 'OK'                                              # 驗證 Webhook 使用，不能省略

if __name__ == "__main__":
    app.run()
