
## 本サイトの位置づけ・目的

セキュリティに関連する検討を行う際に、参考となるスタンダードやレポートを効率的に見つけられる場。

「概要」と「どんな人」が「どんな時」に利用することが推奨されるかを分かるようにする。

スタンダードやレポートへのリンクや概要説明のページへのリンク等を保存する。


## スタンダード/ガイド

### IPA インターネット接続機器の安全な選定・利用ガイドと製品開発者向けガイド

インターネットに接続される機器に関する、利用者向けのガイドと、開発者向けのガイド

[https://www.ipa.go.jp/about/press/20200827.html](https://www.ipa.go.jp/about/press/20200827.html)

#### 脆弱性対処に向けた製品開発者向けガイド

ルーター等のネットワークに接続する機器の脆弱性対策として実施すべき事項をまとめたガイドとチェックリスト。

以下の特徴がある。
* 複数のスタンダード/ガイドから標準的に求められる事項を抽出
* 対策はレベル1〜3まで存在し、製品特性や状況から対策レベルを取捨選択可能
* 12項目と絞り込まれている
* 具体的な技術の話ではないため、どちらかと言うと管理層向け（セキュリティポリシーを定める、セキュア開発を行う、等）

主な対象読者：対象製品の開発を行う事業者（主に中小規模）

[https://www.ipa.go.jp/security/vuln/report/notice/guideforvendor.html](https://www.ipa.go.jp/security/vuln/report/notice/guideforvendor.html)


#### 一般消費者向け「ネット接続製品の安全な選定ガイド」・「ネット接続製品の安全な利用ガイド」

[https://www.ipa.go.jp/security/vuln/report/notice/guideforconsumer.html](https://www.ipa.go.jp/security/vuln/report/notice/guideforconsumer.html)

## レポート

### 日本IBM 情報漏えい時に発生するコストに関する調査2020
ポイント
* 複数国の情報漏えいについて調査・分析
* 情報漏えい時に発生するコストの平均は380万ドル
* 情報漏えい発生から検知まで平均で207日、封じ込めまで280日

[https://www.ibm.com/blogs/security/jp-ja/whats-new-2020-cost-of-a-data-breach-report/](https://www.ibm.com/blogs/security/jp-ja/whats-new-2020-cost-of-a-data-breach-report/)


## ツール関連

### nmap

ポートスキャンを実施するツール

[https://nmap.org/](https://nmap.org/)

### OWASP ZAP
Webサイトに対して攻撃を行い、脆弱性を確認するツール

[https://www.zaproxy.org/](https://www.zaproxy.org/)

### Pysa

Facebook製のPythonコードの静的解析ツール

[https://engineering.fb.com/security/pysa/](https://engineering.fb.com/security/pysa/)

### OpenVAS

脆弱性のあるバージョンのソフトウェアが利用されていないかチェックするツール

[https://www.openvas.org/](https://www.openvas.org/)

### Vuls

脆弱性のあるバージョンのソフトウェアが利用されていないかチェックするツール

[https://vuls.io/](https://vuls.io/)

### OWASP Dependency Check

依存しているコンポーネントに脆弱なものがないかチェックするツール

[https://owasp.org/www-project-dependency-check/](https://owasp.org/www-project-dependency-check/)

### skipfish

Webアプリケーション用のセキュリティ調査ツール

[https://code.google.com/archive/p/skipfish/](https://code.google.com/archive/p/skipfish/)

### Tsunami
ネットワークスキャナー

[https://github.com/google/tsunami-security-scanner](https://github.com/google/tsunami-security-scanner)


## 重要なインシデント

### VPNの不正接続について(2020年8月)

* [日経新聞 テレワーク、VPN暗証番号流出　国内38社に不正接続](https://www.nikkei.com/article/DGXMZO62994110U0A820C2MM8000/)
* [ITMedia VPNパスワード流出、原因は「テレワーク用に急きょ稼働させた旧VPN装置に脆弱性」　平田機工](https://www.itmedia.co.jp/news/articles/2008/26/news123.html)
