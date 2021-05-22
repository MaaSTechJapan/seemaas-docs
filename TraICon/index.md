概要 Absract
============

TraICon(Transport Information
Console)はTraISAREのデータを可視化・アクチュエーションするコンソールである。ユーザはTraISAREのデータをTraIConを介して取得するとともに、TraICon上でデータを分析、可視化することができる。

TraICon (Transport Information Console) is a console for visualization
and actuation of TraISARE data. Users can obtain TraISARE data through
TraICon, and analyze and visualize the data on TraICon.

背景 Background
===============

交通分野の投資やオペレーションに関する意思決定は、実態の移動データに基づいて行われているとは言い難い。実際、日本国内の自治体における交通網計画は、数年に一度のセンサスやパーソントリップ調査に基づいて行われており、それらの根拠データの蓋然性が怪しい。また、交通政策立案の根拠として、結果ありきでシミュレーションモデルが組まれている事例や、MaaSや新しいモビリティサービスの検討において、データが用いられず、担当者の裁量によって企画が実施されている事例もある。このようなデータに基づかない交通政策により、交通ダイヤ改善や商業施設建設、MaaSによるシームレス化や行動変容など施策に対して、その効果を算出するためのモデル化が進んでいない。
結果、総合的な交通体系の中での目指すビジョンに対してどのアクションが有益かを導くシミュレーションができず、無人運転車両やエアモビリティ導入、公共交通無償化などこれまで事例のないようなダイナミックな施策に対して社会実装効果が可視化されないので、技術革新の根拠付けが出来ず諸外国にリードされ続けてしまうといった状態に陥っている。諸外国ではデータ活用が進展し、MaaSアプリで取得された移動データの分析を行い、交通のプランニングや運行オペレーションにフィードバックをかける事例が出現している。ベルリンでは、MaaSアプリのオペレータTrafiが、アプリから取得されたデータを用いて、交通オペレーションの企画を行うソフトウェアを開発し、ITS世界会議2019でコンセプト発表している。ドバイでは、Siemens製MaaSアプリS’hailから取得されたデータをもとに、地下鉄と路面電車のスケジュールを調整し、バス路線を新たに設置するといった事例がある。

これらのトレンドを受け、日本国内においても、政策的後押しを背景に、スマートシティやMaaSの考え方が自治体や交通事業者に普及しつつあり、移動関連のデータやDX関連の投資が進みつつある。実際に、2020年度の経済産業省のスマートモビリティチャレンジにおいては、「モビリティからデータを取得・可視化し、より効率的な移動を実現するなど都市政策へのフィードバックを行うこと」が公募の要件の1つとして入った。国土交通省では、「都市の抱える諸課題に対して、ICT等の新技術を活用しつつ、
マネジメントが行われ、全体最適化が図られる持続可能な都市または地区」とスマートシティを定義し、プロジェクトを公募した。これらの現状を踏まえると、今後交通事業者や自治体を中心に、アプリや交通サービスで取得された実際のユーザーの移動データに基づいて、交通の投資やオペレーションを再考する事例が出現していくと想定される。

現状、交通事業者や自治体が地域の交通データを可視化・分析する際、実際の移動データを使って細かに分析できるソフトウェアがない。交通政策ではそもそも実際の移動データが使われて来なかったため、フォーマットが多様な実際の移動Rawデータの受け入れができない。また従来自治体が見ているデータは、手集計で1日単位（地方バス等では1ヶ月単位など）で丸め込まれているもので、Rawデータに基づいたメッシュ単位（時間単位／列車車両単位／出発地目的地単位など）の細かな推移の把握」（例：金曜日の午後xx時はバスのxxx号線のxxからxxまでの移動が多い、など）ができない。このような問題に対して、TraISAREのデータを使用した地域の交通データを可視化、分析できるダッシュボードと分析機能をもったアプリケーションを開発する。

