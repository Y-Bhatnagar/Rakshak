from backend.state import metaDataHist
from backend.rakshak import payload
from utility.model import K2_metadata
from typing import List

sessionID= payload.sessionId
metaList: List[K2_metadata] = metaDataHist[sessionID]
total_replies = len(metaList) + 1

for meta in reversed(metaList):
    if meta.new_info_detected is True:
        rep_number = meta.reply_number
        break

messages_since_last_intel = total_replies - rep_number