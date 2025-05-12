from fastapi import FastAPI
from controller import items, users, gachareview, gacha, gachadraw, delivery

app = FastAPI()

app.include_router(items.router)
app.include_router(users.router)
app.include_router(gachareview.router)
app.include_router(gacha.router)
app.include_router(gachadraw.router)
app.include_router(delivery.router)
