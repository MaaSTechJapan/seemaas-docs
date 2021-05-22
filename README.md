# docs-traisare::Documents about TraISARE
# ディレクトリ構成
```
- docs-traisare
   |- index.md
   |- images
   |- TraISARE
      |- index.md
      |- images
   |- TraIIRe
      |- index.md
      |- images   
   |- TraICon
      |- index.md
      |- images
```

# 古いSpecをポートする
## 環境構築
```
$ gem install asciidoctor
```

## asciidoc形式のSpecをmarkdownへ変換  
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

