# PersonTravel

## Trip
<!-- backwards compatibility -->
<a id="schematrip"></a>
<a id="schema_Trip"></a>
<a id="tocStrip"></a>
<a id="tocstrip"></a>

```json
{
  "oid": "string",
  "basetype": "Trip",
  "type": "Trip"
}

```

Trip::Trip



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Trip::Trip|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[./TraIIRe.yamlTrip](#schema./traiire.yamltrip)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» oid|string|false|none|決済に使用したcard_id|
|» basetype|string|true|none|none|
|» type|string|true|none|none|

## Leg
<!-- backwards compatibility -->
<a id="schemaleg"></a>
<a id="schema_Leg"></a>
<a id="tocSleg"></a>
<a id="tocsleg"></a>

```json
{
  "basetype": "Leg",
  "type": "Leg",
  "note": "string",
  "using_pass": false
}

```

Leg::Leg



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Leg::Leg|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[./TraIIRe.yamlLeg](#schema./traiire.yamlleg)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» basetype|string|true|none|none|
|» type|string|true|none|none|
|» note|string|false|none|特記事項、使用したフリーパスの名称などを文字列で表す|
|» using_pass|boolean|true|none|定期券を使用したかどうか|

## Person
<!-- backwards compatibility -->
<a id="schemaperson"></a>
<a id="schema_Person"></a>
<a id="tocSperson"></a>
<a id="tocsperson"></a>

```json
{
  "basetype": "Load",
  "type": "Person",
  "gender": 0,
  "age": 0,
  "adults": "string"
}

```

Load::Person



|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Load::Person|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[./TraIIRe.yamlLoad](#schema./traiire.yamlload)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» basetype|string|true|none|none|
|» type|string|true|none|none|
|» gender|integer(int64)|true|none|性別を表す 男性:0, 女性:1, その他:2|
|» age|integer(int64)|true|none|年齢を表す|
|» adults|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|gender|0|
|gender|1|
|gender|2|

