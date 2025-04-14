# チュートリアル

このページでは、Markdown to Testcaseツールを使用してテストケースを作成および変換するためのチュートリアルを紹介します。

## クイックスタート: 各言語用のテストケースの作成

このクイックスタートガイドでは、異なるプログラミング言語での単純な関数のテストケースを作成し、CSVおよびExcel形式に変換する方法を紹介します。

タイピングゲームの完全な例に進む前に、まずは異なるプログラミング言語での `add` 関数のテスト例から始めましょう。

`function_tests.md` という名前のファイルを以下の内容で作成します：

```markdown
# 関数テスト

異なるプログラミング言語におけるadd関数のテストケース。

### TestCases (csharp_tests.csv)
- ID: CS001
  Name: C# Add関数 - 正の数
  Desc: 正の整数でadd関数をテストする
  Pre-conditions: C#環境がセットアップされ、関数が実装されている
  Test Steps: |
    1. Add(5, 3)を呼び出す
    2. 結果を検証する
  Expected Result: |
    - 関数は8を返す
  Actual Result: 
  Test Data: a=5, b=3
  Priority: 高
  Severity: 高
  Status: 未実行
  Environment: .NET 7.0
  Tested By: 
  Date: 
  Comments/Notes: 整数加算の基本テストケース

- ID: CS002
  Name: C# Add関数 - 負の数
  Desc: 負の整数でadd関数をテストする
  Pre-conditions: C#環境がセットアップされ、関数が実装されている
  Test Steps: |
    1. Add(-5, -7)を呼び出す
    2. 結果を検証する
  Expected Result: |
    - 関数は-12を返す
  Actual Result: 
  Test Data: a=-5, b=-7
  Priority: 高
  Severity: 高
  Status: 未実行
  Environment: .NET 7.0
  Tested By: 
  Date: 
  Comments/Notes: 負の数の処理を検証

### TestCases (nodejs_tests.csv)
- ID: JS001
  Name: Node.js Add関数 - 整数加算
  Desc: 整数でadd関数をテストする
  Pre-conditions: Node.js環境がセットアップされ、関数が実装されている
  Test Steps: |
    1. add(10, 20)を呼び出す
    2. 結果を検証する
  Expected Result: |
    - 関数は30を返す
  Actual Result: 
  Test Data: a=10, b=20
  Priority: 高
  Severity: 高
  Status: 未実行
  Environment: Node.js 20.0
  Tested By: 
  Date: 
  Comments/Notes: JavaScript基本整数加算

- ID: JS002
  Name: Node.js Add関数 - 浮動小数点
  Desc: 浮動小数点数でadd関数をテストする
  Pre-conditions: Node.js環境がセットアップされ、関数が実装されている
  Test Steps: |
    1. add(2.5, 3.5)を呼び出す
    2. 結果を検証する
  Expected Result: |
    - 関数は6.0を返す
  Actual Result: 
  Test Data: a=2.5, b=3.5
  Priority: 中
  Severity: 中
  Status: 未実行
  Environment: Node.js 20.0
  Tested By: 
  Date: 
  Comments/Notes: 浮動小数点加算の検証

### TestCases (python_tests.csv)
- ID: PY001
  Name: Python Add関数 - 基本加算
  Desc: 単純な整数でadd関数をテストする
  Pre-conditions: Python環境がセットアップされ、関数が実装されている
  Test Steps: |
    1. add(42, 58)を呼び出す
    2. 結果を検証する
  Expected Result: |
    - 関数は100を返す
  Actual Result: 
  Test Data: a=42, b=58
  Priority: 高
  Severity: 高
  Status: 未実行
  Environment: Python 3.12
  Tested By: 
  Date: 
  Comments/Notes: Python基本加算

- ID: PY002
  Name: Python Add関数 - 文字列連結
  Desc: 文字列入力でadd関数をテストする
  Pre-conditions: Python環境がセットアップされ、関数が文字列を処理できる
  Test Steps: |
    1. add("こんにちは、", "世界")を呼び出す
    2. 結果を検証する
  Expected Result: |
    - 関数は「こんにちは、世界」を返す
  Actual Result: 
  Test Data: a="こんにちは、", b="世界"
  Priority: 中
  Severity: 中
  Status: 未実行
  Environment: Python 3.12
  Tested By: 
  Date: 
  Comments/Notes: 関数がオーバーロードされている場合の文字列連結テスト

### TestCases (cpp_tests.csv)
- ID: CPP001
  Name: C++ Add関数 - 整数加算
  Desc: 整数でadd関数をテストする
  Pre-conditions: C++環境がセットアップされ、関数が実装されている
  Test Steps: |
    1. add(100, 200)を呼び出す
    2. 結果を検証する
  Expected Result: |
    - 関数は300を返す
  Actual Result: 
  Test Data: a=100, b=200
  Priority: 高
  Severity: 高
  Status: 未実行
  Environment: GCC 13.1
  Tested By: 
  Date: 
  Comments/Notes: C++基本加算

- ID: CPP002
  Name: C++ Add関数 - 大きな数値
  Desc: オーバーフローをチェックするために大きな整数でadd関数をテストする
  Pre-conditions: C++環境がセットアップされ、関数が実装されている
  Test Steps: |
    1. add(2147483647, 1)を呼び出す
    2. 結果の動作を検証する
  Expected Result: |
    - 関数は仕様に従ってオーバーフローを処理する
    - int型の場合、-2147483648にオーバーフローする可能性がある
    - longを使用またはオーバーフロー検出を行う場合、適切な結果またはエラーを返す
  Actual Result: 
  Test Data: a=2147483647 (INT_MAX), b=1
  Priority: 中
  Severity: 高
  Status: 未実行
  Environment: GCC 13.1
  Tested By: 
  Date: 
  Comments/Notes: 整数オーバーフロー処理のテスト
```

