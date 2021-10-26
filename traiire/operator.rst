Operator
********
Operatorは実体を運用・保守・管理する組織を表す。実空間ではNode, Edge, Transportationは必ず運営母体を持つ。Operatorこの運営母体を表現する

.. list-table:: Operator
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
     - True
     - 
     - 法人番号
   * - title
     - String
     - True
     - False
     - 
     - 商号又は名称
   * - created
     - Timestamp
     - True
     - False
     - 
     - 法人番号指定年月日
   * - issued
     - Timestamp
     - True
     - False
     - 
     - 法人番号指定年月日
   * - available
     - Timestamp
     - True
     - False
     - 
     - 事由発生年月日
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
     - Operator
     - データが使用している基底の種類を表す。
   * - subtype
     - String
     - True
     - False
     - 
     - 同一基底におけるデータのカテゴリを表す。
   * - wkt
     - Well-Know-Text
     - True
     - False
     - POINT (134.59527 34.48426)
     - 本店又は主たる事務所の所在地をgeocodingしたもの