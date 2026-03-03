# Python UV Starter Template

Python プロジェクトを uv と FastAPI で始めるためのテンプレートリポジトリです。

## 特徴

- 🚀 [uv](https://github.com/astral-sh/uv) - 高速な Python パッケージマネージャー
- ⚡ [FastAPI](https://fastapi.tiangolo.com/) - モダンで高速な Web フレームワーク
- 🔍 [Ruff](https://github.com/astral-sh/ruff) - 超高速な Python リンター・フォーマッター
- 🎯 [MyPy](https://mypy.readthedocs.io/) - 静的型チェック
- ✅ [Pytest](https://pytest.org/) - テストフレームワーク
- 🔄 GitHub Actions CI - 自動 lint チェック

## 必要要件

- Python 3.11 以上
- [uv](https://github.com/astral-sh/uv) パッケージマネージャー

## セットアップ手順

### 1. uv のインストール

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

###  依存関係のインストール

```bash
# Python 環境と依存関係を自動セットアップ
uv sync

# 開発用依存関係も含める
uv sync --all-extras
```

### 4. サーバーの起動

```bash
# 開発サーバーを起動
uv run uvicorn app.main:app --reload
```

サーバーが起動したら、以下のURLでアクセスできます：

- API: http://localhost:8000
- ドキュメント: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 開発コマンド

### テストの実行

```bash
# すべてのテストを実行
uv run pytest

# カバレッジ付きでテストを実行
uv run pytest --cov=app --cov-report=html
```

### リンター・フォーマッター

```bash
# コードフォーマット
uv run ruff format .

# リントチェック
uv run ruff check .

# リントを自動修正
uv run ruff check --fix .
```

### 型チェック

```bash
# MyPy で型チェック
uv run mypy app
```

## プロジェクト構造

```
.
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI アプリケーションエントリーポイント
│   └── api/
│       ├── __init__.py
│       └── routes/
│           ├── __init__.py
│           ├── health.py    # ヘルスチェックエンドポイント
│           └── items.py     # Items CRUD エンドポイント
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_items.py
├── .github/
│   └── workflows/
│       └── ci.yml           # CI 設定
├── pyproject.toml           # プロジェクト設定と依存関係
├── uv.lock                  # ロックファイル
├── .gitignore
└── README.md
```

## API エンドポイント

### ヘルスチェック

```bash
GET /health
```

### Items CRUD

```bash
# すべてのアイテムを取得
GET /api/v1/items

# 新しいアイテムを作成
POST /api/v1/items

# 特定のアイテムを取得
GET /api/v1/items/{item_id}

# アイテムを更新
PUT /api/v1/items/{item_id}

# アイテムを削除
DELETE /api/v1/items/{item_id}
```

## CI/CD

GitHub Actions を使用して、以下のチェックを自動実行します：

- ✅ Ruff によるコードフォーマットチェック
- ✅ Ruff によるリントチェック
- ✅ MyPy による型チェック
- ✅ Pytest によるテスト実行

## 既存の requirements.txt ベースのプロジェクトで uv を使う

uv は `pyproject.toml` ベースのプロジェクトだけでなく、既存の `requirements.txt` を使用するプロジェクトでも利用できます。**爆速な pip** として、インストール速度を劇的に向上させることができます。

### 基本的な使い方

uv には `uv pip` という、従来の pip コマンドをエミュレートするインターフェースが用意されています。

```bash
# 仮想環境の作成
uv venv

# 仮想環境の有効化
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

# パッケージのインストール
uv pip install -r requirements.txt
```

### uv を使うメリット

- **圧倒的なスピード**: Rust 製のため、pip より数倍〜数十倍高速です。特に依存関係が多いプロジェクトでは、CI/CD の時間を大幅に短縮できます。
- **強力なレゾルバ**: 依存関係の競合解決が非常に賢く、かつ高速です。
- **グローバルキャッシュ**: 一度ダウンロードしたパッケージはキャッシュされるため、別のプロジェクトで同じパッケージを使う際は一瞬で終わります。

### 依存関係の固定管理（pip-tools の代わり）

バージョン固定（Lock）をしっかり管理したい場合は、`uv pip compile` が便利です。

```bash
# requirements.in に直接必要なライブラリ名だけを記述
# 例: requirements.in
# fastapi
# uvicorn
# pytest

# 依存関係を解決して requirements.txt を生成
uv pip compile requirements.in -o requirements.txt

# 生成された requirements.txt からインストール
uv pip install -r requirements.txt
```

この方法により、直接依存しているパッケージ（`requirements.in`）と、すべての依存関係が固定されたファイル（`requirements.txt`）を分離して管理できます。

### 既存プロジェクトへの導入手順

1. uv をインストール
2. `pip install` を `uv pip install` に置き換える
3. CI/CD のパイプラインでも `uv pip` を使用する

既存のワークフローを大きく変えずに、インストール速度だけを劇的に向上させることができます。

## ライセンス

MIT

## 貢献

Issue や Pull Request を歓迎します！

詳細なガイドラインは [.github_instructions.md](.github_instructions.md) を参照してください。
