from gym import User
from gym import MuscleGroup
from gym import Exercise
from gym import Workout
from gym import WorkoutExercise
from gym import ExerciseMuscleGroup
from gym import ExerciseSet
from DatabaseConnection import DatabaseConnection
from datetime import datetime
import time

dbcon = DatabaseConnection() # create a DatabaseConnection object that will get passed around

def addMuscleGroupRelationship(exercise_info):
    # Check if exercise already exists in the database
    exercise = Exercise(dbcon)
    exercise_id = exercise.getExerciseIDByName(exercise_info[0])

    # If exercise does not exist, insert it into the database
    if not exercise_id:
        exercise.name = exercise_info[0]
        exercise.description = exercise_info[2]
        exercise.insert()
        exercise_id = exercise.getExerciseIDByName(exercise_info[0])

    # Create a MuscleGroup object and get the MuscleGroupID
    muscle_group = MuscleGroup(dbcon)
    muscle_group_id = muscle_group.getMuscleGroupIDByName(exercise_info[1])

    if not muscle_group_id:
        muscle_group.name = exercise_info[1]
        muscle_group.insert()
        muscle_group_id = muscle_group.getMuscleGroupIDByName(exercise_info[1])

    # Create an ExerciseMuscleGroup object and establish the relationship
    exercise_muscle_group = ExerciseMuscleGroup(dbcon)
    exercise_muscle_group.ExerciseID = exercise_id
    exercise_muscle_group.MuscleGroupID = muscle_group_id
    exercise_muscle_group.insert()


def SetupData():
    muscle_group = MuscleGroup(dbcon)
    muscle_group.name = "Chest"
    muscle_group.insert()
    muscle_group.name = "Back"
    muscle_group.insert()
    muscle_group.name = "Legs"
    muscle_group.insert()
    muscle_group.name = "Shoulders"
    muscle_group.insert()
    muscle_group.name = "Arms"
    muscle_group.insert()
    muscle_group.name = "Hamstrings"
    muscle_group.insert()
    muscle_group.name = "Quads"
    muscle_group.insert()
    muscle_group.name = "Calves"
    muscle_group.insert()
    muscle_group.name = "Bicep"
    muscle_group.insert()
    muscle_group.name = "Tricep"
    muscle_group.insert()
    muscle_group.name = "Lats"
    muscle_group.insert()
    muscle_group.name = "Forearm"
    muscle_group.insert()
    muscle_group.name = "Abs"
    muscle_group.insert()



    exercises = [
        ["Bench Press", "Chest", "Lift the barbell off the rack and lower it to your chest before pushing it back up."],
        ["Bench Press", "Tricep", "Lift the barbell off the rack and lower it to your chest before pushing it back up."],
        ["Deadlift", "Back", "Lift the barbell off the ground to a standing position, keeping your back straight."],
        ["Deadlift", "Legs", "Lift the barbell off the ground to a standing position, keeping your back straight."],
        ["Squat", "Legs", "Lower your body until your thighs are parallel to the ground while holding a barbell on your shoulders."],
        ["Shoulder Press", "Shoulders", "Press a barbell or dumbbells overhead from shoulder height to a locked-out position."],
        ["Bicep Curl", "Bicep", "Curl a dumbbell or barbell from a straight arm position to a flexed bicep position."],
        ["Bicep Curl", "Arms", "Curl a dumbbell or barbell from a straight arm position to a flexed bicep position."],
        ["Pull-up", "Lats", "Hang from a bar with your palms facing away from you, then pull your body up until your chin is above the bar."],
        ["Push-up", "Chest", "Start in a plank position, then lower your body until your chest touches the ground before pushing back up."],
        ["Dumbbell Row", "Back", "Stand with a dumbbell in each hand, bend at the waist, and row the weights up to your sides, keeping your back straight."],
        ["Lunges", "Legs", "Step forward with one leg and lower your body until both knees are bent at 90-degree angles, then return to standing."],
        ["Russian Twist", "Abs", "Sit on the floor with your knees bent and feet lifted, then twist your torso from side to side, touching the floor with the weight or your hands."],
        ["Plank", "Abs", "Hold yourself in a push-up position with your body forming a straight line from head to heels, engaging your core muscles."],
        ["Crunches", "Abs", "Lie on your back with your knees bent and feet flat on the floor, then lift your shoulders off the ground, squeezing your abdominal muscles."],
        ["Leg Press", "Quads", "Sit on a leg press machine and push the weight away from you using your legs, extending them fully before returning to the starting position."],
        ["Leg Press", "Legs", "Sit on a leg press machine and push the weight away from you using your legs, extending them fully before returning to the starting position."],
        ["Tricep Dip", "Tricep", "Position your hands shoulder-width apart on a stable surface behind you, then lower your body by bending your elbows until they're at 90-degree angles."],
        ["Tricep Dip", "Arms", "Position your hands shoulder-width apart on a stable surface behind you, then lower your body by bending your elbows until they're at 90-degree angles."],
        ["Calf Raise", "Calves", "Stand with your feet hip-width apart and raise your heels as high as possible, then lower them back down."],
        ["Romanian Deadlift", "Hamstrings", "Hold a barbell with an overhand grip and straight arms, then bend at the hips, keeping your back straight, until you feel a stretch in your hamstrings."],
        ["Bent Over Row", "Back", "Hold a barbell with an overhand grip, bend at the waist, and row the weight up to your lower chest, squeezing your shoulder blades together."],
        ["Chest Flyes", "Chest", "Lie on a flat bench with a dumbbell in each hand, arms extended above your chest, then lower the weights out to the sides in a wide arc before bringing them back together."],
        ["Hamstring Curl", "Hamstrings", "Lie face down on a leg curl machine and curl the weight up toward your buttocks by bending your knees, then lower back down with control."],
        ["Hamstring Curl", "Legs", "Lie face down on a leg curl machine and curl the weight up toward your buttocks by bending your knees, then lower back down with control."],
        ["Incline Bench Press", "Chest", "Lie on an incline bench with a barbell or dumbbells, then press the weight up over your chest, keeping your elbows at a 45-degree angle to your body."],
        ["Side Plank", "Abs", "Lie on your side with your legs extended and prop yourself up on your elbow and forearm, keeping your body in a straight line from head to heels."]
    ]

    # Add exercises to a muscle group
    for exercise_info in exercises:
        addMuscleGroupRelationship(exercise_info)

