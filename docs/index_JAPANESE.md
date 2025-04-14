# Markdown to Testcase

マークダウンファイルからテストケースを抽出し、CSVとExcel形式に変換するPythonツールです。

![ロゴ](images/markdown2testcase.png)

## 特徴

- `### TestCases (ファイル名)` 形式のマークダウン見出しからテストケースを解析
- YAML入力ファイルの直接サポート
- CSVファイルの生成（テストケースセクションごとに1つ）
- すべてのテストケースを複数シートを持つ単一のExcelファイルにまとめる
- YAML解析エラーの詳細なレポートと提案
- 処理前のyamllintによる自動YAMLバリデーション
- loguruを使用したカラフルなコンソール出力

## クイックスタート

```bash
# PyPIからインストール
pip install markdown-to-testcase

# マークダウンファイルをテストケースに変換
markdown_to_testcase convert -i input_file.md

# yamllintによるバリデーションをスキップ
markdown_to_testcase convert -i input_file.md --no-yaml-lint
```

## 入力フォーマット例

### マークダウン形式

```markdown
### TestCases (ファイル名)
- ID: TC001
  Name: テストケース名
  Desc: テストケースの説明
  Pre-conditions: 前提条件
  Test Steps: テスト実行ステップ
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

### YAML形式

```yaml
filename1.md:
  - ID: TC001
    Name: テストケース名
    # ... 他のフィールド
  - ID: TC002
    Name: 別のテストケース
    # ... 他のフィールド
```

## プロジェクトの状態

このプロジェクトは積極的にメンテナンスされています。最新のアップデートや課題については[GitHubリポジトリ](https://github.com/tkykszk/markdown_to_testcase)を参照してください。
