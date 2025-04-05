# common-modules

# 備忘録

## 指定した文字数に線を入れる方法

https://qiita.com/shizen-shin/items/69ebad537674668c3996

> (1) ctrl + shift + p　でコマンド入力窓を表示する。
> (2) settings.jsonを入力
> 
> image.png
> 
> (3) 「基本設定を開く」をクリック
> (4)　"editor.rulers": [80]を追記（線をひきたい文字数をカッコに入れる。）
> 
> ```json
> {
>   "workbench.iconTheme": "vs-minimal",
>    
>    省略
>    
>   "emmet.triggerExpansionOnTab": true,
>   "editor.rulers": [80]
> }
> ```
> 上の行末に,必須。下にも行が続く場合は、挿入した行の末尾に,をつける。
> 
> 
> ラインを複数引く方法 `[ ]`に複数の数値をカンマでつないで記載すれば、線を複数引くことができる。