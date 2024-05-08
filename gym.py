from DatabaseConnection import DatabaseConnection

class DatabaseConnection:
    def __init__(self, dbconn):
        self.dbconn = dbconn

class User:
    def __init__(self, dbconn):
        self.dbconn = dbconn
        self.UserID = None
        self.firstname = None
        self.lastname = None
        self.username = None
        self.email = None
        self.password = None
        self.datejoined = None

    def getuserid(self):
        return self.UserID

    def insert(self):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Insert SQL
        sql = 'INSERT INTO User (firstname, lastname, username, email, password, datejoined) VALUES (%s, %s, %s, %s, %s, %s)'
        val = (self.firstname, self.lastname, self.username, self.email, self.password, self.datejoined)

        # Execute the SQL command
        mysqlcursor.execute(sql, val)

        # Commit changes
        tempconn.commit()
        #tempconn.close()

    def getUserIDByUsername(self, username):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Query to retrieve the user ID based on the provided username
        sql = "SELECT UserID FROM GYM.User WHERE username = %s"
        mysqlcursor.execute(sql, (username,))
        result = mysqlcursor.fetchone()

        # If a matching user is found, return the user ID
        if result:
            return result[0]
        else:
            return None
        #tempconn.close()

    # Function to check if the provided password matches the password stored in the database
    def isPasswordCorrect(self, user_id, password):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Query to retrieve the password hash for the provided user ID
        sql = "SELECT password FROM GYM.User WHERE UserID = %s"
        mysqlcursor.execute(sql, (user_id,))
        result = mysqlcursor.fetchone()
        # If a matching user is found and the provided password matches the stored password hash, return True
        if result:
            if (result[0] == password):  # Implement appropriate password hashing mechanism here
                return True
            else:
                return False
        else:
            return False
        #tempconn.close()

class MuscleGroup:
    def __init__(self, dbconn):
        self.dbconn = dbconn
        self.MuscleGroupID = None
        self.name = None

    def insert(self):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Insert SQL
        sql = 'INSERT INTO MuscleGroup (name) VALUES (%s)'
        val = (self.name,)

        # Execute the SQL command
        mysqlcursor.execute(sql, val)

        # Commit changes
        tempconn.commit()
        #tempconn.close()

    def findAll(self):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Select all rows from the MuscleGroup table
        sql = "SELECT * FROM MuscleGroup"
        mysqlcursor.execute(sql)
        results = mysqlcursor.fetchall()
        return results
#tempconn.close()
    def getMuscleGroupIDByName(self, muscle_group_name):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Select the MuscleGroupID for the given muscle group name
        sql = "SELECT MuscleGroupID FROM MuscleGroup WHERE name = %s"
        val = (muscle_group_name,)
        mysqlcursor.execute(sql, val)
        result = mysqlcursor.fetchone()

        if result:
            return result[0]
        else:
            return None
