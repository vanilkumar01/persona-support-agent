import json

def generate_handoff_summary(user_query: str, persona: str, context_chunks: list) -> str:
    """Compiles detailed, structured JSON handoff data for an escalating support ticket."""
    handoff_data = {
        "persona": persona,
        "detected_issue": user_query[:100] + "...",
        "retrieved_sources": [c["source"] for c in context_chunks],
        "confidence_score": max([c["score"] for c in context_chunks]) if context_chunks else 0.0,
        "recommended_action": "Review system error codes, check API logs, and contact user directly."
    }
    return json.dumps(handoff_data, indent=2)