Decisions on investment and operations in the transportation sector are
not based on actual traffic data. In fact, transportation network
planning in Japanese municipalities is based on multi-year censuses and
person-trip studies, and the probability of their data is questionable.
There are also some cases where simulation models for transportation
policy planning are built based on the desired results, or where
planning is carried out at the discretion of the person in charge
without using data when considering MaaS or new mobility services. These
non-data-driven transportation policies have resulted in a lack of
modeling for calculating the effects of measures such as traffic
schedule improvement, commercial construction, and seamlessness and
behavioral change through MaaS. As a result, it is not possible to
simulate which actions are beneficial for the desired vision in a
comprehensive transportation system and to visualize the social
implementation effects of measures such as the introduction of
driverless vehicles and air mobility or free public transportation,
which have never been seen before. This is the reason why technical
innovation is rated lower and continue to be led by other countries. In
other countries, the use of data is advancing, and there are examples of
analyzing traffic data captured by MaaS apps to provide feedback for
traffic planning and operations. In Berlin, MaaS app operator Trafi has
developed software that uses data captured from the app to plan traffic
operations, and is presenting the concept at the ITS World Congress
2019. In Dubai, data obtained from the Siemens MaaS app S’hail' is used
to coordinate metro and streetcar and install new bus lines, for
example.

Against the backdrop of these trends, the idea of smart cities and MaaS
is spreading among local governments and transportation operators in
Japan, and investment in mobility-related data and DX is increasing. In
fact, in the Smart Mobility Challenge of the Ministry of Economy, Trade
and Industry in FY2020, one of the requirements of the public call for
applications is to "acquire and visualize data from mobility and provide
feedback to urban policies, such as by realizing more efficient
mobility". The Ministry of Land, Infrastructure, Transport and Tourism
(MLIT) defines a smart city as "a sustainable city or district that
utilizes ICT and other new technologies to manage and optimize the
various issues facing the city," and had solicited applications for
projects. Given the current situation, it can be expected to see cases
of rethinking transportation investments and operations based on actual
data of traffic acquired by apps and transportation services, mainly
from transportation operators and municipalities.

Currently, there is no software that allows transportation companies and
municipalities to use actual traffic data for detailed analysis when
visualizing and analyzing regional traffic data. Because actual traffic
data has never been used in transportation policy, it is impossible to
accept actual raw traffic data in a variety of formats. In addition,
conventional data viewed by local governments are rounded down to the
nearest day (e.g., a month for local buses, etc.) in manual tabulations,
and it is impossible to "grasp detailed trends in a mesh unit (e.g.,
hourly unit/train car unit/departure destination unit) based on raw
data" (e.g., Friday afternoon at xx:00 on bus line xx (e.g., a lot of
travel from xx to xx, etc.). To solve these problems, the application
with dashboards and analytics is to be developed, which can visualize
and analyze regional traffic data using TraISARE data.

想定するユーザ Whom will use this application?
==============================================

交通に関するデータ分析を行いたい交通事業者、自治体、ほかデベロッパー等の街づくり関連企業

Transport operators, municipalities, and other urban development
companies such as developers who want to analyze data on transportation

機能要求 Functional requirement
===============================

実ユーザの移動データの分析実際機能が備え、細かなメッシュ単位のデータの取扱いができ、企画検討に必要なデータを詳細に把握する可視化・分析機能が備わったアプリケーションであること。

-   TraISAREのデータを取り扱うことができること

-   各データメッシュ単位の細やかな取り扱いができること

-   地図、路線図、グラフ、数字での可視化・傾向分析表示が可能であること

-   画面のカスタマイズ対応が可能であること

-   PDFでの（定例/単発での）レポート出力ができること

-   ほぼリアルタイムで情報表示ができること

-   移動以外のデータも紐付けて分析ができること

-   過去実績をもとに未来の利用状況に関して予測の表示ができること

-   一定の仮定を置いたシミュレーションができること

The application should be equipped with the actual function of analyzing
real user traffic data, handling data in a fine mesh unit, and
visualization and analysis functions to grasp the data required for
planning studies in detail.

-   Enable to handle TraISARE data

-   The ability to handle each data mesh unit of detail.

-   Visualization and trend analysis display in maps, route maps, graphs
    and numbers.

-   Screen customization is available

-   Ability to output (regular/one-off) reports in PDF

-   Enable to display information in near real time

-   The ability to analyze data with non-movement data

-   The ability to display predictions about future usage based on past
    performance

-   The ability to simulate with certain assumptions.

非機能要求 Non-functional requirement
=====================================

-   マネタイズを考慮してパッケージ化されていること