def GetUser():
    user = User(dbcon)
    invalid = True
    while invalid:
        userInput = int(input("Enter 1 to create account or 2 to sign in: "))
        if userInput in [1, 2]:
            if userInput == 1:
                user.firstname = input('Enter firstname: ')
                user.lastname = input('Enter lastname: ')
                user.username = input('Enter username: ')
                user.email = input('Enter email: ')
                user.password = input('Enter password: ')
                user.datejoined = datetime.now().date()
                user.insert()
                user_id = user.getUserIDByUsername(user.username)
                print(user_id)
                invalid = False
            if userInput == 2:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                user_id = user.getUserIDByUsername(username)
                if user_id:
                    # If the username exists, check if the provided password is correct
                    if user.isPasswordCorrect(user_id, password):
                        print("Sign-in successful!")
                        invalid = False
                        # Perform any additional actions after successful sign-in
                    else:
                        print("Incorrect password. Please try again.")
                else:
                    print("Username not found. Please try again.")
        else:
            print("Invalid input. Please enter 1 or 2.")

    return user_id

def viewExercises():
    muscle_group = MuscleGroup(dbcon)
    print("0. Print all exercises")
    allmusclegroups = muscle_group.findAll()
    for result in allmusclegroups:
        print(f"{result[0]}. Print {result[1]} exercises")
    userInput = int(input("Which exercises would you like to print: "))

    exercise = Exercise(dbcon)

    if userInput == 0:
        allexercises = exercise.getAllExercises()
    else:
        allexercises = exercise.getExercisesByMuscleGroup(userInput)

    for i in allexercises:
            print(f"{i[0]}. {i[1]} - {i[2]}") 

