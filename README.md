# Pythonを使ったオウム返しLINEbot
## APP概要
こちらで作成したbotチャンネルに、文字を送信するとチャンネルの方から打った文字を返信する。
## 目的
今後に向けて、LINE APIやherokuを理解する為に、試験的にLINE上で送られた文字をオウム返しするlinebotを作成する。

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

pip freeze > requirement.txt 

↑↑のコマンドでrequirement.txtを作成しています。

## 使用方法(動作確認方法)

普段使用しているLINEアカウント、または会社用アカウントなどで、下記QRLを読み取りbot-m802のアカウントを追加し、トークをボタンを押す。
botとトークできるようになるので何か、何でもいいので文字を返信する。すると数秒後返信した文字を返してくれると思うので正常に動作されていると確認できます。

## botのLINEアカウント(動作確認用)

![画像URL](image/199apzbi.png)

## 動作イメージ

![画像](./image/Screenshot_20220323_144720_jp.naver.line.android.jpg)
