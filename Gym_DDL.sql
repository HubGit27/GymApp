CREATE USER 'GYMUser' IDENTIFIED BY 'osboxes.org';

CREATE DATABASE GYM;

grant all privileges on GYM.* TO 'GYMUser';

-- User table
CREATE TABLE GYM.User (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    username VARCHAR(50) UNIQUE,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100),
    datejoined DATE
);

-- MuscleGroup table
CREATE TABLE GYM.MuscleGroup (
    MuscleGroupID INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) UNIQUE
);

-- Exercise table
CREATE TABLE GYM.Exercise (
    ExerciseID INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    description TEXT
);

-- Workout table
CREATE TABLE GYM.Workout (
    WorkoutID INT PRIMARY KEY AUTO_INCREMENT,
    UserID INT,
    name VARCHAR(100),
    duration TIME,
    date DATE,
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);

-- WorkoutExercise table
CREATE TABLE GYM.WorkoutExercise (
    WorkoutExerciseID INT PRIMARY KEY AUTO_INCREMENT,
    WorkoutID INT,
    ExerciseID INT,
    FOREIGN KEY (WorkoutID) REFERENCES Workout(WorkoutID),
    FOREIGN KEY (ExerciseID) REFERENCES Exercise(ExerciseID)
);

-- ExerciseMuscleGroup table
CREATE TABLE GYM.ExerciseMuscleGroup (
    ExerciseMuscleGroupID INT PRIMARY KEY AUTO_INCREMENT,
    ExerciseID INT,
    MuscleGroupID INT,
    FOREIGN KEY (ExerciseID) REFERENCES Exercise(ExerciseID),
    FOREIGN KEY (MuscleGroupID) REFERENCES MuscleGroup(MuscleGroupID)
);

-- Set table
CREATE TABLE GYM.ExerciseSet (
    ExerciseSetID INT PRIMARY KEY AUTO_INCREMENT,
    WorkoutExerciseID INT,
    reps INT,
    weight DECIMAL(10,2),
    FOREIGN KEY (WorkoutExerciseID) REFERENCES WorkoutExercise(WorkoutExerciseID)
);

-- Sequence creation
CREATE SEQUENCE GYM.user_seq;
CREATE SEQUENCE GYM.workout_seq;
CREATE SEQUENCE GYM.workoutexercise_seq;
CREATE SEQUENCE GYM.exerciseset_seq;
CREATE SEQUENCE GYM.exercise_seq;
CREATE SEQUENCE GYM.exercisemusclegroup_seq;
CREATE SEQUENCE GYM.musclegroup_seq;