def startWorkout(userID):
    workoutexercise = WorkoutExercise(dbcon)
    exercise = Exercise(dbcon)
    exerciseset = ExerciseSet(dbcon)
    workout = Workout(dbcon)
    workout.UserID = userID
    date = datetime.now().date()
    workout.date = date
    WorkoutName = input("Enter the name of your workout: ")
    workout.name = WorkoutName
    total_time_start = time.time() # starts "full running time" timer
    workout.duration = "00:00:00"
    workout.insert()
    workoutid = workout.findWorkoutID(userID, WorkoutName, date)
    userInput = 0
    while (userInput < 4):
        print("1. Add an Exercise")
        print("2. Edit Exercise")
        print("3. Delete Exercise")
        print("4. End Workout")
        userInput = int(input("Enter Selection: "))

        if(userInput == 1):
            
            print("Enter the ID of the exercise you would like to do. Enter 0 to view exercises")
            tempInput = int(input("Enter Selection: "))
            if tempInput == 0:
                viewExercises()
                tempInput = int(input("Enter the ID of your exercise: "))

            if exercise.exerciseExists(tempInput):
                workoutexercise.ExerciseID = tempInput
                workoutexercise.WorkoutID = workoutid
                workoutexercise.insert()
                workoutexerciseid = workoutexercise.findWorkoutExerciseID(workoutid, tempInput)
                
                tempInput = 0
                while tempInput != 2:
                    reps = input("How many reps did you do? ")
                    weight = input("For how much weight? ")
                    exerciseset.WorkoutExerciseID = workoutexerciseid
                    exerciseset.reps = reps
                    exerciseset.weight = weight
                    exerciseset.insert()
                    tempInput = int(input("Enter 1 to add another set. Enter 2 to finish exercise: "))
            else:
                print("Exercise does not exist")

        elif (userInput == 2):
            print("editing exercises")
            #Print all exercises and sets for each exercise
            allexercises = workoutexercise.findWorkoutExercisesByWorkoutID(workoutid)
            for i in allexercises:
                print(f"{exercise.getNameByExerciseID(i[2])}: ")
                exercisesets = exerciseset.findExerciseSetsByworkoutexerciseid(i[0])
                counter = 1
                for j in exercisesets:
                    print(f"    Set {counter}: {j[2]} reps at {j[3]} pounds (ID: {j[0]})")
                    counter += 1
        
            setIdInput = int(input("Enter the ID of the set you would like to change: "))
            editDeleteInput = int(input("Enter 1 to edit the set, enter 2 to delete the set"))
            if editDeleteInput == 1:
                reps = int(input("Enter how many reps? "))
                weight = int(input("Enter how much weight"))
                exerciseset.editExerciseSet(setIdInput, reps, weight)
            else:
                exerciseset.deleteExerciseSet(setIdInput)
                print("set deleted")
        elif (userInput == 3):
            print("deleting exercises")
            #Print all exercises and sets for each exercise
            allexercises = workoutexercise.findWorkoutExercisesByWorkoutID(workoutid)
            for i in allexercises:
                print(f"{exercise.getNameByExerciseID(i[2])}: (ID: {i[0]})")
                exercisesets = exerciseset.findExerciseSetsByworkoutexerciseid(i[0])
                counter = 1
                for j in exercisesets:
                    print(f"    Set {counter}: {j[2]} reps at {j[3]} pounds")
                    counter += 1
            
            workoutExerciseSetIdInput = print("Enter the ID of the exercise you would like to delete")
            exerciseset.deleteExerciseSetsByWorkoutExerciseID(workoutExerciseSetIdInput)
            workoutexercise.deleteWorkoutExercise(workoutExerciseSetIdInput)
            
        else:
            total_time_end = time.time()
            total_time = total_time_end - total_time_start
            workout.updateWorkoutDuration(workoutid, total_time)
            print(f"Total Workout time: {total_time}")
            allexercises = workoutexercise.findWorkoutExercisesByWorkoutID(workoutid)
            for i in allexercises:
                print(f"{exercise.getNameByExerciseID(i[2])}: ")
                exercisesets = exerciseset.findExerciseSetsByworkoutexerciseid(i[0])
                counter = 1
                for j in exercisesets:
                    print(f"    Set {counter}: {j[2]} reps at {j[3]} pounds)")
                    counter += 1



def viewWorkouts(userID):
    workoutexercise = WorkoutExercise(dbcon)
    exercise = Exercise(dbcon)
    exerciseset = ExerciseSet(dbcon)
    workout = Workout(dbcon)

    workouts = workout.findWorkoutsByUserID(userID)
    for i in workouts:
        workoutid = i[0]
        workoutname = i[2]
        workouttime = i[3]
        workoutdate = i[4]
        print(f"{workoutname}: {workouttime} : {workoutdate}")
        allexercises = workoutexercise.findWorkoutExercisesByWorkoutID(workoutid)
        for i in allexercises:
            print(f"    {exercise.getNameByExerciseID(i[2])}: ")
            exercisesets = exerciseset.findExerciseSetsByworkoutexerciseid(i[0])
            counter = 1
            for j in exercisesets:
                print(f"        Set {counter}: {j[2]} reps at {j[3]} pounds")
                counter += 1


def main():
    userInput = input("Has the database been loaded? Enter yes or no: ")
    if(userInput == "no"):
        SetupData()
    userID = GetUser()
    userInput = 0
    while (userInput < 4):
        print("1. start a workout")
        print("2. view exercises")
        print("3. view your workouts")
        print("4. quit")
        userInput = int(input("Enter Selection: "))

        if(userInput == 1):
            startWorkout(userID)
        elif (userInput == 2):
            viewExercises()
        elif (userInput == 3):
            viewWorkouts(userID)
        else:
            print("Programming is terminating")
            dbcon.close()


main()