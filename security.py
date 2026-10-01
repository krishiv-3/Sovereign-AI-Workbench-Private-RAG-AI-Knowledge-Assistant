import re


JAILBREAK_PATTERNS = [
    r"ignore (all |the |your )?(previous|prior|earlier) instructions",
    r"ignore (all |the )?instructions",
    r"forget (all |your )?instructions",
    r"disregard (all |the )?instructions",
    r"override (your |the )?instructions",
    r"ignore the documents",
    r"use your own knowledge",
    r"answer from your own knowledge",
    r"reveal (your |the )?(system|hidden) prompt",
    r"show (me )?(your |the )?(system|hidden) prompt",
    r"what is your system prompt",
    r"bypass (your |the )?(rules|restrictions|instructions)",
    r"act as an unrestricted",
    r"jailbreak",
]


def detect_jailbreak(question):

    question_lower = question.lower()

    for pattern in JAILBREAK_PATTERNS:

        if re.search(pattern, question_lower):
            return True

    return False