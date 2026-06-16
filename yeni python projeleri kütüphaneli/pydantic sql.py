from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine

# ... (Model ve engine kısımları aynı kalıyor) ...

# 1. Lifespan fonksiyonunu tanımlayalım
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Uygulama başlarken yapılacaklar (Startup)
    SQLModel.metadata.create_all(engine)
    yield
    # Uygulama kapanırken yapılacaklar (Shutdown)
    # Gerekirse buraya veritabanı bağlantısını kesme kodları gelir

# 2. FastAPI'yi bu lifespan ile başlatalım
app = FastAPI(lifespan=lifespan)

# Artık @app.on_event("startup") satırına ihtiyacın yok, silebilirsin!
