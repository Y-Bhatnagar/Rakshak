from backend.state import metaDataHist
from utility.model import K2_metadata
from typing import List

def msg_count(sessionID: str) -> int:
    if sessionID not in metaDataHist:
        return 0

    metaList = metaDataHist[sessionID]
    total_replies = len(metaList)

    last_intel = 0
    for m in reversed(metaList):
        if m.new_info_detected and len(m.new_info_detected) > 0:
            last_intel = m.reply_number
            break

    return total_replies - last_intel