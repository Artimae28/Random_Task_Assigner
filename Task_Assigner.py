import random
#Define our task assigning function
def task_picker():
  FiveCrew_tasks = ["Task_1", "Task_2", "Task_3", "Task_4", "Task_5"] #List the usual task for a standard 5-employee shift
  FourCrew_tasks = ["Task_1", "Task_2", "Task_3", "Task_4"] #List the tasks for a 4-employee shift
  Mon_staff = ["Employee_1", "Employee_2", "Employee_3", "Employee_4"] #Monday night staff, 4-employee example
  Tue_staff = ["Employee_1", "Employee_2", "Employee_3", "Employee_4", "Employee_5"] #Tuesday night staff, 5-employee example
  Wed_staff = ["Employee_1", "Employee_2", "Employee_3", "Employee_4", "Employee_5"] #Wednesday night staff
  Thur_staff = ["Employee_1", "Employee_2", "Employee_3", "Employee_4", "Employee_5"] #Thursday night staff 
  Fri_staff = ["Employee_1", "Employee_2", "Employee_3", "Employee_4"] #Friday night staff
  Sat_staff = ["Employee_1", "Employee_2", "Employee_3", "Employee_4"] #Saturday night staff
  Sun_staff = ["Employee_1", "Employee_2", "Employee_3", "Employee_4"] #Sunday night staff
  #Note: If you have a Monday-to-Friday job with regular staff, replace day staff list with just one staff list
  #Now we have to randomize our tasks to keep things fair
  random.shuffle(FiveCrew_tasks)
  random.shuffle(FourCrew_tasks)
  #Create an input to ask user what day it is
  day_of_week = input("What day of the week is it? ")
  if day_of_week.lower() == "monday":
    print(f"{Mon_staff[0]}\n{FourCrew_tasks[0]}\n")
    print(f"{Mon_staff[1]}\n{FourCrew_tasks[1]}\n")
    print(f"{Mon_staff[2]}\n{FourCrew_tasks[2]}\n")
    print(f"{Mon_staff[3]}\n{FourCrew_tasks[3]}")
  elif day_of_week.lower() == "tuesday":
    print(f"{Tue_staff[0]}\n{FiveCrew_tasks[0]}\n")
    print(f"{Tue_staff[1]}\n{FiveCrew_tasks[1]}\n")
    print(f"{Tue_staff[2]}\n{FiveCrew_tasks[2]}\n")
    print(f"{Tue_staff[3]}\n{FiveCrew_tasks[3]}\n")
    print(f"{Tue_staff[4]}\n{FiveCrew_tasks[4]}")
  elif day_of_week.lower() == "wednesday":
    print(f"{Wed_staff[0]}\n{FiveCrew_tasks[0]}\n")
    print(f"{Wed_staff[1]}\n{FiveCrew_tasks[1]}\n")
    print(f"{Wed_staff[2]}\n{FiveCrew_tasks[2]}\n")
    print(f"{Wed_staff[3]}\n{FiveCrew_tasks[3]}\n")
    print(f"{Wed_staff[4]}\n{FiveCrew_tasks[4]}")
  elif day_of_week.lower() == "thursday":
    print(f"{Thur_staff[0]}\n{FiveCrew_tasks[0]}\n")
    print(f"{Thur_staff[1]}\n{FiveCrew_tasks[1]}\n")
    print(f"{Thur_staff[2]}\n{FiveCrew_tasks[2]}\n")
    print(f"{Thur_staff[3]}\n{FiveCrew_tasks[3]}\n")
    print(f"{Thur_staff[4]}\n{FiveCrew_tasks[4]}")
  elif day_of_week.lower() == "friday":
    print(f"{Fri_staff[0]}\n{FourCrew_tasks[0]}\n")
    print(f"{Fri_staff[1]}\n{FourCrew_tasks[1]}\n")
    print(f"{Fri_staff[2]}\n{FourCrew_tasks[2]}\n")
    print(f"{Fri_staff[3]}\n{FourCrew_tasks[3]}")
  elif day_of_week.lower() == "saturday":
    print(f"{Sat_staff[0]}\n{FiveCrew_tasks[0]}\n")
    print(f"{Sat_staff[1]}\n{FiveCrew_tasks[1]}\n")
    print(f"{Sat_staff[2]}\n{FiveCrew_tasks[2]}\n")
    print(f"{Sat_staff[3]}\n{FiveCrew_tasks[3]}")
  elif day_of_week.lower() == "sunday":
    print(f"{Sun_staff[0]}\n{FourCrew_tasks[0]}\n")
    print(f"{Sun_staff[1]}\n{FourCrew_tasks[1]}\n")
    print(f"{Sun_staff[2]}\n{FourCrew_tasks[2]}\n")
    print(f"{Sun_staff[3]}\n{FourCrew_tasks[3]}")
task_picker()