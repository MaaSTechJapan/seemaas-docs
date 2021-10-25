############
GeoEssential
############
基底のうち地理情報を取り扱うことが必須のなものが持つ、必須のプロパティを示したものである。エンティティが地物の場合、必ず持つ情報

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
     - 
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
     - 
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
     - 地理情報