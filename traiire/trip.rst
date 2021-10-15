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
     - Primary keyを格納する。
   * - uid
     - String
     - True
     - False
     - 497f6eca-6276-4993-bfeb-53cbbbba6f08
     - Unique idを格納する。
   * - oid
     - String
     - True
     - False
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
     - True
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
   * - load
     - String
     - True
     - False
     - 51bc0050-9428-14ef-b018-834d56c4d10b
     - Tripとして記録されている利用者の情報をまとめたLoadを表す。
   * - WKT
     - Well-Know-Text
     - True
     - True
     - LineString((134.59527,34.48426),(135.00000,35.00000))
     - 地理情報