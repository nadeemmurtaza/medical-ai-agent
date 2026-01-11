import time

# --- Configuration ---
# This System Prompt tells the LLM exactly how to behave.
# It prevents the AI from "hallucinating" fake medical facts.
SYSTEM_PROMPT = """
ROLE: You are an expert Medical Scribe.
TASK: specific raw patient text into a standard SOAP Note format.
RULES: 
1. Do not invent symptoms not mentioned.
2. Use professional medical terminology (e.g., replace "belly hurt" with "Abdominal Pain").
3. Flag any "Red Flag" symptoms (Chest pain, Shortness of breath) immediately.
"""

def mock_llm_processing(text_input):
    """
    Simulates sending data to OpenAI/GPT-4 for processing.
    In a real production environment, this would call: openai.ChatCompletion.create()
    """
    print(f"🔄 Connecting to AI Model with input: '{text_input[:20]}...'")
    time.sleep(1.5) # Simulate network latency
    
    # Mock Response (This is what the AI would generate)
    return {
        "Subjective": f"Patient reports: {text_input}. Onset: Sudden. Severity: Moderate.",
        "Objective": "Vitals: Stable (assumed). Physical Exam: Deferred.",
        "Assessment": "Symptom etiology to be determined.",
        "Plan": "1. Monitor vitals. 2. Consider CBC/CMP panel. 3. Follow up in 24h."
    }

# --- Main Application Workflow ---
if __name__ == "__main__":
    # 1. Doctor dictates raw notes
    doctor_dictation = "Patient complains of sharp pain in the lower right abdomen since this morning. Feels nauseous but no vomiting."
    
    # 2. AI Processes the text
    print("--- STARTING AI SCRIBE ---")
    soap_note = mock_llm_processing(doctor_dictation)
    
    # 3. Output Structured Data
    print("\n--- GENERATED SOAP NOTE ---")
    for section, content in soap_note.items():
        print(f"[{section}]: {content}")
      
