####
Node
####

Nodeは空間の1点を表す概念であり、グラフ構造における頂点に対応する。
交通データにおいてNodeとは駅のプラットフォーム、バス停標柱、タクシー乗り場、空港のゲートなどを表す。
つまり、Nodeは乗り場の抽象表現である。
Nodeはグラフ構造における頂点をし、地物に対する名称を定義する。駅やバス停を表すもので、データ分析の基本単位となる。
NodeはOperatorが所有するものとし、地理情報はPoint型である。


Properties
----------
.. list-table:: Node
   :widths: 15 10 10 10 10 30
   :header-rows: 1

   * - Name
     - Type
     - Required?
     - Nullable?
     - Example
     - Description
   * - id
     - String
     - True
     - False
     - 
     - データに対する固有識別子(UUIDv4)を格納する。
   * - uid
     - String
     - True
     - False
     - str(uuid.uuid4())
     - Entityに対する固有識別子を格納する。
   * - oid
     - String
     - True
     - True
     - 0001
     - 出典にて固有番号を付与している場合はその番号、出典がない場合はuidと同一の値を格納する。
   * - title
     - String
     - True
     - False
     - 龍ヶ崎市
     - 出典における名称
   * - created
     - Timestamp
     - True
     - False
     - 2020-03-14T00:00:00
     - データ生成日時を表す。
   * - issued
     - Timestamp
     - True
     - False
     - 2020-03-14T00:00:00
     - データ発行日時を表す。
   * - available
     - Timestamp
     - True
     - False
     - 2020-03-14T00:00:00
     - データ有効化日時を表す。
   * - valid
     - Timestamp
     - True
     - False
     - null
     - データ有効期限を表す。
   * - type
     - String
     - True
     - False
     - Station
     - データが使用している基底の種類を表す。
   * - subtype
     - String
     - True
     - False
     - 
     - 
   * - operator
     - String
     - True
     - False
     - 1c7f008a-ae84-6763-ae45-6839d83f8995
     - Nodeを所有、運営するOperatorのuid
   * - wkt
     - Well-Know-Text
     - True
     - False
     - POINT (134.59527, 34.48426)
     - 出典における地理位置
   * - address
     - String
     - False
     - False
     - 茨城県龍ヶ崎市
     - 地理位置を逆geocodingした住所、titleだけでは別地域で重複が発生する可能性が高いので、可読性のある住所で判別できるようにしておく。
   * - h3
     - String
     - True
     - False
     - abc123456
     - 出典における地理位置をh3へ変換したもの


Inheritances
------------
各交通モードにおいて、乗り場はそれぞれ固有のプロパティを持つ。
そのため、各交通モードにおいてNodeを継承したオブジェクトを生成する。
継承先では、図に示す継承先名称をtypeに設定し、それぞれの継承先では固有のプロパティを定義することを可能にする。

.. image:: images/class_node.svg
