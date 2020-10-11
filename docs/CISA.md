### 米CISA Emotet対策
[注意喚起](注意喚起.html),[CISA](CISA.html),[Emotet](Emotet.html),[ガイド](ガイド.html),
米CISAが、Emotetに対するアラート。

対策一覧（一部意訳）
* マルウェアに関連する添付ファイル(.dll, .exe等)がついたメールをブロックする
* アンチウィルスソフトでスキャンできない添付ファイル(zipファイル等)がついたメールをブロックする
* グループポリシー(Group Policy Object)と、ファイアウォールのルールを実装する
* アンチウィルスソフトと、パッチ管理のプロセスを導入する
* メールフィルターと不信なIPからの通信をブロックするファイアウォールの実装
* 最小権限の原則を行う
* DMARCを導入する
* ネットワークやファンクションを分離する(セグメンテーション)
* 同じ階層レベルでの不要な通信を制限する
* ファイルやプリンターの共有サービスを停止する。もし必要な場合、強いパスワードかAD認証を利用する。
* MFA(多要素認証)を行う
* 送信元や添付ファイルが想定されたものであったとしても、添付ファイルを開く時は注意する。
* ファイアウォールを有効にし、未承諾な通信要求を拒否するように設定する。
* 不要なサービスを停止する。
* メールの添付ファイルはスキャンし、疑わしいものは削除する。スキャンされた添付ファイルが「正しいファイル形式」か確認する。（拡張子とファイルヘッダがあっているか等）
* 利用者のWebブラウジングを監視し、危険なサイトへのアクセスを制限する。
* リムーバブルメディア(USBメモリ等)を使う時は注意する
* インターネットからダウンロードしたファイルは実行前にスキャンする。
* 最新の脅威情報を入手し、適切なアクセスコントロールを行う。
* MITRE ATT&CK Techniquesにアクセスし、追加対策を確認する。
* CISA’s Alert on Technical Approaches to Uncovering and Remediating Malicious Activityを確認する。
* CISA and MS-ISAC Ransomware Guideを確認する。

[Alert (AA20-280A) Emotet Malware](https://us-cert.cisa.gov/ncas/alerts/aa20-280a)

[「Emotet」対策でパスワード付きzip添付ファイルのブロックを推奨 - 米政府](https://www.security-next.com/119360)