Markdown to Testcaseツールを実行してこれらのテストケースを変換します：

```bash
markdown_to_testcase convert -i function_tests.md
```

これにより、以下の出力ファイルが生成されます：

- `csharp_tests.csv`
- `nodejs_tests.csv`
- `python_tests.csv`
- `cpp_tests.csv`
- 個別のシートにすべてのテストケースを含む `test_cases.xlsx`

この簡単な例では、異なるプログラミング言語での単純な関数のテストケースを作成する方法を紹介しました。

## チュートリアル: タイピングゲームのテスト

このチュートリアルでは、より複雑なタイピングゲームアプリケーションのテストケースをマークダウン形式で作成し、変換する方法を説明します。

### サンプルアプリケーション: Speed Typer

このチュートリアルでは、以下の機能を持つ「Speed Typer」というタイピングゲームをテストしていると想定します：

- ユーザーは画面に表示されるフレーズをタイプする
- 速度と正確性が測定される
- 異なる難易度レベル
- リーダーボード機能
- ユーザーアカウントとプロフィール

## ステップ1: マークダウンでテストケースを作成する

まず、テストケースを含むマークダウンファイルを作成します。`typing_game_tests.md`というファイルを以下の内容で作成します：

```markdown
# Speed Typerタイピングゲームテスト

このドキュメントはSpeed Typerタイピングゲームアプリケーションのテストケースを含んでいます。

## はじめに

Speed Typerはタイピング速度と正確性を測定するタイピングゲームです。

### TestCases (core_functionality.csv)
- ID: TC001
  Name: 基本タイピングテスト
  Desc: 基本的なタイピング機能が正しく動作することを確認する
  Pre-conditions: アプリケーションが起動され、メイン画面が表示されている
  Test Steps: |
    1. 「新しいゲームを開始」ボタンをクリックする
    2. 「かんたん」難易度を選択する
    3. 表示されたフレーズを正確にタイプする
    4. タイピングチャレンジを完了する
  Expected Result: |
    - タイピング入力が正しく登録される
    - 正確さとWPM（1分あたりの単語数）が計算される
    - 正しい統計情報を含む結果画面が表示される
  Actual Result: 
  Test Data: サンプルフレーズ「素早い茶色のキツネは怠け者の犬を飛び越える」
  Priority: 高
  Severity: 高
  Status: 未実行
  Environment: Chrome 120.0.6099.130、Windows 11
  Tested By: 
  Date: 
  Comments/Notes: これはコア機能テストです

- ID: TC002
  Name: エラー処理 - 誤キー押下
  Desc: 誤ったキーストロークが正しく識別されることを確認する
  Pre-conditions: ゲームが開始され、フレーズが表示されている
  Test Steps: |
    1. 表示されたフレーズのタイプを開始する
    2. 意図的に一部の文字に対して間違ったキーを押す
  Expected Result: |
    - 間違ったキーストロークが赤色でハイライトされる
    - エラーカウントが増加する
    - 正確度パーセンテージがそれに応じて減少する
  Actual Result: 
  Test Data: 利用可能な任意のフレーズ
  Priority: 高
  Severity: 中
  Status: 未実行
  Environment: Chrome 120.0.6099.130、Windows 11
  Tested By: 
  Date: 
  Comments/Notes: エラー検出は正確性計算において重要です

### TestCases (user_management.csv)
- ID: TC101
  Name: ユーザー登録
  Desc: 新しいユーザーが登録できることを確認する
  Pre-conditions: アプリケーションが起動され、ログイン画面が表示されている
  Test Steps: |
    1. 「登録」ボタンをクリックする
    2. ユーザー名「testuser123」を入力する
    3. メールアドレス「test@example.com」を入力する
    4. パスワード「Password123!」を入力する
    5. パスワード確認「Password123!」を入力する
    6. 「送信」ボタンをクリックする
  Expected Result: |
    - 登録成功メッセージが表示される
    - ユーザーはログインページにリダイレクトされる
    - 新しい認証情報でログインできる
  Actual Result: 
  Test Data: ユーザー名：testuser123、メール：test@example.com、パスワード：Password123!
  Priority: 高
  Severity: 高
  Status: 未実行
  Environment: Chrome 120.0.6099.130、Windows 11
  Tested By: 
  Date: 
  Comments/Notes: 

- ID: TC102
  Name: ユーザーログイン
  Desc: 既存ユーザーがログインできることを確認する
  Pre-conditions: ユーザーが登録済み
  Test Steps: |
    1. ログイン画面に移動する
    2. ユーザー名「testuser123」を入力する
    3. パスワード「Password123!」を入力する
    4. 「ログイン」ボタンをクリックする
  Expected Result: |
    - ログイン成功
    - ユーザーはメインメニューにリダイレクトされる
    - ユーザーのプロフィール情報が正しく表示される
  Actual Result: 
  Test Data: ユーザー名：testuser123、パスワード：Password123!
  Priority: 高
  Severity: 高
  Status: 未実行
  Environment: Chrome 120.0.6099.130、Windows 11
  Tested By: 
  Date: 
  Comments/Notes: 

### TestCases (leaderboard_functionality.csv)
- ID: TC201
  Name: リーダーボード表示
  Desc: リーダーボードが正しいスコアを表示することを確認する
  Pre-conditions: 複数のユーザーがタイピングテストを完了している
  Test Steps: |
    1. testuser123としてログインする
    2. 「リーダーボード」セクションに移動する
  Expected Result: |
    - リーダーボードが表示される
    - スコアが高いものから低いものへとソートされている
    - ユーザーランキングが正しく表示される
    - 現在のユーザーの位置がハイライトされている
  Actual Result: 
  Test Data: 
  Priority: 中
  Severity: 低
  Status: 未実行
  Environment: Chrome 120.0.6099.130、Windows 11
  Tested By: 
  Date: 
  Comments/Notes: 

- ID: TC202
  Name: 自己ベストスコア
  Desc: 自己ベストスコアが追跡されることを確認する
  Pre-conditions: ユーザーが複数のタイピングテストを完了している
  Test Steps: |
    1. testuser123としてログインする
    2. 以前の試行よりも良いスコアでタイピングテストを完了する
    3. 「プロフィール」ページに移動する
  Expected Result: |
    - 新しい自己ベストがプロフィールに表示される
    - 過去のスコアが履歴で確認できる
    - 新しいスコアがリーダーボードに反映される
  Actual Result: 
  Test Data: 
  Priority: 中
  Severity: 中
  Status: 未実行
  Environment: Chrome 120.0.6099.130、Windows 11
  Tested By: 
  Date: 
  Comments/Notes: 
```