#tempconn.close()
class Exercise:
    def __init__(self, dbconn):
        self.dbconn = dbconn
        self.ExerciseID = None
        self.name = None
        self.description = None

    def insert(self):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Insert SQL
        sql = 'INSERT INTO Exercise (name, description) VALUES (%s, %s)'
        val = (self.name, self.description)

        # Execute the SQL command
        mysqlcursor.execute(sql, val)

        # Commit changes
        tempconn.commit()

    def getNameByExerciseID(self, ExerciseID):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Select the MuscleGroupID for the given muscle group name
        sql = "SELECT Name FROM Exercise WHERE ExerciseID = %s"
        val = (ExerciseID,)
        mysqlcursor.execute(sql, val)
        result = mysqlcursor.fetchone()

        if result:
            return result[0]
        else:
            return None
        
    def getExerciseIDByName(self, exercise_name):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Select the MuscleGroupID for the given muscle group name
        sql = "SELECT ExerciseID FROM Exercise WHERE name = %s"
        val = (exercise_name,)
        mysqlcursor.execute(sql, val)
        result = mysqlcursor.fetchone()

        if result:
            return result[0]
        else:
            return None
    
    def getAllExercises(self):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Select all exercises
        sql = "SELECT * FROM Exercise"
        mysqlcursor.execute(sql)
        results = mysqlcursor.fetchall()

        return results
    
    def getExercisesByMuscleGroup(self, muscle_group_id):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Select exercises based on muscle group ID
        sql = """
                SELECT e.* 
                FROM Exercise e 
                INNER JOIN ExerciseMuscleGroup emg ON e.ExerciseID = emg.ExerciseID 
                WHERE emg.MuscleGroupID = %s
            """
        mysqlcursor.execute(sql, (muscle_group_id,))
        results = mysqlcursor.fetchall()

        return results
    
    def exerciseExists(self, exerciseID):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Query to check if the exercise ID exists in the Exercise table
        sql = "SELECT COUNT(*) FROM Exercise WHERE ExerciseID = %s"
        val = (exerciseID,)
        mysqlcursor.execute(sql, val)
        result = mysqlcursor.fetchone()

        # If the count is greater than 0, the exercise ID exists
        if result and result[0] > 0:
            return True
        else:
            return False
        

class Workout:
    def __init__(self, dbconn):
        self.dbconn = dbconn
        self.WorkoutID = None
        self.UserID = None
        self.name = None
        self.duration = None
        self.date = None

    def insert(self):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Insert SQL
        sql = 'INSERT INTO Workout (UserID, name, duration, date) VALUES (%s, %s, %s, %s)'
        val = (self.UserID, self.name, self.duration, self.date)

        # Execute the SQL command
        mysqlcursor.execute(sql, val)

        # Commit changes
        tempconn.commit()
        #tempconn.close()

    def update(self):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Update SQL
        sql = 'UPDATE Workout SET duration = %s WHERE WorkoutID = %s'
        val = (self.duration, self.WorkoutID)

        # Execute the SQL command
        mysqlcursor.execute(sql, val)

        # Commit changes
        tempconn.commit()
    
    def findWorkoutID(self, userID, workoutName, date):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Query to retrieve the workout ID based on the provided user ID, workout name, and duration
        sql = "SELECT WorkoutID FROM Workout WHERE UserID = %s AND name = %s AND date = %s"
        val = (userID, workoutName, date)
        mysqlcursor.execute(sql, val)
        result = mysqlcursor.fetchone()

        # If a matching workout is found, return the workout ID
        if result:
            return result[0]
        else:
            return None
    
    def findWorkoutsByUserID(self, userID):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Query to retrieve all workouts belonging to the provided user ID
        sql = "SELECT * FROM Workout WHERE UserID = %s"
        val = (userID,)
        mysqlcursor.execute(sql, val)
        results = mysqlcursor.fetchall()

        return results
    
    def updateWorkoutDuration(self, WorkoutID, new_duration):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Update SQL
        sql = "UPDATE Workout SET duration = %s WHERE WorkoutID = %s"
        val = (new_duration, WorkoutID)

        # Execute the SQL command
        mysqlcursor.execute(sql, val)

        # Commit changes
        tempconn.commit()

