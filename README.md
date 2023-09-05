# wsl-django-base

# Python 仮想環境アクティブ
source .venv/bin/activate

# Python 仮想環境終了
deactivate


# 開発サーバ起動コマンド
python manage.py runserver 0.0.0.0:8000

# マイグレーションファイル作成
python manage.py makemigrations [アプリ名]

# マイグレーション実行
python manage.py migrate

