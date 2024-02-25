questions = [
    "What is your age?",
    "Which of the following describe you, if any?",
    "Are you of Hispanic/Latino/Spanish origin?",
    "How would you best describe yourself?",
    "Which of the following best describes the highest level of formal education that you’ve completed or currently undergoing?",
    "How many years of professional coding experience do you have?",
    "What is your preferred development environment?",
    "How do you learn to code?",
    "What is the biggest challenge you face as a developer?",
    "When choosing a programming language for a new project, you prioritize:",
    "How do you communicate effectively with teammates to collaborate while adhering to the timelines?",
    "How do you ensure that you stay up-to-date with industry changes as a software developer?",
    "How do you balance between innovation and meeting project deadlines?",
    "Software development contributes to societal challenges by:",
    "A company uses an AI system to monitor its employees' productivity. The AI suggests firing an employee based on low productivity, but the employee is going through a tough personal time. How should the company proceed?",
    "You're assigned to a project that requires expertise in a programming language you're not familiar with. The deadline is tight. What is your strategy to tackle this situation?",
    "You discover a critical bug right before a software release. What immediate action do you take?",
    "In a professional setting, if your team is supposed to deliver a SaaS product within a two-day timeframe, and you discover a critical bug in the software, how would you address and handle this situation?"
]


import json 
json_data = {f"question {i+1}": question for i, question in enumerate(questions)}

output_json_path = 'form.json'
with open(output_json_path, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)