class WorkoutExercise:
    def __init__(self, dbconn):
        self.dbconn = dbconn
        self.WorkoutExerciseID = None
        self.WorkoutID = None
        self.ExerciseID = None

    def insert(self):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Insert SQL
        sql = 'INSERT INTO WorkoutExercise (WorkoutID, ExerciseID) VALUES (%s, %s)'
        val = (self.WorkoutID, self.ExerciseID)

        # Execute the SQL command
        mysqlcursor.execute(sql, val)

        # Commit changes
        tempconn.commit()
        #tempconn.close()
        
    def findWorkoutExerciseID(self, workoutID, exerciseID):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Query to retrieve the WorkoutExerciseID based on the provided WorkoutID and ExerciseID
        sql = "SELECT WorkoutExerciseID FROM WorkoutExercise WHERE WorkoutID = %s AND ExerciseID = %s"
        val = (workoutID, exerciseID)
        mysqlcursor.execute(sql, val)
        result = mysqlcursor.fetchone()

        # If a matching workout exercise is found, return the WorkoutExerciseID
        if result:
            return result[0]
        else:
            return None
        
    def findWorkoutExercisesByWorkoutID(self, workoutID):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Query to retrieve all WorkoutExercises with the provided WorkoutID
        sql = "SELECT * FROM WorkoutExercise WHERE WorkoutID = %s"
        val = (workoutID,)
        mysqlcursor.execute(sql, val)
        results = mysqlcursor.fetchall()
        return results

    def deleteWorkoutExercise(self, WorkoutExerciseID):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Delete SQL
        sql = "DELETE FROM WorkoutExercise WHERE WorkoutExerciseID = %s"
        val = (WorkoutExerciseID,)

        # Execute the SQL command
        mysqlcursor.execute(sql, val)

        # Commit changes
        tempconn.commit()

class ExerciseMuscleGroup:
    def __init__(self, dbconn):
        self.dbconn = dbconn
        self.ExerciseMuscleGroupID = None
        self.ExerciseID = None
        self.MuscleGroupID = None

    def insert(self):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Insert SQL
        sql = 'INSERT INTO ExerciseMuscleGroup (ExerciseID, MuscleGroupID) VALUES (%s, %s)'
        val = (self.ExerciseID, self.MuscleGroupID)

        # Execute the SQL command
        mysqlcursor.execute(sql, val)

        # Commit changes
        tempconn.commit()
        #tempconn.close()

class ExerciseSet:
    def __init__(self, dbconn):
        self.dbconn = dbconn
        self.ExerciseSetID = None
        self.WorkoutExerciseID = None
        self.reps = None
        self.weight = None

    def insert(self):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Insert SQL
        sql = 'INSERT INTO ExerciseSet (WorkoutExerciseID, reps, weight) VALUES (%s, %s, %s)'
        val = (self.WorkoutExerciseID, self.reps, self.weight)

        # Execute the SQL command
        mysqlcursor.execute(sql, val)

        # Commit changes
        tempconn.commit()
        #tempconn.close()

    def findExerciseSetsByworkoutexerciseid(self, workoutexerciseid):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Query to retrieve all WorkoutExercises with the provided WorkoutID
        sql = "SELECT * FROM ExerciseSet WHERE WorkoutExerciseID = %s"
        val = (workoutexerciseid,)
        mysqlcursor.execute(sql, val)
        results = mysqlcursor.fetchall()
        return results

    def editExerciseSet(self, ExerciseSetID, reps, weight):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Update SQL
        sql = "UPDATE ExerciseSet SET reps = %s, weight = %s WHERE ExerciseSetID = %s"
        val = (reps, weight, ExerciseSetID)

        # Execute the SQL command
        mysqlcursor.execute(sql, val)

        # Commit changes
        tempconn.commit()

    def deleteExerciseSet(self, ExerciseSetID):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Delete SQL
        sql = "DELETE FROM ExerciseSet WHERE ExerciseSetID = %s"
        val = (ExerciseSetID,)

        # Execute the SQL command
        mysqlcursor.execute(sql, val)

        # Commit changes
        tempconn.commit()

    def deleteExerciseSetsByWorkoutExerciseID(self, WorkoutExerciseID):
        tempconn = self.dbconn.getConnection()
        mysqlcursor = tempconn.cursor()

        # Delete SQL
        sql = "DELETE FROM ExerciseSet WHERE WorkoutExerciseID = %s"
        val = (WorkoutExerciseID,)

        # Execute the SQL command
        mysqlcursor.execute(sql, val)

        # Commit changes
        tempconn.commit()