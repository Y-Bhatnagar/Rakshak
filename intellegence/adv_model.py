from intellegence.model import Kimi_K2_model
from intellegence.system_prompts import K2_prompt
from utility.model import K2_reply

#binding K2 with structure
stu_K2 = Kimi_K2_model.with_structured_output(K2_reply)
#chaining prompt and structured model
ai = K2_prompt | stu_K2