-   サポートを考慮し、動作環境を統一すること

-   UIはネイティブ化されてること

-   Windows, MacOS対応に対応すること

-   鉄道現場ではiPadがデファクト化しているため、可能であればiOS,
    Androidに対応すること

-   Considering monetization, the system should be packaged

-   Considering product support, the system operation environment shold
    be unified.

-   The UI should be a native application.

-   Windows and MacOS should be supported.

-   It is ideal that iOS and Android should be supported because the
    iPad is the de facto standard device in railway work field.

構成 Components
===============

Fetcher
-------

FetcherはTraISAREに対してリクエストを生成するクエリージェネレーターである。

The Fetcher is a query generator that generates requests for TraISARE.

Visualizer
----------

VisualizerはFetcherで取得したデータを可視化する。

The Visualizer visualizes the data that the Fetcher aquires.

Actuator
--------

Actuatorはエンティティに対してアクチュエーションを実施する。

The Actuator conducts actuation for entities.

= TraICon: Transport Information Console MaaS Tech Japan K.K.

:doctype: book :toc: left :numbered: :toclevels: 7 :source-highlighter:
rouge :rouge-linenums-mode: inline :imagesdir: images == 概要 Absract
TraICon(Transport Information
Console)はTraISAREのデータを可視化・アクチュエーションするコンソールである。ユーザはTraISAREのデータをTraIConを介して取得するとともに、TraICon上でデータを分析、可視化することができる。
TraICon (Transport Information Console) is a console for visualization
and actuation of TraISARE data. Users can obtain TraISARE data through
TraICon, and analyze and visualize the data on TraICon. == 背景
Background
交通分野の投資やオペレーションに関する意思決定は、実態の移動データに基づいて行われているとは言い難い。実際、日本国内の自治体における交通網計画は、数年に一度のセンサスやパーソントリップ調査に基づいて行われており、それらの根拠データの蓋然性が怪しい。また、交通政策立案の根拠として、結果ありきでシミュレーションモデルが組まれている事例や、MaaSや新しいモビリティサービスの検討において、データが用いられず、担当者の裁量によって企画が実施されている事例もある。このようなデータに基づかない交通政策により、交通ダイヤ改善や商業施設建設、MaaSによるシームレス化や行動変容など施策に対して、その効果を算出するためのモデル化が進んでいない。
結果、総合的な交通体系の中での目指すビジョンに対してどのアクションが有益かを導くシミュレーションができず、無人運転車両やエアモビリティ導入、公共交通無償化などこれまで事例のないようなダイナミックな施策に対して社会実装効果が可視化されないので、技術革新の根拠付けが出来ず諸外国にリードされ続けてしまうといった状態に陥っている。諸外国ではデータ活用が進展し、MaaSアプリで取得された移動データの分析を行い、交通のプランニングや運行オペレーションにフィードバックをかける事例が出現している。ベルリンでは、MaaSアプリのオペレータTrafiが、アプリから取得されたデータを用いて、交通オペレーションの企画を行うソフトウェアを開発し、ITS世界会議2019でコンセプト発表している。ドバイでは、Siemens製MaaSアプリS'hailから取得されたデータをもとに、地下鉄と路面電車のスケジュールを調整し、バス路線を新たに設置するといった事例がある。
これらのトレンドを受け、日本国内においても、政策的後押しを背景に、スマートシティやMaaSの考え方が自治体や交通事業者に普及しつつあり、移動関連のデータやDX関連の投資が進みつつある。実際に、2020年度の経済産業省のスマートモビリティチャレンジにおいては、「モビリティからデータを取得・可視化し、より効率的な移動を実現するなど都市政策へのフィードバックを行うこと」が公募の要件の1つとして入った。国土交通省では、「都市の抱える諸課題に対して、ICT等の新技術を活用しつつ、
マネジメントが行われ、全体最適化が図られる持続可能な都市または地区」とスマートシティを定義し、プロジェクトを公募した。これらの現状を踏まえると、今後交通事業者や自治体を中心に、アプリや交通サービスで取得された実際のユーザーの移動データに基づいて、交通の投資やオペレーションを再考する事例が出現していくと想定される。
現状、交通事業者や自治体が地域の交通データを可視化・分析する際、実際の移動データを使って細かに分析できるソフトウェアがない。交通政策ではそもそも実際の移動データが使われて来なかったため、フォーマットが多様な実際の移動Rawデータの受け入れができない。また従来自治体が見ているデータは、手集計で1日単位（地方バス等では1ヶ月単位など）で丸め込まれているもので、Rawデータに基づいたメッシュ単位（時間単位／列車車両単位／出発地目的地単位など）の細かな推移の把握」（例：金曜日の午後xx時はバスのxxx号線のxxからxxまでの移動が多い、など）ができない。このような問題に対して、TraISAREのデータを使用した地域の交通データを可視化、分析できるダッシュボードと分析機能をもったアプリケーションを開発する。
Decisions on investment and operations in the transportation sector are
not based on actual traffic data. In fact, transportation network
planning in Japanese municipalities is based on multi-year censuses and
person-trip studies, and the probability of their data is questionable.
There are also some cases where simulation models for transportation
policy planning are built based on the desired results, or where
planning is carried out at the discretion of the person in charge
without using data when considering MaaS or new mobility services. These
non-data-driven transportation policies have resulted in a lack of
modeling for calculating the effects of measures such as traffic
schedule improvement, commercial construction, and seamlessness and
behavioral change through MaaS. As a result, it is not possible to
simulate which actions are beneficial for the desired vision in a
comprehensive transportation system and to visualize the social
implementation effects of measures such as the introduction of
driverless vehicles and air mobility or free public transportation,
which have never been seen before. This is the reason why technical
innovation is rated lower and continue to be led by other countries. In
other countries, the use of data is advancing, and there are examples of
analyzing traffic data captured by MaaS apps to provide feedback for
traffic planning and operations. In Berlin, MaaS app operator Trafi has
developed software that uses data captured from the app to plan traffic
operations, and is presenting the concept at the ITS World Congress
2019. In Dubai, data obtained from the Siemens MaaS app S'hail' is used
to coordinate metro and streetcar and install new bus lines, for
example. Against the backdrop of these trends, the idea of smart cities
and MaaS is spreading among local governments and transportation
operators in Japan, and investment in mobility-related data and DX is
increasing. In fact, in the Smart Mobility Challenge of the Ministry of
Economy, Trade and Industry in FY2020, one of the requirements of the
public call for applications is to "acquire and visualize data from
mobility and provide feedback to urban policies, such as by realizing
more efficient mobility". The Ministry of Land, Infrastructure,
Transport and Tourism (MLIT) defines a smart city as "a sustainable city
or district that utilizes ICT and other new technologies to manage and
optimize the various issues facing the city," and had solicited
applications for projects. Given the current situation, it can be
expected to see cases of rethinking transportation investments and
operations based on actual data of traffic acquired by apps and
transportation services, mainly from transportation operators and
municipalities. Currently, there is no software that allows
transportation companies and municipalities to use actual traffic data
for detailed analysis when visualizing and analyzing regional traffic
data. Because actual traffic data has never been used in transportation
policy, it is impossible to accept actual raw traffic data in a variety
of formats. In addition, conventional data viewed by local governments
are rounded down to the nearest day (e.g., a month for local buses,
etc.) in manual tabulations, and it is impossible to "grasp detailed
trends in a mesh unit (e.g., hourly unit/train car unit/departure
destination unit) based on raw data" (e.g., Friday afternoon at xx:00 on
bus line xx (e.g., a lot of travel from xx to xx, etc.). To solve these
problems, the application with dashboards and analytics is to be
developed, which can visualize and analyze regional traffic data using
TraISARE data. == 想定するユーザ Whom will use this application?
交通に関するデータ分析を行いたい交通事業者、自治体、ほかデベロッパー等の街づくり関連企業
Transport operators, municipalities, and other urban development
companies such as developers who want to analyze data on transportation
== 機能要求 Functional requirement
実ユーザの移動データの分析実際機能が備え、細かなメッシュ単位のデータの取扱いができ、企画検討に必要なデータを詳細に把握する可視化・分析機能が備わったアプリケーションであること。
\* TraISAREのデータを取り扱うことができること \*
各データメッシュ単位の細やかな取り扱いができること \*
地図、路線図、グラフ、数字での可視化・傾向分析表示が可能であること \*
画面のカスタマイズ対応が可能であること \*
PDFでの（定例/単発での）レポート出力ができること \*
ほぼリアルタイムで情報表示ができること \*
移動以外のデータも紐付けて分析ができること \*
過去実績をもとに未来の利用状況に関して予測の表示ができること \*
一定の仮定を置いたシミュレーションができること The application should be
equipped with the actual function of analyzing real user traffic data,
handling data in a fine mesh unit, and visualization and analysis
functions to grasp the data required for planning studies in detail. \*
Enable to handle TraISARE data \* The ability to handle each data mesh
unit of detail. \* Visualization and trend analysis display in maps,
route maps, graphs and numbers. \* Screen customization is available \*
Ability to output (regular/one-off) reports in PDF \* Enable to display
information in near real time \* The ability to analyze data with
non-movement data \* The ability to display predictions about future
usage based on past performance \* The ability to simulate with certain
assumptions. == 非機能要求 Non-functional requirement \*
マネタイズを考慮してパッケージ化されていること \*
サポートを考慮し、動作環境を統一すること \* UIはネイティブ化されてること
\* Windows, MacOS対応に対応すること \*
鉄道現場ではiPadがデファクト化しているため、可能であればiOS,
Androidに対応すること \* Considering monetization, the system should be
packaged \* Considering product support, the system operation
environment shold be unified. \* The UI should be a native application.
\* Windows and MacOS should be supported. \* It is ideal that iOS and
Android should be supported because the iPad is the de facto standard
device in railway work field. == 構成 Components === Fetcher
FetcherはTraISAREに対してリクエストを生成するクエリージェネレーターである。
The Fetcher is a query generator that generates requests for TraISARE.
//
ビジュアルで確認しながらリクエストを生成できること。RPCでVisualizerに取得したデータを流し込むことで実現する。
=== Visualizer VisualizerはFetcherで取得したデータを可視化する。 The
Visualizer visualizes the data that the Fetcher aquires. //
kepler.glを使用して可視化する。 === Actuator
Actuatorはエンティティに対してアクチュエーションを実施する。 The
Actuator conducts actuation for entities. // == 詳細仕様 // ===
Visualizer //
Visualizerの画面仕様について述べる。下記にVisualizerのモックアップを示す。
// https://xd.adobe.com/view/a43da670-c3e5-4460-a79d-ac9c3c07ba34-f16e/
// |=== // | 地図 | |
地図上にバス路線/バス停、鉄道路線/鉄道駅が描画されていること // |
地点選択 | マウスオーバー |
地図上でバス路線やバス停にマウスオーバーするとバス路線/バス停がハイライト（強調）表示される
// | | クリック | // \* バス停選択時 // \*
当該バス停を含む路線を固定ハイライト（強調）される // \*\*\*\*
左側カラム（グラフ）で下記で指定された情報を表示する // \*\*\*
バス路線選択時 // \*\*\*\*
当該バス停を含む路線を固定ハイライト（強調）される（バス停選択時に同じ）
// \*\*\*\* 左側カラム（グラフ）で下記で指定された情報を表示する // |
上側バー | | サービス名の記載がある // \*\* Fetcherボタンがある // \*\*
別のボタン（押すとポップアップ）で注意事項とか免責事項とかデータ範囲とか記載できる
// \*\*\* xxのデータを使っているという表示が必要になるため // -
\*\*出力ボタン\*\* // - 業務利用なのでTwitter/Facebook投稿ボタンはなし
// - 画面のスクリーンショット（JPEG,PDF）出力ボタン // -
画面表示に使っている（＝絞り込み条件に沿った）データのCSVダウンロード機能
// \* 右側カラム（Fetcher） // - カラム自体の表示/非表示 // -
Fetcherボタンを押すと出てくる、もう一度押すと消える // -
地図を選択すると消える // - 地点選択 // - バス路線を選べる // -
検索窓で入力する // - バス停を選べる // - 検索窓で入力する // -
便が選べる // - バスの便(何時何駅発の便）を1便ずつ選べる // -
時間が選べる // -
1便単位ではなく、期間（30分〜最大1ヶ月）の期間で集計データ範囲を選べる
// \* 左側カラム（グラフ） - バス停選択時 // \#\#\# 1つめのボックス // -
位置づけ： // - 概要説明（路線概要） // - 表示情報の種類 // -
テキスト表示+アルファ // - 表示内容 // 1. 選択した路線名 - バス停名 //
2. 当該路線の（前後の)バス停の一覧 // 3. 表示している日時範囲 // \#\#\#
2つめのボックス // - 位置づけ： // - 選んだバス停に関する数値情報 // -
表示グラフ // 1. 選択中の期間の利用者数合計 // -
選択中の期間の選択中のバス停の合計利用者数 // - 数値のみ表示 // 2.
選択中の期間の利用者数推移 - 1日単位（グラフ） // -
選択中の期間の選択中のバス停の1時間あたり平均利用者数の推移（1ｈ単位☓24）
// - 棒グラフ(折れ線グラフ)で表示される // 3. 選択中の期間の利用者数推移
- 1週間単位（グラフ） // -
選択中の期間の選択中のバス停の1週間あたり平均利用者数の推移（1日単位☓7）
// - 棒グラフ(折れ線グラフ)で表示される // -
↑この1-3について、BIツールのように、下記のように集計対象や表示方法をカスタマイズする機能を持たせたい
// - 集計対象とする路線 - バス停の選択 // - 集計対象とする日時期間の選択
// - 年月日選択（1月1日〜3月31日、など） // -
曜日選択（全曜日、土日のみ、など） // -
時間選択（終日、午前9:00-12:00のみ、20:00-21:00のみ、など） // -
表示方法の選択 // - 合計数値 // - 折れ線グラフ/棒グラフ // \#\#\#
3つめのボックス // - 位置づけ： // -
選んだバス停を含む路線に関する数値情報 // - 表示グラフ // 1.
選択中の路線の期間の利用者数合計 // -
選択中の期間の\*\*選択中のバス停を含む路線全体\*\*の合計利用者数 // -
数値のみ表示 // 2. 選択中の期間の利用者数推移 - 1日単位（グラフ） // -
選択中の期間の\*\*選択中のバス停を含む路線全体\*\*の1時間あたり平均利用者数の推移（1ｈ単位☓24）
// - 棒グラフ(折れ線グラフ)で表示される // 3. 選択中の期間の利用者数推移
- 1週間単位（グラフ） // -
選択中の期間の\*\*選択中のバス停を含む路線全体\*\*の1週間あたり平均利用者数の推移（1日単位☓7）
// - 棒グラフ(折れ線グラフ)で表示される // -
カスタマイズについては上に同じ // \#\#\# 4つめのボックス // -
思いついたら入れるが、OD集計表とか、乗り換えアクセス分析（接続に何分掛かるか）とかがありえるのではないか
// \#\# デザイン系（NEDOに同じ） // \#\# 起動時 // -
初めて開くと、例として特定路線の情報が表示される // == Implementation
plan // 基本的に以下のコンポーネントを使用することを想定 // \*
JavaScript // \*\* deck.gl // \*\* kepler.gl // \* Python // \*\* pandas
// \*\* matplotlib // == Jupyter // \*Pros.\* // \*
deck.gl、kepler.gl共にJupyter上で動作することを確認 // \*
kepler.glに対してdataframeをベタ流しできるのが大変よろしい // \*Cons.\*
// \*
kepler.glのバインディングが中途半端で動かないコンポーネントがある（e.g.
TripLayer） // \*
静的な画面（操作を伴わない画面）の実装はコードベースで簡単にできるが、パラメーターをいじったり、UI/UXの改良を行おうとするとJupyterの実装に引っ張られて最適化が難しい
// \*
地味にリソース食う、そしてリソースの最適化を行うとなるとJupyter内部の処理に手を入れないと行けない感じ
// == React Native // \*Pros.\* // \*
マルチプラットフォーム対応（iOS、Android、Windows） // \*
Expo使うことでOTAアップデートが可能（今後のExpoバージョンアップで対応予定）
// \*Cons.\* // \* Kepler.glなどのインポート方法が不明（@+++

+++調査中）+++

+++ // \*\* WebGL使ってる関係上、WebViewで叩かないとダメな気がする // \*
使ったことないのでメンテナンスコストが見積もれない
