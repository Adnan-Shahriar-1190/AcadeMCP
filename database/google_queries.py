from shared.db import pool
import json

from shared.db import pool

async def load_token_from_db():
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                """SELECT token FROM google_tokens LIMIT 1"""
            )
            row = await cur.fetchone()
            
            if row is None:
                return None

            return row[0]

async def save_token_to_db(token_data: dict):
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                """SELECT id FROM google_tokens LIMIT 1"""
            )
            existing = await cur.fetchone()

            if existing:
                await cur.execute(
                    """
                    UPDATE google_tokens SET token=%s, updated_at=NOW() WHERE id=%s
                    """,
                    (json.dumps(token_data), existing[0])
                )
            else:
                await cur.execute(
                    """
                    INSERT INTO google_tokens(token)
                    VALUES(%s)
                    """,
                    (json.dumps(token_data),)
                )