## ステップ2: テストケースを処理する

テストケースを含むマークダウンファイルを作成したら、Markdown to Testcaseツールを使用して変換します：

```bash
markdown_to_testcase convert -i typing_game_tests.md
```

## ステップ3: 出力を確認する

ツールを実行した後、`output`ディレクトリで以下を確認します：

1. CSVファイル：
   - `core_functionality.csv`
   - `user_management.csv`
   - `leaderboard_functionality.csv`

2. Excelファイル：
   - `test_cases.xlsx`（テストケースセクションごとに1つのシートを含む）

## ステップ4: テストケースの使用

これらのテストケースは次のように使用できます：

1. QAチームに配布する
2. テスト管理ツールにインポートする
3. 手動テストに使用する
4. テスト実行ステータスを追跡する

## 応用編: テストセクションの追加

マークダウンファイルにさらにセクションを追加してテストケースを拡張できます：

```markdown
### TestCases (difficulty_levels.csv)
- ID: TC301
  Name: 難易度選択
  Desc: 異なる難易度レベルを選択できることを確認する
  Pre-conditions: ユーザーがログインしてメインメニューにいる
  Test Steps: |
    1. 「新しいゲーム」をクリックする
    2. 利用可能な難易度オプションを表示する
  Expected Result: |
    - かんたん、普通、難しいの難易度オプションが表示される
    - 各オプションに簡単な説明が表示される
  Actual Result: 
  Test Data: 
  Priority: 中
  Severity: 中
  Status: 未実行
  Environment: Chrome 120.0.6099.130、Windows 11
  Tested By: 
  Date: 
  Comments/Notes: 
```

変換を再度実行して、新しいセクションを出力ファイルに含めます。

## 効果的なテストケースのためのヒント

1. **具体的にする**: 明確な前提条件とテストステップを含める
2. **テストデータを含める**: テスト中に使用するサンプルデータを提供する
3. **優先順位付け**: テスト作業に焦点を当てるため、適切な優先度と重大度を割り当てる
4. **論理的にグループ化**: 異なる機能領域に対して異なるセクションを使用する
5. **トレーサビリティを維持する**: テストケースを要件やユーザーストーリーにリンクする

## 結論

Markdown to Testcaseツールを使用すると、テストケースを読みやすい形式で維持しながら、テスト実行と追跡に適した形式にエクスポートすることが簡単になります。マークダウン内の柔軟なYAML形式により、特定のテストニーズに合わせて簡単に拡張できる構造化データが可能になります。
