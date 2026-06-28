from shared.db import pool
import json

async def load_token_from_db() -> dict | None:
    row = await pool.fetchrow("SELECT token FROM google_tokens LIMIT 1")
    return row["token"] if row else None

async def save_token_to_db(token_data: dict):
    async with pool.connection() as conn:
        existing = await conn.fetchrow("SELECT id FROM google_tokens LIMIT 1")
        if existing:
            await conn.execute(
                "UPDATE google_tokens SET token = $1, updated_at = NOW() WHERE id = $2",
                json.dumps(token_data), existing["id"]
            )
        else:
            await conn.execute(
                "INSERT INTO google_tokens (token) VALUES ($1)",
                json.dumps(token_data)
            )