# TraIIRe

## Essential
<!-- backwards compatibility -->
<a id="schemaessential"></a>
<a id="schema_Essential"></a>
<a id="tocSessential"></a>
<a id="tocsessential"></a>

```json
{
  "id": "string",
  "uid": "string",
  "oid": "string",
  "title": "string",
  "created": "2017-07-21T17:32:28+09:00",
  "issued": "2017-07-21T19:32:28+09:00",
  "available": "2017-07-22T00:00:00+09:00",
  "valid": "2017-07-24T23:59:59+09:00",
  "basetype": "string",
  "type": "string",
  "subtype": "string",
  "wkt": "string",
  "note": "string"
}

```

Essential



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|データに対する固有識別子(UUIDv4) The unique identifier for Data.|
|uid|string|true|none|実体(Entity)に対する固有識別子 The unique identifier For Entity. e.g. Station, Busstop, Airport, etc..|
|oid|string|false|none|none|
|title|string|true|none|正式名称を格納する(該当ない場合は一般的な呼称でもよい) The official name is stored, or the common name is acceptable.|
|created|string(date-time)|true|none|データ生成日時 The date of created.|
|issued|string(date-time)|true|none|データ発行日時 The date of issued.|
|available|string(date-time)|true|none|データ有効化日時 The date of activation.|
|valid|string(date-time)|true|none|データ有効期限(nullは無期限を表す) The date of expired. The null respresents indefinite period.|
|basetype|string|true|none|継承元の基底クラスを表す|
|type|string|true|none|クラス名（e.g. Station, Railway） The name of the class (e.g. Station, Railway).|
|subtype|string|false|none|計画、予測、実績など時系列方向の種類を表す|
|wkt|string|false|none|地理情報を表す|
|note|string|false|none|特記事項|

## Node
<!-- backwards compatibility -->
<a id="schemanode"></a>
<a id="schema_Node"></a>
<a id="tocSnode"></a>
<a id="tocsnode"></a>

```json
{
  "id": "string",
  "uid": "string",
  "oid": "string",
  "title": "string",
  "created": "2017-07-21T17:32:28+09:00",
  "issued": "2017-07-21T19:32:28+09:00",
  "available": "2017-07-22T00:00:00+09:00",
  "valid": "2017-07-24T23:59:59+09:00",
  "basetype": "string",
  "type": "Node",
  "subtype": "string",
  "wkt": "string",
  "note": "string",
  "operator": "string",
  "address": "string",
  "h3": "string"
}

```

