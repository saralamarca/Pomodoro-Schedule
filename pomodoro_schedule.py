"""
This is a simple Pomodoro Planner that helps you to plan your day.
"""
import datetime


class PomodoroSchedule():
    def __init__(self, num_pomodoros):
        # Constants for pomodoro times
        self.POMODORO_TIME = datetime.timedelta(minutes=25)
        self.SHORT_BREAK = datetime.timedelta(minutes=5)
        self.LONG_BREAK = datetime.timedelta(minutes=15)
        self.LONGER_BREAK = datetime.timedelta(minutes=30)

        self.num_pomodoros = num_pomodoros
    
        # Get the current time
        self.current_time = datetime.datetime.now()

        # Print initial time
        print(f"Schedule starting at: {self.current_time.strftime('%H:%M')}")

    def calculate_break_time(self, pomodoro_count):
        """
        Method to manage the break time between pomodoros.
        Between each 25 min focus period, take a 5 min break.
        After 4 pomodoros, take a 15 min break.
        After 6 pomodoros, take a 30 min break.
        """
        if pomodoro_count % 6 == 0:
            return self.LONGER_BREAK
        elif pomodoro_count % 4 == 0:
            return self.LONG_BREAK
        else:
            return self.SHORT_BREAK


    def print_schedule(self):
        """
        Method to print the schedule.
        """
        for i in range(1, self.num_pomodoros + 1):
            start_time = self.current_time
            end_time = start_time + self.POMODORO_TIME
            print(f"{start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')} Focus minutes")

            self.current_time = end_time
            if i < self.num_pomodoros:
                break_time = self.calculate_break_time(i)
                self.current_time += break_time
                print(f"{end_time.strftime('%H:%M')} - {self.current_time.strftime('%H:%M')} Break")



if __name__ == "__main__":
    print("\n** Welcome to the pomodoro technique schedule planner **\n")
    num_pomodoros = int(input("How many pomodoros (25-min focus periods) do you need? "))
    pomodoro_schedule = PomodoroSchedule(num_pomodoros)
    pomodoro_schedule.print_schedule()