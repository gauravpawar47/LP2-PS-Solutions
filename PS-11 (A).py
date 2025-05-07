class MedicalExpertSystem:
    def __init__(self):
        # Symptom-based rules with possible diagnosis and recommendations
        self.symptom_rules = {
            'fever': {
                'diagnosis': 'You might have an infection or an inflammatory condition.',
                'suggestions': 'Consider getting a blood test and consulting with a doctor to identify the cause of the fever.'
            },
            'headache': {
                'diagnosis': 'Headaches could indicate stress, dehydration, or even a migraine.',
                'suggestions': 'Make sure you are well-hydrated and consider taking a mild pain reliever. If the headache persists, see a doctor.'
            },
            'cough': {
                'diagnosis': 'A cough can be caused by a variety of issues like respiratory infections, allergies, or asthma.',
                'suggestions': 'If the cough persists for more than 3 days, or if you experience difficulty breathing, seek medical advice.'
            },
            'fatigue': {
                'diagnosis': 'Fatigue might indicate an underlying infection, poor sleep, or a chronic condition.',
                'suggestions': 'Try improving your sleep hygiene and diet. If fatigue continues, a blood test may help diagnose any underlying issues.'
            },
            'chest pain': {
                'diagnosis': 'Chest pain is a critical symptom that could be a sign of a heart attack, pulmonary issues, or even severe stress.',
                'suggestions': 'Seek immediate medical help. Do not ignore chest pain as it could be life-threatening.'
            }
        }

    def diagnose(self, symptoms):
        print("\nDiagnosing based on your symptoms...\n")
        diagnosis = []
        for symptom in symptoms:
            symptom = symptom.strip().lower()
            if symptom in self.symptom_rules:
                diagnosis.append({
                    'symptom': symptom,
                    'diagnosis': self.symptom_rules[symptom]['diagnosis'],
                    'suggestions': self.symptom_rules[symptom]['suggestions']
                })
            else:
                diagnosis.append({
                    'symptom': symptom,
                    'diagnosis': f"Symptom '{symptom}' is not recognized in the system.",
                    'suggestions': "Please consult a healthcare provider for a professional diagnosis."
                })
        return diagnosis

    def display_diagnosis(self, diagnosis):
        print("\nDiagnosis Results:\n")
        for result in diagnosis:
            print(f"Symptom: {result['symptom'].capitalize()}")
            print(f"Diagnosis: {result['diagnosis']}")
            print(f"Suggestions: {result['suggestions']}")
            print("-" * 50)

# Example usage
def medical_system():
    print("Welcome to the Medical Expert System\n")
    expert_system = MedicalExpertSystem()
    symptoms = input("Enter symptoms separated by commas (e.g., fever, cough): ").split(",")
    diagnosis = expert_system.diagnose(symptoms)
    expert_system.display_diagnosis(diagnosis)

medical_system()
