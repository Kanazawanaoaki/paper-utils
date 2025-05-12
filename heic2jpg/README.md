# paper-utils extra heic2jpg

[pyheifのインストール](https://github.com/carsales/pyheif#installation )が必要．

## heicファイルをjpgに変換する

- heicファイルをheicフォルダに入れる

- 変換を行う
```
python3 heic2jpg.py
```

新しいheic形式にも対応. `pip install pillow pillow-heif`が必要．
```bash
python3 new_heic2jpg.py
```


- jpgフォルダにjpgファイルが入っている

- 不要になった画像ファイルを削除する

heicファイルもjpgファイルも削除されてしまうので注意

```
python3 clean.py
```

