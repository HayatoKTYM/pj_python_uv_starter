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

## ライセンス

MIT

## 貢献

Issue や Pull Request を歓迎します！

詳細なガイドラインは [.github_instructions.md](.github_instructions.md) を参照してください。
