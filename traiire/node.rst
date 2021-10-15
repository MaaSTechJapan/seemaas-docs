Node
****

Nodeは空間の1点を表す概念であり、グラフ構造における頂点に対応する。
交通データにおいてNodeとは駅のプラットフォーム、バス停標柱、タクシー乗り場、空港のゲートなどを表す。
Nodeはグラフ構造における頂点をし、地物に対する名称を定義する。駅やバス停を表すもので、データ分析の基本単位となる。
NodeはOperatorが所有するものとし、地理情報はPoint型である。
subtypeは以下から選択するものとする。
# Station
# Busstop
# Airport
# Port
# Cycleport

.. list-table:: GeoEssential
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
     - Primary keyを格納する。
   * - uid
     - String
     - True
     - False
     - str(uuid.uuid4())
     - Unique idを格納する。
   * - oid
     - String
     - True
     - False
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
     - Node
     - データが使用している基底の種類を表す。
   * - subtype
     - String
     - True
     - False
     - Station
     - 交通種別を表す適切なType
   * - operator
     - String
     - True
     - False
     - 1c7f008a-ae84-6763-ae45-6839d83f8995
     - Nodeを所有、運営するOperatorのuid
   * - WKT
     - Well-Know-Text
     - True
     - False
     - POINT (134.59527, 34.48426)
     - 出典における地理位置
   * - h3
     - String
     - True
     - False
     - abc123456
     - 出典における地理位置をh3へ変換したもの
   * - address
     - String
     - False
     - False
     - 茨城県龍ヶ崎市
     - 地理位置を逆geocodingした住所、titleだけでは別地域で重複が発生する可能性が高いので、可読性のある住所で判別できるようにしておく。