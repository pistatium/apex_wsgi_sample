# apex_wsgi_sample

AWS Lambda + API Gateway でWSGI互換のアプリケーション(Flaskなど)を動かすサンプルです。


## 開発
`src` 以下の `flask` アプリケーションを自由に修正

## デプロイ

* Apex をインストール
  * http://apex.run/
  
* AWS の認証情報を環境変数にセット

* `project.json` の `role` を修正

* Apex デプロイ

* API Gateway のプロキシ統合としてセットアップ


