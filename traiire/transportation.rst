##############
Transportation
##############
移動手段である。鉄道車両、バス車両、タクシー車両などの移動体の表現するのに加え、徒歩といった移動体として実体のない移動手段も同一の基底で表現する。
subtypeは下記から選択するものとする

* subtype
  
  * Train
  * Bus
  * Airplane
  * Ship
  * Walk
  * Car
  * Bicycle

.. list-table:: Transportation
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
     - 531H
     - 列車番号、運行管理番号など乗り物を表す名称
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
     - データ有効化日時を表す。
   * - valid
     - Timestamp
     - True
     - False
     - 
     - データ有効期限を表す。
   * - type
     - String
     - True
     - False
     - Transportation
     - データが使用している基底の種類を表す。
   * - subtype
     - String
     - True
     - False
     - Train
     - 同一基底におけるデータのカテゴリを表す。
   * - operator
     - String
     - True
     - False
     - 1c7f008a-ae84-6763-ae45-6839d83f8995
     - Nodeを所有、運営するOperatorのuid
   * - from_node
     - String
     - True
     - False
     - 5619904b-52a8-a672-cb76-dd372b98f839
     - 乗り物の始発側のNode
   * - to_node
     - String
     - True
     - False
     - 70e25ccc-82d2-fec2-faf5-2841720287a0
     - 乗り物の終点側のNode