import sqlite3
import os
from pathlib import Path
from datetime import datetime, timezone

DATA = Path(os.getenv("BRANDPILOT_DATA_DIR", ".brandpilot_data"))
DATA.mkdir(parents=True, exist_ok=True)

DB_PATH = DATA / "audit.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS audit_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                review_id TEXT NOT NULL,
                reviewer TEXT NOT NULL,
                role TEXT NOT NULL,
                action TEXT NOT NULL,
                decision TEXT,
                comment TEXT,
                timestamp TEXT NOT NULL
            )
        """)


def log_event(review_id, reviewer, role, action, decision="", comment=""):
    timestamp = datetime.now(timezone.utc).isoformat()

    with get_connection() as conn:
        conn.execute("""
            INSERT INTO audit_logs
            (review_id, reviewer, role, action, decision, comment, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            review_id, reviewer, role, action,
            decision, comment, timestamp
        ))


def get_audit_logs(limit=100):
    with get_connection() as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("""
            SELECT * FROM audit_logs
            ORDER BY id DESC
            LIMIT ?
        """, (limit,)).fetchall()

        return [dict(row) for row in rows]