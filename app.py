import streamlit as st
import os
from src.classifier import classify_customer_persona
from src.rag_pipeline import LocalRAGPipeline
from src.generator import generate_adaptive_response


def load_documents():

    rag = LocalRAGPipeline()

    for file in os.listdir("data"):

        if file.endswith(".txt") or file.endswith(".md"):

            with open(
                os.path.join("data", file),
                "r",
                encoding="utf-8"
            ) as f:

                rag.ingest_document(
                    file,
                    f.read()
                )

    return rag

st.title("Persona Support Agent")

user_query = st.text_area(
"Enter customer message"
)

if st.button("Submit"):
    persona_result = classify_customer_persona(
        user_query
    )

    rag = load_documents()

    context = rag.retrieve_context(
        user_query
    )

    result = generate_adaptive_response(
        user_query=user_query,
        persona=persona_result["persona"],
        context_chunks=context
    )

    st.subheader("Detected Persona")
    st.write(persona_result)

    st.subheader("Response")
    st.write(result["response"])

    if result["escalated"]:
        st.error("Escalated to Human Support")
        st.code(result["handoff_summary"])

