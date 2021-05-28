Raw Store
---------

Raw
Storeは交通事業者から提供された情報をそのままの形で保存するレイヤーである。Receiverの受信単位を1つのファイルとし、Raw
Storeに保存する。ファイルは主にXML、JSON、CSVなどの構造化ファイルとして保存することを想定するが、ファイルとして保存するのでJPEG、PDF、Protocol
Bufferなども保存できる。




Common Store
------------

Common StoreはEncorderで正規化、抽象化したデータを保存する。Common
StoreのデータはTraIIReデータ形式、Apache
Parquetファイルで保存する。すべての事業者のデータをTraIIRe形式に統一して保存することで、事業者に依らないデータの分析、情報提供を可能にする。

### Components and storage directory structures

Common StoreはAzure ADLS Gen2 Blob containerである。Blob
containerは以下のようにTraIIReデータ形式の基底モデルに従ってディレクトリを構成している。Encoderで生成したTraIIReデータ形式のファイルを該当する基底モデルのディレクトリに格納する。

      - commonstore
        |- edge
        |- graph
        |- node
        |- operator
        |- timetable
        |- transportation
        |- load
        |- leg
        |- trip
