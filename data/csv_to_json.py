import pandas as pd

# Load the CSV file
csv_file_path = 'response.csv'
df = pd.read_csv(csv_file_path)
id = 0
def transform_row(row):
    global id
    id += 1
    transformed = {
        "id": id,
        "Answer 1": row["1. What is your age?"], 
        "Answer 2": row["2. Which of the following describe you, if any? "],   
        "Answer 3": row["3. Are you of Hispanic/Latino/Spanish origin ?"],
        "Answer 4": row["4. How would you best describe yourself?"] ,  
        "Answer 5": row["5. Which of the following best describes the highest level of formal education that you’ve completed or currently undergoing?"], # Replace
        "Answer 6": row["6. How many years of professional coding experience do you have ?"],
        "Answer 7": row['7. What is you preferred development environment?'],
        "Answer 8": row["8. How do you learn to code?"],
        "Answer 9": row["9. What is the biggest challenge you face as a developer?"],
        "Answer 10": row["10. When choosing a programming language for a new project, you prioritize:"],
        "Answer 11": row["11. How do you communicate effectively with teammates to collaborate while adhering to the timelines?"],
        "Answer 12": row["12. How do you ensure that you stay up-to-date with industry changes as a software developer?"],
        "Answer 13": row["13. How do you balance between innovation and meeting project deadlines?"],
        "Answer 14": row["14. Software development contributes to societal challenges by:"],
        "Answer 15": row["15. A company uses an AI system to monitor its employees' productivity. The AI suggests firing an employee based on low productivity, but the employee is going through a tough personal time. How should the company proceed?"],
        "Answer 16": row["16. You're assigned to a project that requires expertise in a programming language you're not familiar with. The deadline is tight. What is your strategy to tackle this situation? "],
        "Answer 17": row["17. You discover a critical bug right before a software release. What immediate action do you take?"],
        "Answer 18": row["18. In a professional setting, if your team is supposed to deliver a SaaS product within a two-day timeframe, and you discover a critical bug in the software, how would you address and handle this situation?"],
    }
    return transformed

transformed_data = df.apply(transform_row, axis=1)

json_data = transformed_data.to_json(orient='records')

output_json_path = 'response.json'
with open(output_json_path, 'w') as json_file:
    json_file.write(json_data)

