Load
****
LoadはTransportationに積載され移動する主体を集計したものである。具体的にはヒト、モノ、動物、貨物などである。

.. list-table:: Load
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
     - True
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
     - データ有効化日時を表す。移動履歴データの場合はTripやLegと一致する。
   * - valid
     - Timestamp
     - True
     - False
     - 
     - データ有効期限を表す。移動履歴データの場合はTripやLegと一致する。
   * - type
     - String
     - True
     - False
     - Load
     - データが使用している基底の種類を表す。
   * - subtype
     - String
     - True
     - False
     - 
     - 実績データなのか、予定データなのか、予測データなのかを表す。
   * - count
     - float
     - True
     - False
     - 1.0
     - 人数の合計、重さとっいった乗り物によって移動した実体の量を表す。
   * - count_unit
     - String
     - True
     - False
     - person
     - countの単位を表す。
   * - persons
     - List[String]
     - True
     - True
     - [7cc6404d-cc46-ce30-79ed-e0e6214b7eb1, 65fa4cf7-a53a-4133-8c2a-2e01a13547e8, b1025dc8-21de-7eaf-c2e3-b91da51aa0e5, 778ba0b0-ac39-c1fe-4213-ddb27becdd4a]
     - Loadを構成しているPersonの集合を表す。
   * - fare
     - Int
     - True
     - True
     - 580
     - 移動に要した運賃、費用を表す
