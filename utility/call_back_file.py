import httpx
import logging

GUVI_CALLBACK_URL = "https://hackathon.guvi.in/api/updateHoneyPotFinalResult"

async def send_guvi_callback(final_call_obj) -> bool:
    try:
        payload_dict = final_call_obj.model_dump()
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.post(
                GUVI_CALLBACK_URL,
                json=payload_dict,
                headers={"Content-Type": "application/json"}
            )

            response.raise_for_status()
            logging.info("GUVI final callback sent successfully")
            return True
    except Exception as e:
        logging.error(f"GUVI callback failed: {e}")
        return False