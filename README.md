# note-latest-feed

339PLANNING公式サイトに埋め込む「noteの最新記事3件」表示用のデータリポジトリ。

`fetch_latest.py` が毎朝6時(JST)にnote.com/339planningのRSSを取得し、最新3件を `latest3.json` に書き出す（GitHub Actionsで自動実行）。

サイト側は `latest3.json` を [jsDelivr](https://www.jsdelivr.com/) 経由で読み込んで表示する。
