"""
Culture Protocol Engine
"""

__version__ = "0.1.0"
__description__ = "Transform AI cognition through the power of culture"

from .models import (
    CultureProtocol,
    ValueToken,
    Meme,
    Practice,
    Myth
)

from .services import (
    CultureProtocolComposer,
    CultureEvaluationEngine,
    culture_composer,
    culture_evaluator
)

__all__ = [
    "CultureProtocol",
    "ValueToken",
    "Meme", 
    "Practice",
    "Myth",
    "CultureProtocolComposer",
    "CultureEvaluationEngine",
    "culture_composer",
    "culture_evaluator"
]