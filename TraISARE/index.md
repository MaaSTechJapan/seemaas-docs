概要 Abstract
=============

交通システムの高度化により、移動手段の多様化が進んでいるしかしながら各交通システムは事業者毎に異なったシステムが運用されており、シームレスな移動を実現するためのデータ処理に問題を抱えている。これらを解決するTraISARE:Transport
Information Store with Aggregator, Receiver and
Encoderを提案し、実装する。

With the advancement of transportation systems, diversification of
transportation means is progressing. However, each transportation system
has a different system operation for each business operator and has a
problem with data processing for realizing seamless movement. To solve
these problems, we propose and implement TraISARE: Transport Information
Store with Aggregator, Receiver and Encoder.

背景 Background
===============

公共交通情報の統一フォーマットのデファクトスタンダードと言えるのが、[GTFS](https://developers.google.com/transit/?hl=ja)である。これは交通事業者が駅、バス停、時刻表、ルートなどの情報を記述するために規定されたデータフォーマットである。元々Google
Mapsで公共交通情報を処理するために規定されたフォーマットであるが、現在は一般にも公開され、事業者によってはオープンデータとして配布しているケースもある。このフォーマットの最大のメリットは、作成したデータを登録することでGoogle
Maps上へ情報を表示・検索できるようになることである。中小の事業者では自社でスマートフォンサービスをメンテナンスすることが難しい場合があり、データを用意するだけで世界最大の地図基盤に情報提供をできるメリットは大きい。しかし、欧米発祥ということもあり日本の交通事情に即していないケースも見受けられるため、最近では国土交通省より[標準的なバス情報フォーマット](http://www.mlit.go.jp/sogoseisaku/transport/sosei_transport_tk_000067.html)としてGTFSを拡張した仕様を公開している。鉄道に関しては、まだ日本の事情に即したフォーマットは提供されていない。

日本の公共交通情報の提供としては、公共交通オープンデータ協議会(ODPT)が挙げられる。現在59事業者が参画しており、商用利用可能な形で10事業者がデータの公開を行なっている。ODPTでは鉄道、バス、航空機の情報を提供している。  
また海外では公共交通情報をオープンデータとして提供するトレンドが2014年頃より広がり、ロンドンにおける[TfL](https://tfl.gov.uk/)、フィンランドにおける[DigiTraffic](https://www.digitraffic.fi/en/)、サンフランシスコ市における[SFMTA](https://www.sfmta.com/reports/gtfs-transit-data)など数多くの公共交通情報が提供されるようになってきている。これら諸外国では、交通機関は官営あるいは一社独占で提供する場合が多く、データの提供を開始する場合は、すべての交通機関のデータを一括して提供することが可能である。  
日本ではJRグループとその他私鉄、更にバス事業者、タクシー事業者といった数多くのステークホルダーが存在し、それぞれの経営判断や社内事情などもあって、データを一括して提供するといった事業は、1事業者だけでは実現困難と言える。加えて各社から配信されるデータが異なるという事情が、この問題を更に困難にしている。データはGTFS形式である程度統一されているが、事業者毎に異なる基幹システム、各社の事情を考慮した情報量の担保、加えてGTFS以上の情報量を持たせることなどの事業者毎の課題を吸収しなければならない。

[GTFS](https://developers.google.com/transit/?hl=ja) is the de facto
standard for the unified format of public transportation information.
This is a data format defined for transportation companies to describe
information such as stations, bus stops, timetables, and routes.
Originally it was a format specified by Google Maps to process such
public transportation information. Now it is open to the public, and
some operators distribute it as open data. The biggest advantage of this
format is to enable the Google maps to display and search it by
registering the data. It is the benefit for some smaller operators, who
are difficult to maintain their own smartphone services, to provide
their information to the larget map platform in the world simply by
preparing data. However, sometimes it does not match the traffic
conditions in Japan because it is a western-oriented platform, and the
extended GTFS as a standard bus information format start to release by
the Ministry of Land, Infrastructure, Transport and Tourism. Regarding
to railways, the format that suits the circumstances of Japan has not
been provided.

The association for open data of public transportation (ODPT) is one of
the provider of public transport information in Japan. Currently, 59
companies are participating, and 10 companies are publishing data that
can be used for commercial purposes. ODPT provides rail, bus and
aircraft information.  
It is gradually increasing in overseas to provide public transportation
information as open data since around 2014. Many public transportation
information such as [TfL](https://tfl.gov.uk/) in London,
[DigiTraffic](https://www.digitraffic.fi/en/) in Finland, and
[SFMTA](https://www.sfmta.com/reports/gtfs-transit-data) in San
Francisco have been provided. However the situation is different from
that of Japan. In many countries, transportation is provided by the
government or by one company. It enables to publish the data at once if
data is provided, . In Japan, there are many service provider such as
the JR Group, private railways, bus operators, and taxi operators. It is
difficult to realize to publish the data at once due to each operator’s
management decision and internal circumstances. In addition, the fact
that the data delivered by each company is different makes this problem
even more difficult. The data is unified to some extent in GTFS format,
but there are issues for each business such as the core system that
differs for each business, the guarantee of the amount of information
considering the circumstances of each company, and the provision of more
information than GTFS. Must be absorbed.

目的 Purpose
============

TraISAREは以下のようなアプリケーションを実現するためのデータ基盤である。

-   リアルタイムな乗り換え案内を実現する(時刻表によらない乗換案内を実現する)

-   需要予測によるダイナミックプライシング

Realize a platform that can handle traffic transport information with a
unified interface.

-   Trip planner using real-time data (Not using timetable-data)

-   Dynamic pricing depend on demand forecast

機能 Function
=============

TraISAREは遍く交通輸送情報を統一したインターフェース処理できる基盤を実現するため、以下の5点の機能を実現する。
- 各社から提供されるRAWデータの保持 -
提供されたRAWデータの正規化・抽象化 -
正規化・抽象化されたデータのアグリゲーション -
アグリゲートされた情報の提供

Realize a platform that can handle traffic transport information with a
unified interface.

-   Retention of Raw data provided by each company

-   Normalization and abstraction of provided Raw data

-   Aggregation of normalized / abstracted data

-   Providing aggregated information

データフロー Data flow
======================

TraISAREは以下のフローでデータを処理する。

-   各交通事業者のデータを受信する

-   受信したデータをRaw Storeに保存する

-   保存したデータを統一データ形式に変換する

-   変換したデータをCommon Storeに保存する

-   Common Storeのデータを使用して統計処理や機械学習を実施する

TraISARE processes the data with the flow shown in blow:

-   Receive the data from each operators

-   Store the revcieved data to Raw Store

-   Convert the stored data to the unified format

-   Converted data stores in Common Store

-   Condunct stastical processing or machine learning with the data in
    common store

システム構成 System configration
================================

TraISAREは5つのコンポーネント(Receiver, Raw Store, Encoder, Common
Store, Aggregator)で構成する。

TraISARE consists of 5 components (Receiver, Raw Store, Encoder, Common
Store, Aggregator)

![System configuration](images/components.png)

Receiver
--------

Receiverは交通事業者のデータを受信するためのモジュールである。各交通事業者のデータは、次のように提供される。

-   Push受信: 事業者からデータが送信されてくる場合

-   Pull受信: 事業者からデータを取得する場合

受信方法が交通事業者毎に異なるため、TraISAREではReceiverを事業者毎に準備する。それぞれのReceiverがデータを受信し、Raw
Storeへ保存する。

In this system, the following method is assumed as a method of providing
data from the operator.

-   Push reciever: The data is trasmitted from operator

-   Pull receiver: The request is transmitted to operator to get the
    data

In order to support these receptions, TraISARE prepares a module called
Receiver for each operator. Each Receiver receives the data and stores
it in the Raw Store.

Raw Store
---------

Raw
Storeは交通事業者から提供された情報をそのままの形で保存するレイヤーである。Receiverの受信単位を1つのファイルとし、Raw
Storeに保存する。ファイルは主にXML、JSON、CSVなどの構造化ファイルとして保存することを想定するが、ファイルとして保存するのでJPEG、PDF、Protocol
Bufferなども保存できる。

In the Raw Store, it is a layer that stores information provided by
transportation operators as it is. Raw Store saves as a file by
receiving unit. Although it is assumed that it is mainly saved as a
structured file such as XML, JSON, CSV, etc., it is saved as a file, so
it can also be saved as JPEG, PDF, Protocol Buffer, etc.

Encorder
--------

Encoderは、RAW
Storeに保存された情報を読み取り、正規化、抽象化を実施してCommon
Storeに保存するモジュールである。

Encoder is a module that reads information stored in the RAW Store,
normalizes and abstracts it, and stores it in the Common Store.

正規化・抽象化 Normalization and abstraction  
Raw
Store内のデータの矛盾を排除するためデータを正規化し、TraIIRe形式に変換することでデータを抽象化する。TraIIRe形式は移動情報の中間表現であり、抽象化の手法は[別紙](../TraIIRe/index.html)に述べる。

Normalize the data stored in Raw Store to eliminate the inconsistency
and convert the normalized data to TraIIRe format to produce abstract
data. The TraIIRe format is an intermediate representation of traffic
information. Details shown in [another document](../TraIIRe/index.html).

Common Store
------------

Common StoreはEncorderで正規化、抽象化したデータを保存する。Common
StoreのデータはTraIIReデータ形式、Apache
Parquetファイルで保存する。すべての事業者のデータをTraIIRe形式に統一して保存することで、事業者に依らないデータの分析、情報提供を可能にする。

Common Store stores normalized and abstracted data by Encorder. The data
in the Common Store is stored in TraIIRe format and Apache Parquet
format. It enables to analyze data and provide information regardless of
the operator by storing the data from all operators in a unified TraIIRe
data format.

### Components and storage directory structures

Common StoreはAzure ADLS Gen2 Blob containerである。Blob
containerは以下のようにTraIIReデータ形式の基底モデルに従ってディレクトリを構成している。Encoderで生成したTraIIReデータ形式のファイルを該当する基底モデルのディレクトリに格納する。

The Common Store is the Azure ADLS Gen2 Blob container. This is
organized into directories according to the TraIIRe data format base
model as follows. Store the TraIIRe data format file generated by the
encoder in the directory of the corresponding base model.

      - commonstore
        |- edge
        |- graph
        |- node
        |- operator
        |- timetable
        |- transportation
        |- load
        |- leg
        |- trip

Aggrigator
----------

AggregatorはCommon
Storeに保存された情報をアグリゲーションする。Aggrigatorはユーザーからのリクエストに応じてCommon
Storeに保存された情報を読みとり、必要な処理を実施してユーザーに返す。Aggregatorは以下の機能を持つことを想定する。

Aggregator aggregates the information stored in the Common Store.
Aggrigator reads the information stored in the Common Store in response
to the request from the user, performs the necessary processing, and
returns it to the user. It is assumed that Aggregator has a function
below:

-   Query: Common Storeに対するクエリー処理

-   API: Application Programing Interface, Common
    Storeに対するInterfaceラッパー

-   SA: Statical Analytics, 統計分析

-   ML: Machine Learning , 機械学習(AI)

### Query function

クエリ機能はCommon
Storeに保存したTraIIRe形式データに対してクエリを実行する機能である。本機能は小規模なデータに対して実行することを想定する。本機能によりレポート、ダッシュボードの作成に必要なデータを生成する。

The query function executes queries against TraIIRe format data stored
in the Common Store. It is assumed that this function will be executed
for small-scale data. This function generates the data necessary for
creating reports and dashboards.

### API function

Common
Storeに対するI/Fラッパーは、TraISAREのAPIとして外部と連携するための機能である。現在想定しているI/Fは以下である。

\+ The I/F wrapper for the Common Store is a function for linking with
the outside as a TraISARE API. The currently assumed I/F is as follows.

-   NGSI-LD

-   GTFS, GTFS-RT

-   odpt

    上記に挙げた仕様に対するラッパーという立ち位置は、実際の処理としてCommon
    Storeに保持されたデータのフォーマット変換とI/Fの提供という二つの機能がそれぞれの仕様に対して必要となる。そのため、それぞれの仕様に対してそれぞれのAggrigator実装が必要となる。（運用時もそれぞれ別プロセスとして動作させる）

    The position of the wrapper for the specifications listed above
    requires two functions for each specification: format conversion of
    data stored in the Common Store and provision of I / F as actual
    processing. Therefore, each Aggrigator implementation is required
    for each specification. (Also run as separate processes during
    operation)

### SA function

Common
Storeに保存されたデータに対して統計分析を行うための機能。運行中の台数、ある区間における乗車率の算出など、レポート・ダッシュボードの作成に必要となる数値の算出を行う。

A function for statistical analysis of data stored in the Common Store.
Calculate the numbers required to create reports and dashboards, such as
calculating the number of cars in operation and the occupancy rate in a
certain section.

### ML function

Common
Storeに保持されたデータを基に機械学習行い、未来の状態を予測する。例えば、列車在線情報の遅れ情報より、未来の遅れを予測する。

Perform machine learning based on data stored in the Common Store. For
example, it predicts future delays from delay information in train line
information

= TraISARE: Transport Information Store with Aggregator, Receiver and
Encoder MaaS Tech Japan K.K.

:toc: left :toclevel: 5 :toc-title: 目次 :sectnums: :imagesdir: images
== 概要 Abstract
交通システムの高度化により、移動手段の多様化が進んでいるしかしながら各交通システムは事業者毎に異なったシステムが運用されており、シームレスな移動を実現するためのデータ処理に問題を抱えている。これらを解決するTraISARE:Transport
Information Store with Aggregator, Receiver and
Encoderを提案し、実装する。 With the advancement of transportation
systems, diversification of transportation means is progressing.
However, each transportation system has a different system operation for
each business operator and has a problem with data processing for
realizing seamless movement. To solve these problems, we propose and
implement TraISARE: Transport Information Store with Aggregator,
Receiver and Encoder. == 背景 Background
公共交通情報の統一フォーマットのデファクトスタンダードと言えるのが、link:https://developers.google.com/transit/?hl=ja\[GTFS\]である。これは交通事業者が駅、バス停、時刻表、ルートなどの情報を記述するために規定されたデータフォーマットである。元々Google
Mapsで公共交通情報を処理するために規定されたフォーマットであるが、現在は一般にも公開され、事業者によってはオープンデータとして配布しているケースもある。このフォーマットの最大のメリットは、作成したデータを登録することでGoogle
Maps上へ情報を表示・検索できるようになることである。中小の事業者では自社でスマートフォンサービスをメンテナンスすることが難しい場合があり、データを用意するだけで世界最大の地図基盤に情報提供をできるメリットは大きい。しかし、欧米発祥ということもあり日本の交通事情に即していないケースも見受けられるため、最近では国土交通省よりlink:http://www.mlit.go.jp/sogoseisaku/transport/sosei\_transport\_tk\_000067.html\[標準的なバス情報フォーマット\]としてGTFSを拡張した仕様を公開している。鉄道に関しては、まだ日本の事情に即したフォーマットは提供されていない。
日本の公共交通情報の提供としては、公共交通オープンデータ協議会(ODPT)が挙げられる。現在59事業者が参画しており、商用利用可能な形で10事業者がデータの公開を行なっている。ODPTでは鉄道、バス、航空機の情報を提供している。
+
また海外では公共交通情報をオープンデータとして提供するトレンドが2014年頃より広がり、ロンドンにおけるlink:https://tfl.gov.uk/\[TfL\]、フィンランドにおけるlink:https://www.digitraffic.fi/en/\[DigiTraffic\]、サンフランシスコ市におけるlink:https://www.sfmta.com/reports/gtfs-transit-data\[SFMTA\]など数多くの公共交通情報が提供されるようになってきている。これら諸外国では、交通機関は官営あるいは一社独占で提供する場合が多く、データの提供を開始する場合は、すべての交通機関のデータを一括して提供することが可能である。
+
日本ではJRグループとその他私鉄、更にバス事業者、タクシー事業者といった数多くのステークホルダーが存在し、それぞれの経営判断や社内事情などもあって、データを一括して提供するといった事業は、1事業者だけでは実現困難と言える。加えて各社から配信されるデータが異なるという事情が、この問題を更に困難にしている。データはGTFS形式である程度統一されているが、事業者毎に異なる基幹システム、各社の事情を考慮した情報量の担保、加えてGTFS以上の情報量を持たせることなどの事業者毎の課題を吸収しなければならない。
link:https://developers.google.com/transit/?hl=ja\[GTFS\] is the de
facto standard for the unified format of public transportation
information. This is a data format defined for transportation companies
to describe information such as stations, bus stops, timetables, and
routes. Originally it was a format specified by Google Maps to process
such public transportation information. Now it is open to the public,
and some operators distribute it as open data. The biggest advantage of
this format is to enable the Google maps to display and search it by
registering the data. It is the benefit for some smaller operators, who
are difficult to maintain their own smartphone services, to provide
their information to the larget map platform in the world simply by
preparing data. However, sometimes it does not match the traffic
conditions in Japan because it is a western-oriented platform, and the
extended GTFS as a standard bus information format start to release by
the Ministry of Land, Infrastructure, Transport and Tourism. Regarding
to railways, the format that suits the circumstances of Japan has not
been provided. The association for open data of public transportation
(ODPT) is one of the provider of public transport information in Japan.
Currently, 59 companies are participating, and 10 companies are
publishing data that can be used for commercial purposes. ODPT provides
rail, bus and aircraft information. + It is gradually increasing in
overseas to provide public transportation information as open data since
around 2014. Many public transportation information such as
link:https://tfl.gov.uk/\[TfL\] in London,
link:https://www.digitraffic.fi/en/\[DigiTraffic\] in Finland, and
link:https://www.sfmta.com/reports/gtfs-transit-data\[SFMTA\] in San
Francisco have been provided. However the situation is different from
that of Japan. In many countries, transportation is provided by the
government or by one company. It enables to publish the data at once if
data is provided, . In Japan, there are many service provider such as
the JR Group, private railways, bus operators, and taxi operators. It is
difficult to realize to publish the data at once due to each operator's
management decision and internal circumstances. In addition, the fact
that the data delivered by each company is different makes this problem
even more difficult. The data is unified to some extent in GTFS format,
but there are issues for each business such as the core system that
differs for each business, the guarantee of the amount of information
considering the circumstances of each company, and the provision of more
information than GTFS. Must be absorbed. == 目的 Purpose
TraISAREは以下のようなアプリケーションを実現するためのデータ基盤である。
\*
リアルタイムな乗り換え案内を実現する(時刻表によらない乗換案内を実現する)
\* 需要予測によるダイナミックプライシング Realize a platform that can
handle traffic transport information with a unified interface. \* Trip
planner using real-time data (Not using timetable-data) \* Dynamic
pricing depend on demand forecast == 機能 Function
TraISAREは遍く交通輸送情報を統一したインターフェース処理できる基盤を実現するため、以下の5点の機能を実現する。
- 各社から提供されるRAWデータの保持 -
提供されたRAWデータの正規化・抽象化 -
正規化・抽象化されたデータのアグリゲーション -
アグリゲートされた情報の提供 Realize a platform that can handle traffic
transport information with a unified interface. - Retention of Raw data
provided by each company - Normalization and abstraction of provided Raw
data - Aggregation of normalized / abstracted data - Providing
aggregated information == データフロー Data flow
TraISAREは以下のフローでデータを処理する。 -
各交通事業者のデータを受信する - 受信したデータをRaw Storeに保存する -
保存したデータを統一データ形式に変換する - 変換したデータをCommon
Storeに保存する - Common
Storeのデータを使用して統計処理や機械学習を実施する TraISARE processes
the data with the flow shown in blow: - Receive the data from each
operators - Store the revcieved data to Raw Store - Convert the stored
data to the unified format - Converted data stores in Common Store -
Condunct stastical processing or machine learning with the data in
common store == システム構成 System configration
TraISAREは5つのコンポーネント(Receiver, Raw Store, Encoder, Common
Store, Aggregator)で構成する。 TraISARE consists of 5 components
(Receiver, Raw Store, Encoder, Common Store, Aggregator)
image::components.png\[System configuration\] === Receiver
Receiverは交通事業者のデータを受信するためのモジュールである。各交通事業者のデータは、次のように提供される。
- Push受信: 事業者からデータが送信されてくる場合 - Pull受信:
事業者からデータを取得する場合
受信方法が交通事業者毎に異なるため、TraISAREではReceiverを事業者毎に準備する。それぞれのReceiverがデータを受信し、Raw
Storeへ保存する。 In this system, the following method is assumed as a
method of providing data from the operator. - Push reciever: The data is
trasmitted from operator - Pull receiver: The request is transmitted to
operator to get the data In order to support these receptions, TraISARE
prepares a module called Receiver for each operator. Each Receiver
receives the data and stores it in the Raw Store. === Raw Store Raw
Storeは交通事業者から提供された情報をそのままの形で保存するレイヤーである。Receiverの受信単位を1つのファイルとし、Raw
Storeに保存する。ファイルは主にXML、JSON、CSVなどの構造化ファイルとして保存することを想定するが、ファイルとして保存するのでJPEG、PDF、Protocol
Bufferなども保存できる。 In the Raw Store, it is a layer that stores
information provided by transportation operators as it is. Raw Store
saves as a file by receiving unit. Although it is assumed that it is
mainly saved as a structured file such as XML, JSON, CSV, etc., it is
saved as a file, so it can also be saved as JPEG, PDF, Protocol Buffer,
etc. === Encorder Encoderは、RAW
Storeに保存された情報を読み取り、正規化、抽象化を実施してCommon
Storeに保存するモジュールである。 Encoder is a module that reads
information stored in the RAW Store, normalizes and abstracts it, and
stores it in the Common Store. 正規化・抽象化 Normalization and
abstraction:: Raw
Store内のデータの矛盾を排除するためデータを正規化し、TraIIRe形式に変換することでデータを抽象化する。TraIIRe形式は移動情報の中間表現であり、抽象化の手法はlink:../TraIIRe/index.html\[別紙\]に述べる。
+ Normalize the data stored in Raw Store to eliminate the inconsistency
and convert the normalized data to TraIIRe format to produce abstract
data. The TraIIRe format is an intermediate representation of traffic
information. Details shown in link:../TraIIRe/index.html\[another
document\]. === Common Store Common
StoreはEncorderで正規化、抽象化したデータを保存する。Common
StoreのデータはTraIIReデータ形式、Apache
Parquetファイルで保存する。すべての事業者のデータをTraIIRe形式に統一して保存することで、事業者に依らないデータの分析、情報提供を可能にする。
Common Store stores normalized and abstracted data by Encorder. The data
in the Common Store is stored in TraIIRe format and Apache Parquet
format. It enables to analyze data and provide information regardless of
the operator by storing the data from all operators in a unified TraIIRe
data format. ==== Components and storage directory structures Common
StoreはAzure ADLS Gen2 Blob containerである。Blob
containerは以下のようにTraIIReデータ形式の基底モデルに従ってディレクトリを構成している。Encoderで生成したTraIIReデータ形式のファイルを該当する基底モデルのディレクトリに格納する。
The Common Store is the Azure ADLS Gen2 Blob container. This is
organized into directories according to the TraIIRe data format base
model as follows. Store the TraIIRe data format file generated by the
encoder in the directory of the corresponding base model. ---- -
commonstore |- edge |- graph |- node |- operator |- timetable |-
transportation |- load |- leg |- trip ---- === Aggrigator
AggregatorはCommon
Storeに保存された情報をアグリゲーションする。Aggrigatorはユーザーからのリクエストに応じてCommon
Storeに保存された情報を読みとり、必要な処理を実施してユーザーに返す。Aggregatorは以下の機能を持つことを想定する。
Aggregator aggregates the information stored in the Common Store.
Aggrigator reads the information stored in the Common Store in response
to the request from the user, performs the necessary processing, and
returns it to the user. It is assumed that Aggregator has a function
below: \* Query: Common Storeに対するクエリー処理 \* API: Application
Programing Interface, Common Storeに対するInterfaceラッパー \* SA:
Statical Analytics, 統計分析 \* ML: Machine Learning , 機械学習(AI) ====
Query function クエリ機能はCommon
Storeに保存したTraIIRe形式データに対してクエリを実行する機能である。本機能は小規模なデータに対して実行することを想定する。本機能によりレポート、ダッシュボードの作成に必要なデータを生成する。
The query function executes queries against TraIIRe format data stored
in the Common Store. It is assumed that this function will be executed
for small-scale data. This function generates the data necessary for
creating reports and dashboards. ==== API function Common
Storeに対するI/Fラッパーは、TraISAREのAPIとして外部と連携するための機能である。現在想定しているI/Fは以下である。
+ The I/F wrapper for the Common Store is a function for linking with
the outside as a TraISARE API. The currently assumed I/F is as follows.
- NGSI-LD - GTFS, GTFS-RT - odpt +
上記に挙げた仕様に対するラッパーという立ち位置は、実際の処理としてCommon
Storeに保持されたデータのフォーマット変換とI/Fの提供という二つの機能がそれぞれの仕様に対して必要となる。そのため、それぞれの仕様に対してそれぞれのAggrigator実装が必要となる。（運用時もそれぞれ別プロセスとして動作させる）
+ The position of the wrapper for the specifications listed above
requires two functions for each specification: format conversion of data
stored in the Common Store and provision of I / F as actual processing.
Therefore, each Aggrigator implementation is required for each
specification. (Also run as separate processes during operation) ==== SA
function Common
Storeに保存されたデータに対して統計分析を行うための機能。運行中の台数、ある区間における乗車率の算出など、レポート・ダッシュボードの作成に必要となる数値の算出を行う。
A function for statistical analysis of data stored in the Common Store.
Calculate the numbers required to create reports and dashboards, such as
calculating the number of cars in operation and the occupancy rate in a
certain section. ==== ML function Common
Storeに保持されたデータを基に機械学習行い、未来の状態を予測する。例えば、列車在線情報の遅れ情報より、未来の遅れを予測する。
Perform machine learning based on data stored in the Common Store. For
example, it predicts future delays from delay information in train line
information
