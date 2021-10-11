##########
Conponents
##########
.. image:: images/systemconfiguration.svg

Functions
*********
TraISAREはデータを統一フォーマットで取り扱うことを目的としている。そのために必要な機能は下記に示すReceiver, Encoder, Aggregator, Viewerの4つである。

Receiver
---------
移動データを受信・取得しrawstoreに保存する機能である。データにより形式、更新頻度は異なるため、Receiverはデータ毎に設計する。
リアルタイムデータや定期的に更新される、ロケーション、時刻表データなどに対しては、データ受信・取得システムをクラウド上に構築するが、
更新頻度が極端に低い、駅・ネットワークデータについては手動でのデータ受信・取得に対応する。

Encoder
--------
rawstoreのデータを統一データフォーマットTraIIReへ変換する機能である。
TraISAREではcommonstoreにData matchingのための基本データを保有しており、Encoderはrawdataを基本データに対してマッチングさせながら変換する。


Aggregator
-----------
commonstoreのデータを操作し、データを表示用に集計、分析、出力jする機能である。Aggregatorは用途に応じて様々存在するが、具体的には以下の用途に使用する。

* Query Function
  
  Common Storeに対するクエリーを実行する。この機能は比較的小規模なデータに対して適用する。

* Statical Analytics Function
  
  Common Storeのデータに統計処理を実施して、集計結果を出力する。

* Machine Learning
  
  Common Storeのデータに機械学習を実施して、予測結果を出力する。例えば列車在線情報の遅れ情報より、未来の遅れを予測し、結果を出力する。

* API function
  
  Common Storeのデータを出力するためのインターフェイスで外部と連携するための機能である。データ出力フォーマットはNGSI-LD, GTFS, odptに対応する

Viewer
------
martstoreのデータを表示するユーザインターフェイスである。ダッシュボードを作成、保存したり、ユーザの閲覧権限を管理したりする。


Storages
********
各Fuctionを実行した結果生み出したデータを保存するストレージはrawstore, commonstore, martstoreの3つである。
これらストレージはすべてクラウド上に構築し、データ取り扱い量に応じた柔軟なスケーリングを可能にする。

rawstore
--------
Receiverが受信・取得したデータを保存するストレージである。データ形式は様々であるが、rawstoreでは素のデータを保存する。ファイルはReceiverの受信単位毎とし、
主にXML、JSON、CSVなどの構造化ファイルとして保存する。素のデータの保存を目的としているので、JPEG、PDF、ProtocolBufferなども保存する。
乗客の乗降履歴、人流といったデータは個人情報保護、データ権利の関係上、受信・取得元毎にデータを管理し、権利関係者以外の閲覧に供されないようにする。

commonstore
-----------
TraISAREの基本データとTraIIReデータを保存するストレージである。commonstoreに保存されるデータはTraIIReデータフォーマットに変換したものである。
commonstoreではデータ統一ための基幹となるベースデータを保有し、すべてのデータはベースデータに対してマッチングした状態で保存する。

martstore
---------
Aggregatorで集計、分析した結果を保存するストレージである。