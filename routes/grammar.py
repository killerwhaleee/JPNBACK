from fastapi import APIRouter
from services.grammar_service import get_grammar_details, analyze_sentence
from models import SentenceRequest
from fastapi import HTTPException


router = APIRouter()


@router.get("/grammar/{grammar_id}")
def get_grammar(grammar_id: int):
    """获取某个语法点的详细信息"""
    return get_grammar_details(grammar_id)


@router.post("/grammar/analyze")
def analyze_grammar(request: SentenceRequest):
    """分析语法结构"""
    if not request.sentence:
        raise HTTPException(status_code=400, detail="Sentence cannot be empty")

    try:
        return analyze_sentence(request.sentence)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error analyzing sentence: {str(e)}"
        )
