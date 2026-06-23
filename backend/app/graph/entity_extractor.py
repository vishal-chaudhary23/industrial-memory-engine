import os
import json

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from app.services.llm import llm

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

prompt = ChatPromptTemplate.from_template("""
You are an Industrial Knowledge Graph Extraction System.

Extract entities and relationships from the industrial document text.

Rules:
- Return ONLY valid JSON.
- Do not add explanations or markdown.
- Do not invent information.
- Use exact names from the text whenever possible.
- If no entities or relationships exist, return empty arrays.

Entity Types:
- equipment: pumps, valves, motors, compressors, sensors, PLCs, pipelines, tanks, equipment tags (e.g., P-101, V-201)
- person: engineers, operators, inspectors, managers
- standard: ISO, OSHA, API, ASME, IEC, regulatory references
- document: SOPs, manuals, work orders, inspection reports, audit reports, permits
- incident: failures, leaks, shutdowns, overheating, accidents, faults
- parameter: pressure, temperature, flow rate, vibration, RPM, voltage, current
- location: plant areas, units, production lines, stations

Relationship Types:
- INSPECTED
- OPERATED
- REPORTED
- CAUSED
- FAILED_DUE_TO
- LOCATED_IN
- COMPLIES_WITH
- REFERENCES
- MAINTAINED_BY
- RELATED_TO

Text:
{text}

Output Schema:

{{
  "entities": [
    {{
      "name": "",
      "type": ""
    }}
  ],
  "relationships": [
    {{
      "source": "",
      "relation": "",
      "target": ""
    }}
  ]
}}
""")