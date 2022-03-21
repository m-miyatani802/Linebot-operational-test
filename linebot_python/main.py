from flask import Flask,request,abort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent,TextMessage,TextSendMessage
import os

# flackの核
app=Flask(__name__)

#環境変数の取得
# ↓Lineデベロッパーからチャンネルアクセストークンとチャンネルシークレットを入力
YOUR_CHANNEL_ACCESS_TOKEN="channel_access_token"
YOUR_CHANNEL_SECRET="channel_secret"
line_bot_api=LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler=WebhookHandler(YOUR_CHANNEL_SECRET)

# @app.route("")はURLと関数を関連付ける。
@app.route("/callback",methods=["POST"])  # ←このURLにpostリクエストが来たらcallback関数が起動する.
def callback():
    # get X-Line-Singnature herader value
    signature=request.headers["X-Line-Signature"]

    # get request body as text
    # Flackでpostされたデータをそのまま受けるときは,request.dataではなくrequest.get_dateを使う.
    body=request.get_data(as_text=True)  # ←bodyを取得
    app.logger.info("Request body"+body)

    # handle webhook body
    try:
        # 署名を検出し,問題なければhandleに定義されている関数を読みだす
        handler.handle(body,signature)
    except InvalidSignatureError:
        # 署名検証で失敗したときは例外をあげる(エラー400を出す)
        abort(400)
    return "OK"

# オウム返しをする処理--メッセージを受け取った後に,どんな処理をしてどんなリプライを返すのかの処理
@handler.add(MessageEvent,message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__=="__main__":
    # app.run()
    port=int(os.getenv("PORT",5000))
    # ↓ ローカルサーバーを起動
    app.run(host="0.0.0.0",port=port)
