# docs-traisare::Documents about TraISARE

# 編集方法

```bash
# Auto reload
sphinx-autobuild docs docs/_build/html
```

# 古いSpecをポートする

## 環境構築
```
$ gem install asciidoctor
```

## asciidoc形式のSpecをmarkdownへ変換  
Tips:
https://karinavarela.me/2020/05/06/converting-asciidoc-to-markdown/  

pandocファイルを生成(index.xml)
```
$ asciidoctor -b docbook index.adoc
```
pandocでxmlをmarkdownへ変換
```
$ pandoc -f docbook -t markdown_strict index.xml index.adoc -o index.md
```

~~- kramdown-asciidoc使って、AsciidocをMarkdownにする~~
		~~- gem install kramdown-asciidoc~~

~~https://www.sphinx-doc.org/ja/master/usage/markdown.html~~  

# markdownからhtmlをビルド
シェルに入って作業する. `_build/html/`にコンパイル結果が格納される.
```
$ pipenv shell

$(docs-traisare) make html
```

# コンパイルしたhtmlを削除
```
$(docs-traisare) make clean
```

# ER図の描画
ER alchemy: https://blog.amedama.jp/entry/2017/12/30/063023

## 環境

### ER alchemy:
```
$ pipenv install eralchemy
```

### pygraphviz
ER alchemyはバックグランドでgraphvizを使用するので、インストールする必要がある。加えてpythonラッパーであるpygraphvizのインストール必要。ただでは入らないので、コツが必要。

```
$ pipenv shell  #pipenvのシェルに入る

$(docs-traisare) sudo apt-get install graphviz graphviz-dev  #シェル内でgraphvizをインストールする

$(docs-traisare) exit  #シェルを抜ける

$ pipenv install pygraphviz  #pygraphvizをインストールする
```
## Usage
render-erdiagram.py
```
from eralchemy import render_er

render_er(f"{inputdir}{inputfile}", f"{outputdir}{outputfile}")
```

