from system.database import engine, fancy_table
from sqlalchemy import insert, select

def set_fancy(user_id, username, prefix, suffix, fancy_name):
    with engine.begin() as conn:
        stmt = insert(fancy_table).values(user_id=user_id, username=username, prefix=prefix, suffix=suffix, fancy_name=fancy_name)
        # use replace behavior
        conn.execute(stmt)

def get_fancy_for_user(user_id):
    with engine.connect() as conn:
        stmt = select(fancy_table.c.fancy_name).where(fancy_table.c.user_id==user_id)
        r = conn.execute(stmt).fetchone()
        return r[0] if r else None
