# インストールガイド

## 前提条件

- Python 3.12以上
- yamllint（YAML検証用）

## PyPIからのインストール

Markdown to Testcaseのインストールは、pipを使用することが推奨されています：

```bash
pip install markdown-to-testcase
```

## ソースからのインストール

ソースからインストールする場合：

```bash
# リポジトリをクローン
git clone https://github.com/tkykszk/markdown_to_testcase.git
cd markdown_to_testcase

# 依存関係をインストール
pip install -r requirements.txt

# オプション：開発モードでインストール
pip install -e .
```

## バイナリインストール

### Windows

最新の`.exe`ファイルを[リリースページ](https://github.com/tkykszk/markdown_to_testcase/releases)からダウンロードして直接実行できます。

```powershell
# コマンドラインから
markdown_to_testcase.exe convert -i input_file.md
```

### macOS（Homebrew）

```bash
# Homebrewを使用してインストール
brew tap tkykszk/markdown_to_testcase
brew install markdown_to_testcase

# コマンドを実行
markdown_to_testcase convert -i input_file.md
```

### Ubuntu/Debian（apt）

```bash
# リポジトリを追加
curl -s https://tkykszk.github.io/markdown_to_testcase/apt/KEY.gpg | sudo apt-key add -
echo "deb https://tkykszk.github.io/markdown_to_testcase/apt ./" | sudo tee /etc/apt/sources.list.d/markdown_to_testcase.list

# パッケージリストを更新してインストール
sudo apt update
sudo apt install markdown-to-testcase

# コマンドを実行
markdown_to_testcase convert -i input_file.md
```

## インストールの確認

インストールが成功したことを確認するには、次のコマンドを実行します：

```bash
markdown_to_testcase --version
```

これにより、インストールされたパッケージのバージョン情報が表示されます。
