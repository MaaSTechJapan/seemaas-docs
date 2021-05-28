.. docs-traisare documentation master file, created by
   sphinx-quickstart on Sun May 16 14:51:10 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to TraISARE documentation!
=========================================

=================
What is TraISARE?
=================
TraISAREは遍く交通輸送情報を統一したインターフェース処理する基盤である。

都市部における渋滞や人口密集、過疎地域での公共交通の維持、観光地における回遊消費の促進、新しい生活様式、安心安全な移動と経済活動の両立など、数多くの交通に関する課題が存在する。これらの課題解決に期待されているのが、多様な交通を一つのサービスに統合するMaaS（Mobility as a Service）である。しかし、この実現に必要となる駅やバス停などの地理情報、時刻表情報、運行情報などは事業者・開発ベンダーごとに異なっているケースが多く、事業者の垣根を越えたサービス開発やデータの活用が困難である。交通におけるデータ活用、サービス開発をより高度に進めていくために交通データ統合基盤TraISAREを開発した。

TraISAREではデータの統合、集計、提供を統一した方法で実現する基盤である。そのため以下の機能を実現する。
- Reciever
各社から提供される交通データの受信
- Encoder
提供されたRAWデータの正規化・抽象化
- Aggregator
正規化・抽象化されたデータの集計

TraISAREは交通データ統合基盤(Transport Information Store)であり、基盤として集計(Aggregate)、受信(Receive)、変換(Encode)機能をもつものであるので、これらを統合した **Tra**nsport **I**nformation **S**tore with **A**ggregator, **R**eceiver and **E** ncoderから命名した。

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   ./abstraction.md
   ./systemconfig.md
   ./functions.md
   ./traiire.md
 
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
