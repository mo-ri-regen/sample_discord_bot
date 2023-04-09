# Discord bot 設定

## ポータルサイトにアクセス

https://discord.com/developers/applications にログイン

### Bot

- 下記を ON にする

PRESENCE INTENT
SERVER MEMBERS INTENT
MESSAGE CONTENT INTENT

- TOKEN をコピーする
  ※ソースコードに「.env」を作成し TOKEN に貼り付ける

### OAuth2 > URL Generator

Scopes は bot をチェック
BOT PERMISSIONS で必要な権限にチェック
GENERATED URL の URL のリンクにアクセス
どの Discord サーバにいれるか認証が聞かれるのでクリックして認証する

## Discord アプリ

ユーザ設定>詳細設定

開発者モードを ON にする

## ライブラリ

ターミナルを開いて下記コマンドを実行

```
pip3 install -U discord.py
pip3 install -U python-dotenv
```

## 参考

https://qiita.com/taitaitatata/items/1039dc1786bf27c3def9
https://aprico-media.com/posts/8960
