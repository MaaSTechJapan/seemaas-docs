Edgetime
********
EdgetimeはEdgeに時刻情報を付加したものである。
移動データにおける時刻表に相当する情報である。

.. list-table:: Edgetime
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
     - 
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
     - 上野,日暮里,0511
     - データ名称を表す、可読性のある文字列を格納する。
   * - created
     - Timestamp
     - True
     - False
     - 2021-04-01T00:00:00
     - データ生成日時を表す。
   * - issued
     - Timestamp
     - True
     - False
     - 2021-04-01T00:00:00
     - データ発行日時を表す。
   * - available
     - Timestamp
     - True
     - False
     - 2021-04-01T00:00:00
     - データ有効化日時を表す。
   * - valid
     - Timestamp
     - True
     - False
     - 2021-09-30T23:59:59
     - データ有効期限を表す。
   * - type
     - String
     - True
     - False
     - Edgetime
     - データが使用している基底の種類を表す。
   * - subtype
     - String
     - True
     - False
     - 
     - 同一基底におけるデータのカテゴリを表す。
   * - edge
     - String
     - True
     - False
     - 
     - edgeのuid
   * - departure_time
     - Timestamp
     - True
     - False
     - 1970-01-01T05:11:00
     - Edge始点の出発時刻
   * - arrival_time
     - Timestamp
     - True
     - False
     - 1970-01-01T05:13:00
     - Edge終点への到着時刻
   * - geton_type
     - Int
     - True
     - False
     - 1
     - Edge始点で乗り物に乗車可能かを表す(乗車可能:1, 乗車不可:0)。
   * - getoff_type
     - Int
     - True
     - False
     - 1
     - Edge終点で乗り物から下車可能かを表す(下車可能:1, 下車不可:0)。
   * - transportation
     - String
     - True
     - False
     - 
     - transportationのuid
   * - calendar
     - List[Int]
     - True
     - False
     - [1,1,1,1,1,0,0,0]
     - 運行曜日を8bitであらわす
   * - operation_day
     - String
     - True
     - False
     - [Timestamp]
     - 運行日
   * - exception_day
     - String
     - True
     - False
     - [Timestamp]
     - 除外日