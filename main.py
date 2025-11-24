from fastapi import FastAPI, Header, HTTPException
from config import ADMIN_DASH_TOKEN
from system.database import engine, fancy_table
from sqlalchemy import select

app = FastAPI(title='MelodyX Admin')

def check_token(token: str):
    return token == ADMIN_DASH_TOKEN

@app.get('/health')
async def health():
    return {'status':'ok'}

@app.get('/fancy_names')
async def get_fancy_names(x_token: str = Header(None)):
    if not check_token(x_token):
        raise HTTPException(status_code=401, detail='Unauthorized')
    with engine.connect() as conn:
        stmt = select(fancy_table.c.user_id, fancy_table.c.username, fancy_table.c.fancy_name)
        rows = conn.execute(stmt).fetchall()
        return [{'user_id':r[0], 'username':r[1], 'fancy_name':r[2]} for r in rows]
