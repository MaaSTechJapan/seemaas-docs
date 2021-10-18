#####
Graph
#####
Graphは空間を構成しているNodeとEdgeの集合でありグラフ構造そのものである。
空間におけるNode, Edgeの部分的な集合はSub Graphと呼び、具体的には、列車やバスの運行系統を表す。(Sub Graph) ⊂ (Graph)の関係となる。
TraIIReではいずれの集合もGraphと呼ぶ。交通データにおいてGraphは鉄道路線、バス運行系統などを表す。

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
     - f13c6846-e336-069c-90a6-8ac8b65fa9d8
     - Unique idを格納する。
   * - oid
     - String
     - True
     - False
     - JJ
     - 出典があるデータの場合は出典のユニークid、出典がない場合はuidと同一の値を格納する。
   * - title
     - String
     - True
     - False
     - 常磐線・下り
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
     - Graph
     - データが使用している基底の種類を表す。
   * - subtype
     - String
     - True
     - False
     - Railway
     - 同一基底におけるデータのカテゴリを表す。
   * - WKT
     - Well-Know-Text
     - True
     - False
     - LINESTRING ((134.59527,34.48426),(135.00000,35.00000))
     - 地理情報
   * - legs
     - List[Dict{Int:String}]
     - True
     - False
     - [{1:c170e4ec-48e2-2ba8-8157-cf0795efdaa9},{2:b81daeca-8b8e-fb01-8ac6-4dafd198916f},{3:db5280d3-ca7e-6e18-bfb1-64487b1a1478}]
     - Graphを構成するEdgeの集合
   * - operator
     - String
     - True
     - False
     - 1c7f008a-ae84-6763-ae45-6839d83f8995
     - Graphを所有、運営するOperatorのuid




















