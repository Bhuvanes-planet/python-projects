def symptom_checker():
    print("=== Basic Symptom Checker ===")
    print("Answer with yes or no\n")

    fever = input("Do you have fever? ").lower()
    cold = input("Do you have cold/runny nose? ").lower()
    cough = input("Do you have cough? ").lower()
    stomach_pain = input("Do you have stomach pain? ").lower()
    headache = input("Do you have headache? ").lower()
    body_pain = input("Do you have body pain? ").lower()

    print("\nPossible Result:")

    if fever == "yes" and cold == "yes" and cough == "yes":
        print("- Symptoms may be consistent with a common cold, flu, or another respiratory infection.")

    elif fever == "yes" and body_pain == "yes":
        print("- Symptoms may be consistent with a viral infection.")

    elif stomach_pain == "yes" and fever == "yes":
        print("- Stomach pain with fever can have several causes and may need medical evaluation.")

    elif headache == "yes" and fever == "yes":
        print("- Fever with headache can occur in various infections.")

    elif body_pain == "yes":
        print("- General body pain can result from strain, fatigue, or illness.")

    else:
        print("- No clear pattern detected.")

    print("\nThis is not a medical diagnosis.")
    print("Consult a qualified healthcare professional for medical advice.")

symptom_checker()
