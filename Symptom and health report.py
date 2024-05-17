import tkinter as tk
from datetime import datetime
import csv
import threading

def record_symptoms(symptoms):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('symptoms.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp] + symptoms)
    print("Symptoms recorded successfully.")

def record_health_metrics(heart_rate, blood_pressure, blood_oxygen):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('health_metrics.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, heart_rate, blood_pressure, blood_oxygen])
    print("Health metrics recorded successfully.")

def submit_symptoms():
    symptoms = entry_symptoms.get().split(',')  # Assuming symptoms are entered as comma-separated values
    record_symptoms(symptoms)
    label_feedback_symptoms.config(text="Symptoms recorded successfully.")

def submit_health_metrics():
    heart_rate = entry_heart_rate.get()
    blood_pressure = entry_blood_pressure.get()
    blood_oxygen = entry_blood_oxygen.get()
    record_health_metrics(heart_rate, blood_pressure, blood_oxygen)
    label_feedback_metrics.config(text="Health metrics recorded successfully.")

def scheduled_reminder():
    threading.Timer(24 * 3600, scheduled_reminder).start()  # Remind every 24 hours
    print("Reminder: Don't forget to record your symptoms and health metrics!")

def create_health_report():
    report = "Health Report\n"
    report += "Date: {}\n\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    # Read symptoms
    report += "Recorded Symptoms:\n"
    try:
        with open('symptoms.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                report += ", ".join(row) + "\n"
    except FileNotFoundError:
        report += "No symptoms recorded yet.\n"

    # Read health metrics
    report += "\nRecorded Health Metrics:\n"
    try:
        with open('health_metrics.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                report += ", ".join(row) + "\n"
    except FileNotFoundError:
        report += "No health metrics recorded yet.\n"

    with open('health_report.txt', 'w') as file:
        file.write(report)
    label_feedback_report.config(text="Health report created successfully.")
    print("Health report created successfully.")

# Create GUI window
window = tk.Tk()
window.title("Health Buddy - Symptom Tracker")

# Create input field for symptoms
label_symptoms = tk.Label(window, text="Enter symptoms (comma-separated):")
label_symptoms.pack()
entry_symptoms = tk.Entry(window)
entry_symptoms.pack()

# Create submit button for symptoms
button_submit_symptoms = tk.Button(window, text="Submit Symptoms", command=submit_symptoms)
button_submit_symptoms.pack()

# Create feedback label for symptoms
label_feedback_symptoms = tk.Label(window, text="")
label_feedback_symptoms.pack()

# Create input fields for health metrics
label_heart_rate = tk.Label(window, text="Enter heart rate:")
label_heart_rate.pack()
entry_heart_rate = tk.Entry(window)
entry_heart_rate.pack()

label_blood_pressure = tk.Label(window, text="Enter blood pressure (e.g., 120/80):")
label_blood_pressure.pack()
entry_blood_pressure = tk.Entry(window)
entry_blood_pressure.pack()

label_blood_oxygen = tk.Label(window, text="Enter blood oxygen level (%):")
label_blood_oxygen.pack()
entry_blood_oxygen = tk.Entry(window)
entry_blood_oxygen.pack()

# Create submit button for health metrics
button_submit_metrics = tk.Button(window, text="Submit Health Metrics", command=submit_health_metrics)
button_submit_metrics.pack()

# Create feedback label for health metrics
label_feedback_metrics = tk.Label(window, text="")
label_feedback_metrics.pack()

# Create button to generate health report
button_generate_report = tk.Button(window, text="Generate Health Report", command=create_health_report)
button_generate_report.pack()

# Create feedback label for health report
label_feedback_report = tk.Label(window, text="")
label_feedback_report.pack()

# Start scheduled reminders
scheduled_reminder()

# Start GUI event loop
window.mainloop()
