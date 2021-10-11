Edge
****

2つのNodeの関係を方向とともに表すベクトルであり、グラフ構造における辺に対応する。
交通データにおいてEdgeとは駅間の線路、バス停間の道路などを表す。
Edgeはグラフ構造における辺を表し、Nodeのつながりを定義する。
”起点から終点へ行く”という表現であり、必ず2つのNodeを結ぶ有向エッジになる、
Edgeは運行事業者が所有するものとする。

- Edge::Railway
- Edge::Busroute
- Edge::Airroute
- Edge::Searoute
- Edge::Walkroute

.. list-table:: Edge
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
     - md5(f”{from_node},{to_node}”)
     - 起点と終点の2つのNodeのuidをセパレータのカンマ(,)で区切った文字列をmd5ハッシュ値化したものである。
   * - oid
     - String
     - True
     - False
     - f"{from_node},{to_node}"
     - 起点と終点の2つのNodeのuidをセパレータのカンマ(,)で区切った文字列である。
   * - title
     - String
     - True
     - False
     - f"{from_node.title},{to_node.title}"
     - 起点と終点の2つの地物名称をセパレータのカンマ(,)で区切ったものである。
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
     - Edge
     - データが使用している基底の種類を表す。
   * - subtype
     - String
     - True
     - False
     - Railway
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
     - 始点側のNode
   * - to_node
     - String
     - True
     - False
     - 70e25ccc-82d2-fec2-faf5-2841720287a0
     - 終点側のNode
   * - geometry
     - GeoJSON
     - True
     - False
     - {"type": "LineString", "coordinates": [[134.59527,34.48426],[135.00000,35.00000]]}
     - 出典におけるLine形状
   * - geom
     - Well-Know-Text
     - True
     - False
     - LINESTRING ((134.59527,34.48426),(135.00000,35.00000))
     - 出典におけるLine形状