Node



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Node|any|false|none|Nodeはグラフ構造における頂点を表す。<br>The Node reperesents for a vertex in a graph structure.|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Essential](#schemaessential)|false|none|Essentialは全てのデータがもつ基底データを定義したものである。<br>The Essential defines the base data that each data have to keep.|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» type|string|true|none|Node|
|» operator|string|true|none|運行事業者のuid|
|» address|string,null|false|none|wktを可読性のある住所に読み替えたもの|
|» h3|string|true|none|対象地物が含まれるh3（基本はResolution.10を使用）|

## Edge
<!-- backwards compatibility -->
<a id="schemaedge"></a>
<a id="schema_Edge"></a>
<a id="tocSedge"></a>
<a id="tocsedge"></a>

```json
{
  "id": "string",
  "uid": "string",
  "oid": "string",
  "title": "string",
  "created": "2017-07-21T17:32:28+09:00",
  "issued": "2017-07-21T19:32:28+09:00",
  "available": "2017-07-22T00:00:00+09:00",
  "valid": "2017-07-24T23:59:59+09:00",
  "basetype": "string",
  "type": "string",
  "subtype": "string",
  "wkt": "string",
  "note": "string",
  "operator": "string",
  "from_node": "string",
  "to_node": "string"
}

```

Edge



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Edge|any|false|none|TraIIReグラフ構造における辺を表す。<br>The Edge represents for an edge in a TraIIRe graph structure.|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Essential](#schemaessential)|false|none|Essentialは全てのデータがもつ基底データを定義したものである。<br>The Essential defines the base data that each data have to keep.|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» operator|string|true|none|運行事業者のuid|
|» from_node|string|true|none|始点Nodeのid<br>The id of starting Node|
|» to_node|string|true|none|終点Nodeのid<br>The ID of ending Node|

## Graph
<!-- backwards compatibility -->
<a id="schemagraph"></a>
<a id="schema_Graph"></a>
<a id="tocSgraph"></a>
<a id="tocsgraph"></a>

```json
{
  "id": "string",
  "uid": "string",
  "oid": "string",
  "title": "string",
  "created": "2017-07-21T17:32:28+09:00",
  "issued": "2017-07-21T19:32:28+09:00",
  "available": "2017-07-22T00:00:00+09:00",
  "valid": "2017-07-24T23:59:59+09:00",
  "basetype": "string",
  "type": "string",
  "subtype": "string",
  "wkt": "string",
  "note": "string",
  "operator": "string",
  "edges": [
    "string"
  ]
}

```

Graph



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Graph|any|false|none|GraphはTraIIReグラフ構造におけるEdgeの集合である。<br>The Graph is the whole set of Node and Edge in a graph structure.|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Essential](#schemaessential)|false|none|Essentialは全てのデータがもつ基底データを定義したものである。<br>The Essential defines the base data that each data have to keep.|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» operator|string|true|none|運行事業者のuid|
|» edges|[string]|true|none|Graphとして名称がつけられたEdge_idのarray An array of Edge_id named as Graph|

## Transportation
<!-- backwards compatibility -->
<a id="schematransportation"></a>
<a id="schema_Transportation"></a>
<a id="tocStransportation"></a>
<a id="tocstransportation"></a>

```json
{
  "id": "string",
  "uid": "string",
  "oid": "string",
  "title": "string",
  "created": "2017-07-21T17:32:28+09:00",
  "issued": "2017-07-21T19:32:28+09:00",
  "available": "2017-07-22T00:00:00+09:00",
  "valid": "2017-07-24T23:59:59+09:00",
  "basetype": "string",
  "type": "string",
  "subtype": "string",
  "wkt": "string",
  "note": "string",
  "operator": "string",
  "from_node": "string",
  "to_node": "string"
}

```

Transportation



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Transportation|any|false|none|TransportationはGraph上を移動する実体を表す。<br>The Transportation represents an entity that moves on a graph structure.|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Essential](#schemaessential)|false|none|Essentialは全てのデータがもつ基底データを定義したものである。<br>The Essential defines the base data that each data have to keep.|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» operator|string|true|none|運行事業者のid|
|» from_node|string|true|none|始発のNodeのid<br>The id of the first Node|
|» to_node|string|true|none|終点のNodeのid<br>The id of the final Node|

## Edgetime
<!-- backwards compatibility -->
<a id="schemaedgetime"></a>
<a id="schema_Edgetime"></a>
<a id="tocSedgetime"></a>
<a id="tocsedgetime"></a>

```json
{
  "id": "string",
  "uid": "string",
  "oid": "string",
  "title": "string",
  "created": "2017-07-21T17:32:28+09:00",
  "issued": "2017-07-21T19:32:28+09:00",
  "available": "2017-07-22T00:00:00+09:00",
  "valid": "2017-07-24T23:59:59+09:00",
  "basetype": "string",
  "type": "string",
  "subtype": "string",
  "wkt": "string",
  "note": "string",
  "sequence": 0,
  "edge": "string",
  "departure_time": "1970-01-01T13:34:45+09:00",
  "arrival_time": "1970-01-01T13:34:45+09:00",
  "geton_type": 0,
  "getoff_type": 0,
  "transportation": "string",
  "graph": "string",
  "calender": [
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    0
  ],
  "operation_days": [
    0
  ],
  "exception_days": [
    0
  ]
}

```

Edgetime



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Edgetime|any|false|none|EdgetimeはあるEdgeにおけるTrainsportationの時刻表を表す。<br>The Timetable represents for a timetable in the Node.|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Essential](#schemaessential)|false|none|Essentialは全てのデータがもつ基底データを定義したものである。<br>The Essential defines the base data that each data have to keep.|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» sequence|integer|true|none|順序、1始まり<br>Order begining from 1|
|» edge|string|true|none|Transportationが通過するEdge|
|» departure_time|string,null(date-time)|true|none|Nodeからの出発時刻<br>The time of deperture from the Node|
|» arrival_time|string,null(date-time)|true|none|Nodeへの到着時刻<br>The time arrival at the Node|
|» geton_type|integer|true|none|'1: 乗車可 Enables to get on'<br>'0: 乗車不可 Unables to get on'|
|» getoff_type|integer|true|none|'1:下車可 Enables to get off'<br>'0:下車不可 Unables to get off'|
|» transportation|string|true|none|Transportationのid<br>The id of the Transportation|
|» graph|string,null|true|none|Nodeが属しているGraphのid<br>The id of the Graph to which the Node belongs.|
|» calender|[integer]|true|none|この時刻表で運行される曜日。SPECIFICDAYが指定された場合、operation_daysに記載された日付群を参照<br>The day of the week that operator uses this timetable. If SPECIFICDAY is selected, the days in operation_days is necessary|
|» operation_days|[number]|false|none|特定の日付に運行される場合のISO8601日付リスト<br>The list of specific day with ISO8601 format when the SPECIFCDAY is selected|
|» exception_days|[number]|false|none|特定の日付に運行されない場合のISO8601日付リスト<br>The list of specific day with ISO8601 format when the SPECIFCDAY is selected|

#### Enumerated Values

|Property|Value|
|---|---|
|geton_type|0|
|geton_type|1|
|getoff_type|0|
|getoff_type|1|

## Trip
<!-- backwards compatibility -->
<a id="schematrip"></a>
<a id="schema_Trip"></a>
<a id="tocStrip"></a>
<a id="tocstrip"></a>

```json
{
  "id": "string",
  "uid": "string",
  "oid": "string",
  "title": "string",
  "created": "2017-07-21T17:32:28+09:00",
  "issued": "2017-07-21T19:32:28+09:00",
  "available": "2017-07-22T00:00:00+09:00",
  "valid": "2017-07-24T23:59:59+09:00",
  "basetype": "string",
  "type": "string",
  "subtype": "string",
  "wkt": "string",
  "note": "string",
  "origin_node": "string",
  "destination_node": "string",
  "legs": [
    "string"
  ],
  "fare": 0,
  "unit_fare": "JPY",
  "load": "string"
}

```

Trip



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Trip|any|false|none|TripはLoadの移動経路を表現する。<br>The Trip represents the route of the Load's movement.|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Essential](#schemaessential)|false|none|Essentialは全てのデータがもつ基底データを定義したものである。<br>The Essential defines the base data that each data have to keep.|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» oid|string|false|none|ICカードの番号等|
|» origin_node|string,null|true|none|Tripの起点となるNode<br>The starting Node of the Trip|
|» destination_node|string,null|true|none|Tripの終点となるNode<br>The terminal Node of the Trip|
|» legs|[string]|true|none|Tripが経由するleg_idのarray An array of leg_id that the Trip goes through|
|» fare|integer(float)|true|none|Loadを積載して移動することで発生する収入。legsであらわされているLeg::fareの合算値となる。|
|» unit_fare|string|true|none|fareの単位 Unit of the fare|
|» load|string|false|none|Tripとして記録されている利用者の情報をまとめたLoadのuid|

## Leg
<!-- backwards compatibility -->
<a id="schemaleg"></a>
<a id="schema_Leg"></a>
<a id="tocSleg"></a>
<a id="tocsleg"></a>

```json
{
  "id": "string",
  "uid": "string",
  "oid": "string",
  "title": "string",
  "created": "2017-07-21T17:32:28+09:00",
  "issued": "2017-07-21T19:32:28+09:00",
  "available": "2017-07-22T00:00:00+09:00",
  "valid": "2017-07-24T23:59:59+09:00",
  "basetype": "string",
  "type": "string",
  "subtype": "string",
  "wkt": "string",
  "note": "string",
  "from_node": "string",
  "to_node": "string",
  "transportation": "string",
  "fare": 0,
  "unit_fare": "string"
}

```

Leg



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Leg|any|false|none|LegはLoadが移動に使用した移動手段毎の乗車地点、降車地点を表現する。|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Essential](#schemaessential)|false|none|Essentialは全てのデータがもつ基底データを定義したものである。<br>The Essential defines the base data that each data have to keep.|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» from_node|string|true|none|Legを開始したNodeを表す|
|» to_node|string|true|none|Legを終了したNodeを表す|
|» transportation|string|true|none|移動に使用した乗り物のuid|
|» fare|number|true|none|移動に要した運賃、費用を表す|
|» unit_fare|string|true|none|fareの単位 Unit of the fare|

## Operator
<!-- backwards compatibility -->
<a id="schemaoperator"></a>
<a id="schema_Operator"></a>
<a id="tocSoperator"></a>
<a id="tocsoperator"></a>

```json
{
  "id": "string",
  "uid": "string",
  "oid": "string",
  "title": "string",
  "created": "2017-07-21T17:32:28+09:00",
  "issued": "2017-07-21T19:32:28+09:00",
  "available": "2017-07-22T00:00:00+09:00",
  "valid": "2017-07-24T23:59:59+09:00",
  "basetype": "string",
  "type": "string",
  "subtype": "string",
  "wkt": "string",
  "note": "string"
}

```

Operator



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Operator|[Essential](#schemaessential)|false|none|Operatorは実体を運用・保守・管理する組織を表す。<br>The Operator represents for an organization that operates, maintains, and manages the entity.|

## Load
<!-- backwards compatibility -->
<a id="schemaload"></a>
<a id="schema_Load"></a>
<a id="tocSload"></a>
<a id="tocsload"></a>

```json
{
  "id": "string",
  "uid": "string",
  "oid": "string",
  "title": "string",
  "created": "2017-07-21T17:32:28+09:00",
  "issued": "2017-07-21T19:32:28+09:00",
  "available": "2017-07-22T00:00:00+09:00",
  "valid": "2017-07-24T23:59:59+09:00",
  "basetype": "string",
  "type": "string",
  "subtype": "string",
  "wkt": "string",
  "note": "string",
  "count": "string",
  "unit_count": "string"
}

```

LoadはTransportationに積載される主体の属性を表す。Loadはヒトを表すこともあれば、複数の人、貨物を表すことができる。どのような現実の主体を表すかは継承先で規定し、名称はtypeで表す。



allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[Essential](#schemaessential)|false|none|Essentialは全てのデータがもつ基底データを定義したものである。<br>The Essential defines the base data that each data have to keep.|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» oid|string|false|none|ユーザを一意に表すID等|
|» count|string|true|none|Loadの積載量 The amount of the Load|
|» unit_count|string|true|none|countの単位 Unit of the count|

