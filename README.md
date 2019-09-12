# XOR

XOR暗号に関するスクリプト等

[![MIT](https://img.shields.io/badge/license-MIT-blue)](https://osdn.net/projects/opensource/wiki/licenses%2FMIT_license)
[![Python 3.7.4](https://img.shields.io/badge/Python-3.7.4-blue)](https://www.python.org/downloads/release/python-374/)

## XOR暗号とは

排他的論理和（XOR、⊕で表す）を用いて暗号化する手法。平文、暗号文、鍵すべてがバイナリ。

平文を X、鍵を Yと置いたときに、X ⊕ Y ⊕ Y = X が成り立つ。つまり暗号文をもう一度鍵と XOR すれば平文が出てくる。

## スクリプトの説明

### `encrypt.py`

[`encrypt.py`](./encrypt.py) は `flag.txt` で与えられた文字列を `key.txt` で与えられた鍵を元に暗号化するスクリプトです。暗号文は `enc.txt` に保存されます。

### `decrypt.py`（未完成）

***注意: このスクリプトは未完成です。以下の説明は実装予定の機能です。***

`decrypt.py` は鍵を総当たりで見つけ出すスクリプトです。ASCII 文字で表示可能な 32 〜 126 番の文字を鍵と仮定して、排他的論理和を取った結果を出力します。実行時の引数で鍵長を指定することもできます。

## LICENSE

(c) 2019 luxuria.
