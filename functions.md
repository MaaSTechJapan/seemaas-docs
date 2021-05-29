# Functions
## Receiver
Receiverは交通事業者のデータを受信するための機能である。各交通事業者のデータは、次のように提供される。
- Push受信: 事業者からデータが送信されてくる場合
- Pull受信: 事業者からデータを取得する場合
受信方法が交通事業者毎に異なるため、TraISAREではReceiverを事業者毎に準備する。それぞれのReceiverがデータを受信し、Raw Storeへ保存する。

## Encorder
Encoderは、RAW Storeに保存された情報を読み取り、正規化、抽象化を実施してCommon Storeに保存する機能である。正規化・抽象化とはRaw Store内のデータの矛盾を排除するためデータを正規化し、TraIIRe形式に変換することでデータを抽象化することを指す。

## Aggregator
AggregatorはCommon Storeに保存された情報を集約、分析する機能である。Aggregatorは以下の機能を持つ。

### Query Function
Common Storeに対するクエリーを実行する。この機能は比較的小規模なデータに対して適用する。この機能によりレポート、ダッシュボードの作成に必要なデータを生成する。

### Statical Analytics Function
Common Storeのデータに統計処理を実施して、集計結果を出力する。運行中の台数、ある区間における乗車率の算出など、レポート・ダッシュボードの作成に必要となる数値を算出する。

### Machine Learning
Common Storeのデータに機械学習を実施して、予測結果を出力する。例えば列車在線情報の遅れ情報より、未来の遅れを予測し、結果を出力する。

### API function
Common Storeのデータを出力するためのインターフェイスで外部と連携するための機能である。データ出力フォーマットは以下に対応する。
- NGSI-LD
- GTFS, GTFS-RT
- odpt


