# python Line_bot operational test

## -Pythonを使ったオウム返しLINEbot-

## APP概要
こちらで作成したLINEチャンネルアカウントに、文字を送信するとアカウントから打った文字を返信する。
## 目的
今後に向けて、LINE APIやherokuを理解する為に、試験的にLINE上で送信した文字をオウム返しするlinebotを作成。

## 開発環境
Windows 11

python 3.9.10

## 動作環境

heroku

git

## ライブラリ

Flask==2.0.3

line-bot-sdk==2.1.0

あとは、pip install に予め入っているライブラリ。

pip freeze > requirements.txt 

↑↑のコマンドで作ったrequirement.txtをそのまま使用。

## 作成にあたって詰まった箇所

1. herokuにうまくデプロイできず失敗。

　→ローカルリポジトリにリモートと追加していなかった為。

2. デプロイ完了後、LINEbotに送信しても返信が来ず、LINE DevelopersのwebhookでURL検証を行うもエラー。

　→herokuのlogを確認したが、heroku[router]: at=error code=H10 desc="App crashed"
 
  となっており、様々試行錯誤した結果、pip freeze > requirements.txtで出力したrequirements.txtをそのまま使用すると正常に動作した。

## 使用方法(動作確認方法)

普段使用しているLINEアカウント、または会社用アカウントなどで、下記QRLを読み取りbot-m802のアカウントを追加し、トークをボタンを押す。
botとトークできるようになるので何か、何でもいいので文字を返信する。すると数秒後返信した文字を返すので正常に動作されていると確認できる。

## botのLINEアカウント(動作確認用)

![画像URL](image/199apzbi.png)

## 動作イメージ

![画像](./image/Screenshot_20220323_144720_jp.naver.line.android.jpg)
