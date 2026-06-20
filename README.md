# Persona-Aware AI Support Agent

An intelligent customer support assistant that combines Persona Classification, Retrieval-Augmented Generation (RAG), and Gemini AI to deliver personalized support responses based on the user's communication style and intent.

## Features

* Customer Persona Classification

  * Technical Expert
  * Frustrated User
  * Business Executive

* Retrieval-Augmented Generation (RAG)

  * Retrieves relevant knowledge base documents
  * Uses semantic search for contextual responses

* Adaptive Response Generation

  * Technical responses for experts
  * Empathetic responses for frustrated users
  * Concise business-focused responses for executives

* Confidence-Based Escalation

  * Automatically escalates low-confidence queries
  * Generates structured handoff summaries for human agents

* Interactive Web Interface

  * Built using Streamlit
  * Easy-to-use customer support dashboard

## Tech Stack

* Python
* Gemini AI
* Streamlit
* ChromaDB
* LangChain
* RAG (Retrieval-Augmented Generation)
* Git & GitHub

## Project Structure

persona-support-agent/

├── data/

├── src/

│ ├── classifier.py

│ ├── rag_pipeline.py

│ ├── generator.py

│ ├── escalator.py

│ └── utils.py

├── app.py

├── requirements.txt

└── README.md

## Workflow

User Query
↓
Persona Classification
↓
Knowledge Retrieval (RAG)
↓
Adaptive Response Generation
↓
Confidence Evaluation
↓
Human Escalation (if required)

## Installation

```bash
git clone https://github.com/yourusername/persona-support-agent.git

cd persona-support-agent

pip install -r requirements.txt
```

Create a .env file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

## Example Use Cases

* API Authentication Issues
* Password Recovery Support
* Billing and Subscription Queries
* Customer Escalation Workflows
* Enterprise Support Automation

## Future Enhancements

* Multi-language support
* Voice-enabled customer assistance
* Advanced analytics dashboard
* Integration with CRM platforms
* Fine-tuned support models

## Author

V Anil Kumar

GitHub: https://github.com/vanilkumar01

LinkedIn: https://www.linkedin.com/in/v-anil-kumar-/
