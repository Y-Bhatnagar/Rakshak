from backend.state import metaDataHist
from backend.rakshak import payload
from utility.model import K2_metadata
from typing import List

def msg_count(sessionID: str) -> int:
    if sessionID not in metaDataHist:
        return 0
    else:
        metaList: List[K2_metadata] = metaDataHist[sessionID]
        total_replies = len(metaList)+1 #as the current AI Message by K2 is not yet in the metaDataHist
        rep_number = 0

        for meta in reversed(metaList):
            if meta.new_info_detected is True:
                rep_number = meta.reply_number
                break
        
        messages_since_last_intel = total_replies - rep_number
    return  messages_since_last_intel