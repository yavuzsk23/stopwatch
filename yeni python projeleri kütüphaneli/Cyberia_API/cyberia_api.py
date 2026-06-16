from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select

# 1. Önce Veritabanı Motorunu (Engine) Tanımla
sqlite_url = "sqlite:///cyberia_data.db"
engine = create_engine(sqlite_url) # Hata buradaydı, bu satır üstte olmalı!

# 2. Sonra Lifespan Fonksiyonunu Yaz
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Uygulama açılırken tabloları oluştur
    SQLModel.metadata.create_all(engine)
    yield

# 3. Sonra FastAPI'yi Başlat
app = FastAPI(lifespan=lifespan)

# Diğer modeller ve endpointler aşağıda devam edebilir...
