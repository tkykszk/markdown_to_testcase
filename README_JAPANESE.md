# Markdown to Testcase

マークダウンファイルからテストケースを抽出し、CSVおよびExcel形式に変換するPythonツールです。

## 機能

- `### TestCases (ファイル名)` 形式のマークダウン見出しからテストケースを解析
- 直接YAMLファイルをサポート
- CSVファイルの生成（テストケースセクションごとに1つ）
- すべてのテストケースを複数シートを持つ単一のExcelファイルにまとめる
- YAMLパース問題に関する詳細なエラーレポートと提案
- loguruを使用したカラフルなコンソール出力

## インストール

```bash
# リポジトリをクローン
git clone https://github.com/tkykszk/markdown_to_testcase.git
cd markdown_to_testcase

# 依存関係のインストール
pip install -r requirements.txt
```

## 使い方

基本的な使い方:

```bash
python main.py convert -i 入力ファイル.md
```

利用可能なすべてのオプション:

```bash
python main.py convert -i 入力ファイル.md -o 出力ディレクトリ -F --verbose
```

### コマンドラインオプション

- `-i, --input`: 入力マークダウンまたはYAMLファイルのパス（必須）
- `-o, --output-dir`: 出力ファイルを保存するディレクトリ（デフォルト: `output`）
- `-F, --force`: 確認なしで出力ファイルを上書き
- `-d, --debug`: デバッグモードを有効化（DEBUGレベルのログを出力）
- `--verbose`: YAMLパース問題に関する詳細なエラーメッセージと提案を表示
- `-v, --version`: バージョン情報を表示

## 入力フォーマット

### マークダウンフォーマット

このツールは、次の形式に一致するマークダウンファイル内のセクションを探します:

```markdown
### TestCases (ファイル名)
- ID: TC001
  Name: テストケース名
  Desc: テストケースの説明
  Pre-conditions: 必要な前提条件
  Test Steps: テストを実行するための手順
  Expected Result: 期待される結果
  Actual Result: 実際の結果（テスト後に記録）
  Test Data: 使用するテストデータ
  Priority: 高/中/低
  Severity: 高/中/低
  Status: 未実行/合格/不合格
  Environment: テスト環境情報
  Tested By: テスター名
  Date: テスト日
  Comments/Notes: 追加メモ
```

1つのセクションに複数のテストケースを含めることができ、1つのファイルに複数のセクションを含めることができます。

### YAMLフォーマット

このツールは、次の形式の直接YAMLファイルもサポートしています:

```yaml
filename1.md:
  - ID: TC001
    Name: テストケース名
    # ... その他のフィールド
  - ID: TC002
    Name: 別のテストケース
    # ... その他のフィールド

filename2.md:
  - ID: TC101
    Name: 別ファイル用のテストケース
    # ... その他のフィールド
```

## 出力

- CSVファイルは指定された出力ディレクトリ（デフォルト: `output`）に作成され、テストケースセクションごとに1つのファイルが生成されます。
- `test_cases.xlsx`という名前のExcelファイルが出力ディレクトリに作成され、テストケースセクションごとに1つのシートが含まれます。

## 開発

### 要件

- Python 3.12+
- `requirements.txt`にリストされている依存関係

### テスト

```bash
pytest
```

### コードフォーマット

```bash
black .
flake8
```

## ライセンス

MIT
