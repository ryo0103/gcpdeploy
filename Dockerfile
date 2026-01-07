# Python 3.10のベースイメージを使用
FROM python:3.10-slim

# 作業ディレクトリを設定
WORKDIR /app

# システムの依存関係をインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Pythonの依存関係をコピーしてインストール
COPY pyproject.toml .
RUN pip3 install uv && uv pip install --system -r pyproject.toml

# アプリケーションファイルをコピー
COPY . .

# Streamlitのポートを公開
EXPOSE 8080

# ヘルスチェック
HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health

# Streamlitアプリを起動（Cloud Run向けに最適化）
ENTRYPOINT ["streamlit", "run", "examples/app.py", \
    "--server.port=8080", \
    "--server.address=0.0.0.0", \
    "--server.headless=true", \
    "--server.enableCORS=false", \
    "--server.enableXsrfProtection=false"]