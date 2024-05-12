import re
from typing import List


def tokenize(text: str) -> List[str]:
    return [
        token.lower().replace("’", "'")
        for token in re.findall(r"\b\w+?\b(?:'|’)?", text)
    ]
