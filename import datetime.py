import datetime # This module provides classes for manipulating dates and times

print("Welcome to the Habit Tracker!") 
print("This program helps you track your daily habits.")
class HabitTracker: # This class is used to track habits
    # It contains methods to add, mark, view, remove, edit, clear, and search habits
    # It uses a dictionary to store habits and their corresponding dates
    def __init__(self): # This method initializes the HabitTracker class
        self.habits = {}

    def add_habit(self, habit_name): # This code adds a new habit to the list
        if habit_name not in self.habits:
            self.habits[habit_name] = []
            print(f"Habit '{habit_name}' added.")
        else:
            print(f"Habit '{habit_name}' already exists.")

    def mark_habit(self, habit_name): # This code marks a habit as completed for today
        if habit_name in self.habits:
            today = datetime.date.today()
            if today not in self.habits[habit_name]:
                self.habits[habit_name].append(today)
                print(f"Habit '{habit_name}' marked for today.")
            else:
                print(f"Habit '{habit_name}' is already marked for today.")
        else:
            print(f"Habit '{habit_name}' does not exist.")
    def remove_habit(self, habit_name): # This code removes a habit from the list
        if habit_name in self.habits:
            del self.habits[habit_name]
            print(f"Habit '{habit_name}' removed.")
        else:
            print(f"Habit '{habit_name}' does not exist.")
    def edit_habit(self, old_name, new_name): # This code edits the name of an existing habit
        if old_name in self.habits:
            if new_name not in self.habits:
                self.habits[new_name] = self.habits.pop(old_name)
                print(f"Habit '{old_name}' renamed to '{new_name}'.")
            else:
                print(f"Habit '{new_name}' already exists.")
        else:
            print(f"Habit '{old_name}' does not exist.")
    def clear_habits(self): # This code clears all habits from the list
        self.habits.clear()
        print("All habits cleared.")
    def search_habit(self, habit_name): # This code searches for a specific habit in the list of habits
        if habit_name in self.habits:
            print(f"Habit '{habit_name}' found.")
        else:
            print(f"Habit '{habit_name}' not found.")     
    def view_habits(self): # This code displays all the habits and their corresponding dates
        if not self.habits:
            print("No habits to track.")
        else:
            for habit, dates in self.habits.items():
                print(f"Habit: {habit}")
                print(f"Dates: {', '.join(str(date) for date in dates)}")

if __name__ == "__main__": # This block of code is executed when the script is run directly
    # It creates an instance of the HabitTracker class and provides a menu for the user to interact with
    tracker = HabitTracker()

    while True: # This loop continues until the user chooses to exit 
        print("\nHabit Tracker Menu:")
        print("1. Add Habit")
        print("2. Mark Habit")
        print("3. View Habits")
        print("4. Remove Habit")
        print("5. Edit Habit")
        print("6. Clear All Habits")
        print("7. Search Habit")
        print("8. Exit")
        choice = input("Choose an option: ")

        if choice == "1": # Add Habit
            habit_name = input("Enter the habit name: ")
            tracker.add_habit(habit_name)
        elif choice == "2": # Mark Habit
            habit_name = input("Enter the habit name to mark: ")
            tracker.mark_habit(habit_name)
        elif choice == "3": # View Habits
            tracker.view_habits()
        elif choice == "4": # Remove Habit
            habit_name = input("Enter the habit name to remove: ")
            tracker.remove_habit(habit_name)
        elif choice == "5": # Edit Habit
            old_name = input("Enter the old habit name: ")
            new_name = input("Enter the new habit name: ")
            tracker.edit_habit(old_name, new_name)
        elif choice == "6": # Clear All Habits
            tracker.clear_habits()
        elif choice == "7": # Search Habit
            habit_name = input("Enter the habit name to search: ")
            tracker.search_habit(habit_name)
        elif choice == "8": # Exit
            print("Exiting Habit Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")