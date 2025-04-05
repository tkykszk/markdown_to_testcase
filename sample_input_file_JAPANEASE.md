# テストケース仕様書

このファイルには複数のテストケースセクションが含まれています。

## 温度変換機能テスト

### TestCases (fahrenheit_to_celsius.md)
- ID: TC001
  Name: 通常の華氏温度（32°F）を摂氏へ変換
  Desc: 氷点である32°Fを入力し、摂氏0°Cが返ることを確認する
  Pre-conditions: 関数が小数点以下の計算に対応していること
  Test Steps: 1. 入力値 32°F を関数に渡す\n2. 結果を検証
  Expected Result: 1. 関数の例外が発生しない\n2. 0.0
  Test Data: 32
  Priority: 高
  Severity: 中
  Status: 未実施
  Environment: Python 3.12, macOS
  Tested By: 開発者
  Date: 2025-04-05
  Comments/Notes: 華氏32度は摂氏0度に相当

- ID: TC002
  Name: 華氏100°Fの変換
  Desc: 100°Fを摂氏に変換し、37.78°C付近の値になることを確認する
  Test Steps: 1. 入力値 100°F を渡す \n2. 返値を検証
  Expected Result: 1. 関数の例外が発生しない\n2. 結果が37.78±0.01であることを確認
  Test Data: 100
  Priority: 中
  Severity: 低
  Status: 未実施
  Environment: Python 3.12
  Tested By: テスト担当者
  Comments/Notes: 結果は浮動小数点なので誤差に注意

- ID: TC003
  Name: マイナスの華氏値の変換
  Desc: 華氏 -40°F を入力し、摂氏 -40°C が返ることを確認する
  Test Steps: 1. 入力値 -40°F を渡す \n2. 結果を確認
  Expected Result: 1. 例外が発生しないこと、結果が-40.0であること
  Test Data: -40
  Priority: 高
  Severity: 高
  Status: 未実施
  Environment: Python 3.12, Linux
  Comments/Notes: -40°Fと-40°Cは一致する唯一の温度

## API機能テスト

### TestCases (api_temperature_conversion.md)
- ID: TC101
  Name: APIに32°Fを送信し摂氏0°Cを取得
  Desc: 氷点となる華氏32度をAPI経由で送信し、摂氏0.0が返却されるか確認する
  Pre-conditions: "APIが稼働していること、エンドポイント: /convert"
  Test Steps: |
    1. 以下のJSONをPOST送信:
       {
         "fahrenheit": 32
       }
    2. HTTP 200が返ること
    3. レスポンスJSONの "celsius" フィールドが 0.0 であること
  Expected Result: '{"celsius": 0.0}'
  Test Data: '{"fahrenheit": 32}'
  Priority: 高
  Severity: 中
  Status: 未実施
  Environment: APIサーバ localhost:5000, Python FastAPI
  Tested By: 開発者
  Comments/Notes: 数値は浮動小数点で返る想定

- ID: TC102
  Name: 100°FをAPIで送信し摂氏に変換
  Desc: 100°F -> 約37.78°C の変換を確認する
  Test Steps: |
    1. JSON {"fahrenheit": 100} をAPIに送信
    2. HTTP 200のレスポンス確認
    3. "celsius" 値が 37.78±0.01 の範囲にあることを確認
  Expected Result: '{"celsius": 約37.78}'
  Test Data: '{"fahrenheit": 100}'
  Priority: 中
  Severity: 低
  Status: 未実施
  Environment: Postman または curl
  Comments/Notes: 浮動小数点誤差に注意

## 文字列フォーマット機能テスト

### TestCases (format_number_with_commas.md)
- ID: TC201
  Name: 整数値を3桁区切りでカンマ挿入
  Desc: int型またはfloat型の値を文字列に変換し、整数部分にカンマを3桁ごとに挿入する関数のテスト
  Pre-conditions: |
    - 入力は int または float の型
    - 出力は str 型であること
    - 小数点以下はそのまま維持される（例：1234567.89 → "1,234,567.89"）
    - マイナス値の場合でも符号位置は変わらない（例：-1234 → "-1,234"）
  Test Steps: |
    1. 以下の複数の入力値を対象関数に与える
        - 1
        - 123
        - 1234
        - 123456789
        - 123456789012
        - 1234567.89
        - -987654321
        - 0
    2. 返された出力文字列に対して、カンマ区切りが正しい位置（3桁区切り）で挿入されているか検証
    3. float型の値については小数点以下の桁が維持されていることを確認
    4. 出力が文字列であることを確認
  Expected Result: |
    - 入力 1 → 出力 "1"
    - 入力 123 → 出力 "123"
    - 入力 1234 → 出力 "1,234"
    - 入力 123456789 → 出力 "123,456,789"
    - 入力 123456789012 → 出力 "123,456,789,012"
    - 入力 1234567.89 → 出力 "1,234,567.89"
    - 入力 -987654321 → 出力 "-987,654,321"
    - 入力 0 → 出力 "0"
  Test Data: [1, 123, 1234, 123456789, 123456789012, 1234567.89, -987654321, 0]
  Priority: 高
  Severity: 中
  Status: 未実施
  Environment: Python 3.12, Windows/macOS/Linux
  Tested By: 開発者A
  Date: 2025-04-05
  Comments/Notes: 仕様として、整数部のみカンマ区切りの対象とし、小数部はそのまま残す
