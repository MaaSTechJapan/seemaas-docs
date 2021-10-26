Trip
****
Legをtrip chain化したものである。つまり、LoadのODを表すものである。
移動履歴データの中には移動情報に乗り物特定できないもの、一意に決定できないものがあるが、それらデータもすべてTripで扱う。

.. list-table:: Trip
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
     - 497f6eca-6276-4993-bfeb-53cbbbba6f08
     - Entityに対する固有識別子を格納する。
   * - oid
     - String
     - True
     - True
     - 497f6eca-6276-4993-bfeb-53cbbbba6f08
     - 出典があるデータの場合は出典のユニークid、出典がない場合はuidと同一の値を格納する。
   * - title
     - String
     - True
     - False
     - 
     - データ名称を表す、可読性のある文字列を格納する。
   * - created
     - Timestamp
     - True
     - False
     - 
     - データ生成日時を表す。
   * - issued
     - Timestamp
     - True
     - False
     - 
     - データ発行日時を表す。
   * - available
     - Timestamp
     - True
     - False
     - 
     - origin_nodeにおいてTripを開始した時刻
   * - valid
     - Timestamp
     - True
     - False
     - 
     - destination_nodeにおいてTripを終了した時刻
   * - type
     - String
     - True
     - False
     - Trip
     - データが使用している基底の種類を表す。
   * - subtype
     - String
     - False
     - False
     - Prediction
     - 実績データなのか、予定データなのか、予測データなのかを表す。
   * - origin_node
     - String
     - True
     - False
     - 6b4316eb-9bae-3d95-f71b-dd0c9142a73c
     - 移動の出発地Nodeを表す。
   * - destination_node
     - String
     - True
     - False
     - 2ecb2fd2-0c2b-f389-0077-6b7cef043620
     - 移動の目的地Nodeを表す。
   * - legs
     - List[String]
     - True
     - True
     - [630c8f04-9944-c517-8a3f-ab7fe0179731,6316e403-4cc1-e314-c824-44ddd77212f7]
     - 出発地から目的地へ移動するために使用したLegの集合
   * - fare
     - Int
     - True
     - True
     - 580
     - 移動に要した運賃、費用を表す
   * - unit_fare
     - String
     - True
     - True
     - JPY
     - fareの単位 Unit of the fare
   * - load/count
     - float
     - True
     - False
     - 1
     - Loadの積載量
   * - load/unit_count
     - String
     - True
     - False
     - persons
     - countの単位
   * - load/objects
     - List[String]
     - True
     - False
     - [51bc0050-9428-14ef-b018-834d56c4d10b,80bc0050-9428-14ef-b018-834d56c4d10b]
     - 積載しているObjectの一覧
