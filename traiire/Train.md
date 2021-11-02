# Train

## Station
<!-- backwards compatibility -->
<a id="schemastation"></a>
<a id="schema_Station"></a>
<a id="tocSstation"></a>
<a id="tocsstation"></a>

```json
{
  "basetype": "Node",
  "type": "Station",
  "additional": {
    "station_title": "string"
  }
}

```

Node::Station



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Node::Station|any|false|none|Stationは駅を表す。駅とは列車に乗るためのプラットフォームではなく、人間の認知としての駅である。<br>The Station represents a station. A station is not a platform for getting on a train but a station as a human recognition.|

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
|» additional|object|false|none|none|
|»» station_title|string|false|none|駅名(多言語対応)<br>Station name (Multillingual support)|

## Railway
<!-- backwards compatibility -->
<a id="schemarailway"></a>
<a id="schema_Railway"></a>
<a id="tocSrailway"></a>
<a id="tocsrailway"></a>

```json
{
  "basetype": "string",
  "type": "Railway",
  "from_node": "string",
  "to_node": "string"
}

```

Edge::Railway



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Edge::Railway|any|false|none|RailwayはStation同士を結ぶ鉄道路線を表す。 <br>The Railway represents a railway connecting the Stations.|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[./TraIIRe.yamlEdge](#schema./traiire.yamledge)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» basetype|string|true|none|Edge|
|» type|string|true|none|Railwayに固定<br>Fixed to the Railway|
|» from_node|string|true|none|始点のStationのid<br>The id of the starting Station|
|» to_node|string|true|none|終点のStationのid<br>The id of the ending Station|

## OperationRailway
<!-- backwards compatibility -->
<a id="schemaoperationrailway"></a>
<a id="schema_OperationRailway"></a>
<a id="tocSoperationrailway"></a>
<a id="tocsoperationrailway"></a>

```json
{
  "basetype": "Graph",
  "type": "OperationRailway",
  "edges": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "additional": {
    "nickname": "string"
  }
}

```

Graph::OperationRailway



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Graph::OperationRailway|any|false|none|OperationRailwayはTrainが所属する運行系統を表す。<br>The OperationRailway represents the operation railway on which the train is operated.|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[./TraIIRe.yamlGraph](#schema./traiire.yamlgraph)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» basetype|string|false|none|none|
|» type|string|true|none|OperationRailwayに固定<br>Fixed to the OperationRailway|
|» edges|[string]|true|none|運行路線に含まれるRailroadを、終点のPlatformと始点のPlatformが一致するように並べた配列<br>Array of the Railroad which is included in a operation railway, with the Platform at the end coinciding with the Platform at the beginning|
|» additional|object|false|none|none|
|»» nickname|string|false|none|路線愛称名<br>Railway nickname|

## TrainEdgetime
<!-- backwards compatibility -->
<a id="schematrainedgetime"></a>
<a id="schema_TrainEdgetime"></a>
<a id="tocStrainedgetime"></a>
<a id="tocstrainedgetime"></a>

```json
{
  "type": "TrainTimetable",
  "basetype": "Edgetime",
  "transportation": "string",
  "additional": {
    "coupled_train": "string"
  }
}

```

Edgetime::TrainEdgetime



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Edgetime::TrainEdgetime|any|false|none|TimeTimetableは駅における時刻表を表す。The TrainTimetable represents for the timetable in the station.|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[./TraIIRe.yamlEdgetime](#schema./traiire.yamledgetime)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» type|string|true|none|none|
|» basetype|string|true|none|none|
|» transportation|string|true|none|Trainのid<br>The id of the Train|
|» additional|object|false|none|none|
|»» coupled_train|string|false|none|この列車に連結されている列車のid<br>The id of the train which coupled to this Train|

## Train
<!-- backwards compatibility -->
<a id="schematrain"></a>
<a id="schema_Train"></a>
<a id="tocStrain"></a>
<a id="tocstrain"></a>

```json
{
  "title": "621M",
  "basetype": "Transportation",
  "type": "Train",
  "additional": {
    "head_sign": "string"
  }
}

```

Transportation::Train



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Transportation::Train|any|false|none|Trainは列車を表す。<br>The Train represents a rolling stock of railway.|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[./TraIIRe.yamlTransportation](#schema./traiire.yamltransportation)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» title|string|true|none|列車番号<br>Operation number of the Train|
|» basetype|string|true|none|none|
|» type|string|true|none|none|
|» additional|object|false|none|none|
|»» head_sign|string|false|none|案内用行先案内<br>The train information of distination|

