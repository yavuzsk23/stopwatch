from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Gelen verinin kalıbını belirliyoruz
class Kullanici(BaseModel):
    isim: str
    yas: int

@app.get("/")
def ana_sayfa():
    return {"durum": "Oldu bu is!", "yavuz": "Hizli yazilimci"}

# Yeni POST kapımız burası
@app.post("/selamla")
def selamla(kisi: Kullanici):
    return {"mesaj": f"Selam {kisi.isim}, {kisi.yas} yasindasin ve backend canavarısın!"}
