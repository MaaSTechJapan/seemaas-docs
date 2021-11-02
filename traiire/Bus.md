# Bus

## BusroutePattern
<!-- backwards compatibility -->
<a id="schemabusroutepattern"></a>
<a id="schema_BusroutePattern"></a>
<a id="tocSbusroutepattern"></a>
<a id="tocsbusroutepattern"></a>

```json
{
  "basetype": "Graph",
  "type": "BusroutePattern"
}

```

Graph::BusroutePattern



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Graph::BusroutePattern|any|false|none|BusroutePatternはTraIIReにおけるGraphを継承する。BusroutePatternはバスの運行系統を表すモデルである。<br>BusroutePattern inherits the Graph of the TraIIRe. The BusroutePattern represents the operation route of the Bus.|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[./TraIIRe.yamlGraph](#schema./traiire.yamlgraph)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» basetype|string|true|none|none|
|» type|string|true|none|BusroutePatternに固定<br>Fixed to the BusroutePattern|

## Bus
<!-- backwards compatibility -->
<a id="schemabus"></a>
<a id="schema_Bus"></a>
<a id="tocSbus"></a>
<a id="tocsbus"></a>

```json
{
  "basetype": "Transportation",
  "type": "Bus",
  "additional": {
    "head_sign": "string"
  }
}

```

Transportation::Bus



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Transportation::Bus|any|false|none|BusはTraIIReにおけるTransportationを継承する。Busはバス車両を表すモデルである。Busは運行事業者や運行系統名、名称などの運行に関わる情報をもつ。<br>The Bus inherits the Transportation in TraIIRe. The Bus represents a bus vehicle. The Bus has the operation related information such as the operator, operation route and name.|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[./TraIIRe.yamlTransportation](#schema./traiire.yamltransportation)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» basetype|string|true|none|none|
|» type|string|true|none|none|
|» additional|object|false|none|none|
|»» head_sign|string|false|none|案内用行先案内<br>The bus information of distination|

## Busstop
<!-- backwards compatibility -->
<a id="schemabusstop"></a>
<a id="schema_Busstop"></a>
<a id="tocSbusstop"></a>
<a id="tocsbusstop"></a>

```json
{
  "basetype": "Node",
  "type": "Busstop"
}

```

Node::Busstop



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Node::Busstop|any|false|none|BusstopはTraIIReにおけるNodeを継承する。Busstopはバス停を表すモデルであるが、実際にバスが停車するバス停標柱を表すものではなく、バス停の存在を表す抽象的なものである。同一の存在はTrain::Stationである。バス停の存在とバス停標柱の関係を分離しておくことで、大規模なバス停や、同一バス停でも往路復路で標柱が異なる場合に、それぞれの乗り場を生成することで詳細な表現が可能になる。<br>Busstop inherits the Node in TraIIRe. The Busstop represents a bus stop but it is not a bus stop pole that the bus stops. This is an abstruct expression of the bus stop. Train::Station is the same philosophy. By separating the relationship between the existence of a bus stop and the bus stop pole, it is possible to generate a detailed representation of a large bus stop or a different pole for in the same bus stop on the inbound and outbound by generating the respective boarding area.|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[./TraIIRe.yamlNode](#schema./traiire.yamlnode)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» basetype|string|true|none|none|
|» type|string|true|none|none|

## BusstopTimetable
<!-- backwards compatibility -->
<a id="schemabusstoptimetable"></a>
<a id="schema_BusstopTimetable"></a>
<a id="tocSbusstoptimetable"></a>
<a id="tocsbusstoptimetable"></a>

```json
{
  "basetype": "Edgetime",
  "type": "BusTimetable",
  "arrival_time": "08:50:00",
  "departure_time": "09:00:00",
  "transportation": "string"
}

```

Edgetime::BusTimetable



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Edgetime::BusTimetable|any|false|none|BusTimetableはTraIIReにおけるTimetableを継承する。BusTimetableはあるバスの情報を停車バス停でスライスしたものである。BusTimetableをBusroutePattern別、行先別に集計することにより、あるバス停の時刻表を表現できる。<br>The BusTimetable inherits the Timetable in TraIIRe. The BusTimetable is a slice of a bus information by its stop. Aggregating BusTimetable by BusroutePattern and destination, the timetable of a bus stop can be represented.|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[./TraIIRe.yamlEdgetime](#schema./traiire.yamledgetime)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» basetype|string|true|none|none|
|» type|string|true|none|none|
|» arrival_time|string,null(time)|true|none|Busstopへの到着時刻<br>The arrival time of the Busstop|
|» departure_time|string,null(time)|true|none|Busstopの出発時刻<br>The departure time of the Busstop|
|» transportation|string|true|none|Busのid<br>The id of the Bus|

## Busroute
<!-- backwards compatibility -->
<a id="schemabusroute"></a>
<a id="schema_Busroute"></a>
<a id="tocSbusroute"></a>
<a id="tocsbusroute"></a>

```json
{
  "basetype": "Edge",
  "type": "Busroute",
  "from_node": "string",
  "to_node": "string"
}

```

Edge::Busroute



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Edge::Busroute|any|false|none|BusrouteはTraIIReにおけるEdgeを継承する。BusrouteはBusstop同士の接続を表すエッジである。<br>The Busroute inherits the Edge in TraIIRe. The Busroute is the edge that connects the Busstops.|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[./TraIIRe.yamlEdge](#schema./traiire.yamledge)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» basetype|string|true|none|none|
|» type|string|true|none|none|
|» from_node|string|true|none|始点のBusstopのid<br>The id of the starting Busstop|
|» to_node|string|true|none|終点のBusstopのid<br>The id of the ending Busstop|

