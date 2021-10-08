Leg
****
LegはLoadが移動に使用した移動手段毎の乗車地点、降車地点を表現する。
Legは乗降履歴を格納するフォーマットとして設計するが、扱うことができるのは乗降記録と乗り物が特定可能なもののみである。
すなはち、乗降を記録するデバイスが乗り物自体に設置されている場合に限り、Legで取り扱いが可能であるが、
乗降を記録するデバイスが地上固定である場合はLegでは取り扱うことができない。

.. list-table:: Leg
   :widths: 15 10 10 10 10 30
   :header-rows: 1
   
   * - Column
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
     - 
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
     - 2017-07-21T17:32:28+09:00
     - データ生成日時を表す。
   * - issued
     - Timestamp
     - True
     - False
     - 2017-07-21T19:32:28+09:00
     - データ発行日時を表す。
   * - available
     - Timestamp
     - True
     - False
     - 2020-11-01T15:32:45.974412+09:00
     - from_nodeからLegを開始した時刻を表す。具体的にはICカードの乗車時タッチ時などである。
   * - valid
     - Timestamp
     - True
     - False
     - 2020-11-01T15:32:45.974412+09:00
     - to_nodeに到着した時刻を表す。具体的にはICカードの降車時タッチなどである。
   * - type
     - String
     - True
     - False
     - Leg
     - データが使用している基底の種類を表す。
   * - subtype
     - String
     - True
     - False
     - Result
     - データが実績値なのか、予定なのか、予測値なのかを表す。
   * - from_node
     - String
     - True
     - False
     - 630c8f04-9944-c517-8a3f-ab7fe0179731
     - Legを開始したNodeを表す。
   * - to_node
     - String
     - True
     - False
     - 6316e403-4cc1-e314-c824-44ddd77212f7
     - Legを終了したNodeを表す。
   * - transportation
     - String
     - True
     - False
     - 90c1a642-7081-6138-05e3-27bec669b6de
     - 移動に使用した乗り物のを表す。
   * - load
     - String
     - True
     - False
     - 51bc0050-9428-14ef-b018-834d56c4d10b
     - Legとして記録されている利用者の情報をまとめたLoadを表す。
   * - geometry
     - GeoJSON
     - True
     - False
     - {"type": "LineString", "coordinates": [[134.59527,34.48426],[135.00000,35.00000]]}
     - 地理情報
   * - geom
     - Well-Know-Text
     - True
     - False
     - LINESTRING ((134.59527,34.48426),(135.00000,35.00000))
     - 地理情報