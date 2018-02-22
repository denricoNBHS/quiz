# Complete each task listed below and then push your solutions to your github repository.

# 1.  Import the module called school
import school

# 2. Use list indexing to store the last element of schedule as last_period
schedule = ["Algebra", "Physics", "Study Hall", "English", "Arabic", "Lunch", "World History", "Physical Education"]
last_period = schedule[-1]

# 3. Use a list slice to store a list of the classes before lunch. Give this slice the name pre_lunch  
pre_lunch = schedule[:5]

# If we want to make this work for any schedule, we can do this instead of counting the periods and hard-coding the index.
pre_lunch2 = schedule[:schedule.index("Lunch")]


# 4. Use a list comprehension to generate a list of all courses in the schedule starting with the letter 'A'
#    and call it a_courses
a_courses = [cls for cls in schedule if cls[0] == "A"]

# 5. The print_schedule function in the school module you imported earlier has two formal parameters:
# a name (string) and a schedule (list). You may look at the function in school.py if you'd like.
# Call the print_schedule function school.print_schedule, giving it your name and the schedule you generated earlier.
# Write the output of the function to the file "my_schedule.txt"
with open("my_schedule.txt", "w") as f:
    f.write(school.print_schedule("Mr. Enrico", schedule))




