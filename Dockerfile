# 開発・デバッグ用イメージ作成
FROM lambda-stack:20.04

WORKDIR /workspace

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV TRANSFORMERS_CACHE /workspace/transformers_cache
ENV TOKENIZERS_PARALLELISM=false