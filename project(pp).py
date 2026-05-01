import random
class WorkoutGenerator:
    def __init__(self):
        self.cardio = ["Jumping Jacks", "Running", "Cycling", "Burpees"]
        self.strength = ["Push-ups", "Squats", "Lunges", "Bench Press"]
        self.flexibility = ["Yoga", "Stretching", "Toe Touch", "Child Pose"]
        self.core = ["Plank", "Crunches", "Leg Raises", "Russian Twists"]

    def generate_workout(self):
        return {
            "Cardio": random.choice(self.cardio),
            "Strength": random.choice(self.strength),
            "Flexibility": random.choice(self.flexibility),
            "Core": random.choice(self.core)
        }

    def display_workout(self, workout):
        print("\n Daily Workout Plan\n")
        for category, exercise in workout.items():
            print(f"{category}: {exercise}")
            
def main():
    generator = WorkoutGenerator()
    
    while True:
        print("\n Random Workout Generator")
        print("1. Generate Workout")
        print("2. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            workout = generator.generate_workout()
            generator.display_workout(workout)
        elif choice == "2":
            print("Stay Fit! ")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()


    
