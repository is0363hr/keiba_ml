from sqlalchemy import create_engine
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from config.local_setting import DATABASE_URI


ENGINE = create_engine(
    DATABASE_URI, encoding="utf-8", echo=True
)  # Trueだと実行のたびにSQLが出力される
# Sessionの作成
session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するなど。
    sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()
