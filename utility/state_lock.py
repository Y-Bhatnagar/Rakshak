import asyncio

lock: dict[str, asyncio.Lock] = {}

def get_lock(session_id:str):
    if session_id not in lock:
        lock[session_id] = asyncio.Lock()
    return lock[session_id]