from flask import Flask, request

# 載入 json 標準函式庫，處理回傳的資料格式
import json

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from dotenv import load_dotenv
import os

#載入 apscheduler 保存待辦事項
from apscheduler.schedulers.background import BackgroundScheduler

#載入 ai 的預設提示詞
from ai_response import ai_process
#載入 偵測 ai 啟動詞函式
from text_dectetion import check_calling
Startword = "@A-mouse" #replace Startword with your line bot's name

from Schedule import set_scheduler

load_dotenv()
token = os.environ.get("MY_TOKEN")
secret_number = os.environ.get("MY_SECRET")
app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)                    # 取得收到的訊息內容
    try:
        json_data = json.loads(body)                         # json 格式化訊息內容
        access_token = token
        secret = secret_number
        line_bot_api = LineBotApi(access_token)              # 確認 token 是否正確, 記得把 access_token 換成你的 line bot token
        handler = WebhookHandler(secret)                     # 確認 secret 是否正確, 記得把 secret 換成你的 line bot secret
        
        signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
        handler.handle(body, signature)                      # 綁定訊息回傳的相關資訊
        tk = json_data['events'][0]['replyToken']            # 取得回傳訊息的 Token
        type = json_data['events'][0]['message']['type']     # 取得 LINe 收到的訊息類型
        if type=='text':
            if check_calling(Startword ,json_data['events'][0]['message']['text']): # 確認是否收到啟動詞
                loading_text = json_data['events'][0]['message']['text'] # 儲存文字
                cleaned_text = loading_text.replace(Startword, "") #把啟動詞移除
                msg = ai_process(cleaned_text)  # 取得整理過的文字訊息並傳送給 AI
                reply = msg #回復 AI 產生的內容
        else:
            reply = '你傳的不是文字'
        line_bot_api.reply_message(tk,TextSendMessage(reply))# 回傳訊息
    except:
        print(body)                                          # 如果發生錯誤，印出收到的內容
    return 'OK'                                              # 驗證 Webhook 使用，不能省略

if __name__ == "__main__":
    app.run()
