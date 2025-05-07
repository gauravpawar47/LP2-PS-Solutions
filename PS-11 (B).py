class EmployeePerformanceEvaluation:
    def __init__(self):
        # In-depth performance evaluation categories
        self.performance_criteria = {
            'productivity': {
                'low': 'The employee has not met the expected level of output. This could be due to a lack of focus or insufficient resources.',
                'average': 'The employee meets the basic productivity requirements but has room for improvement in efficiency and time management.',
                'high': 'The employee exceeds expectations in terms of productivity, consistently delivering high-quality work in a timely manner.'
            },
            'teamwork': {
                'poor': 'The employee struggles with collaboration, may not communicate effectively with the team, or may have issues with conflict resolution.',
                'good': 'The employee works well with others and is a reliable team member, though there might be occasional miscommunication or lack of engagement.',
                'excellent': 'The employee is an exceptional team player, often taking the initiative to help others, foster collaboration, and contribute to a positive team dynamic.'
            },
            'communication': {
                'poor': 'The employee has difficulty expressing thoughts clearly and does not communicate effectively with colleagues or supervisors.',
                'good': 'The employee communicates clearly in most situations but could work on providing more details or being more proactive in communication.',
                'excellent': 'The employee excels in communication, providing clear, concise, and timely information to everyone involved.'
            }
        }

    def evaluate(self, criteria):
        print("\nEvaluating employee performance...\n")
        evaluation_result = {}
        for key, value in criteria.items():
            if value in self.performance_criteria[key]:
                evaluation_result[key] = self.performance_criteria[key][value]
            else:
                evaluation_result[key] = "Invalid rating. Please provide 'low', 'average', or 'high' for productivity and 'poor', 'good', or 'excellent' for teamwork and communication."
        return evaluation_result

    def provide_feedback(self, evaluation_result):
        print("\nDetailed Feedback:\n")
        for category, feedback in evaluation_result.items():
            print(f"{category.capitalize()}: {feedback}")
            print("-" * 50)

# Example usage
def performance_evaluation():
    print("Welcome to the Employee Performance Evaluation System\n")
    expert_system = EmployeePerformanceEvaluation()
    
    criteria = {
        'productivity': input("Enter productivity rating (low, average, high): ").lower(),
        'teamwork': input("Enter teamwork rating (poor, good, excellent): ").lower(),
        'communication': input("Enter communication rating (poor, good, excellent): ").lower(),
    }
    
    evaluation = expert_system.evaluate(criteria)
    expert_system.provide_feedback(evaluation)

performance_evaluation()
