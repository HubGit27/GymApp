-- Insert sample data into MuscleGroup table
INSERT INTO GYM.MuscleGroup (MuscleGroupID, name) VALUES
(NEXTVAL(GYM.musclegroup_seq),'Chest'),
(NEXTVAL(GYM.musclegroup_seq),'Back'),
(NEXTVAL(GYM.musclegroup_seq),'Legs'),
(NEXTVAL(GYM.musclegroup_seq),'Shoulders'),
(NEXTVAL(GYM.musclegroup_seq),'Arms'),
(NEXTVAL(GYM.musclegroup_seq), 'Lats'),
(NEXTVAL(GYM.musclegroup_seq), 'Quads'),
(NEXTVAL(GYM.musclegroup_seq), 'Calves'),
(NEXTVAL(GYM.musclegroup_seq), 'Hamstrings'),
(NEXTVAL(GYM.musclegroup_seq), 'Abs');

-- Insert sample data into Exercise table
INSERT INTO GYM.Exercise (ExerciseID, name, description) VALUES
(NEXTVAL(GYM.exercise_seq),'Bench Press', 'Lift the barbell off the rack and lower it to your chest before pushing it back up.'),
(NEXTVAL(GYM.exercise_seq),'Deadlift', 'Lift the barbell off the ground to a standing position, keeping your back straight.'),
(NEXTVAL(GYM.exercise_seq),'Squat', 'Lower your body until your thighs are parallel to the ground while holding a barbell on your shoulders.'),
(NEXTVAL(GYM.exercise_seq),'Shoulder Press', 'Press a barbell or dumbbells overhead from shoulder height to a locked-out position.'),
(NEXTVAL(GYM.exercise_seq),'Bicep Curl', 'Curl a dumbbell or barbell from a straight arm position to a flexed bicep position.');

INSERT INTO GYM.ExerciseMuscleGroup (ExerciseMuscleGroupID, ExerciseID, MuscleGroupID) VALUES
(NEXTVAL(GYM.exercisemusclegroup_seq), 1, 1),
(NEXTVAL(GYM.exercisemusclegroup_seq), 2, 2),
(NEXTVAL(GYM.exercisemusclegroup_seq), 3, 3),
(NEXTVAL(GYM.exercisemusclegroup_seq), 4, 4),
(NEXTVAL(GYM.exercisemusclegroup_seq), 5, 5);

-- Insert sample data into User table
INSERT INTO GYM.User (UserID, firstname, lastname, username, email, datejoined) VALUES
(NEXTVAL(GYM.user_seq),'John', 'Doe', 'johndoe', 'john@example.com', '2024-01-01'),
(NEXTVAL(GYM.user_seq),'Jane', 'Smith', 'janesmith', 'jane@example.com', '2024-02-15');

-- Insert sample data into Workout table
INSERT INTO GYM.Workout (WorkoutID, UserID, name, duration, date) VALUES
(NEXTVAL(GYM.workout_seq), 1, 'Upper Body Workout', '01:00:00', '2024-04-01'),
(NEXTVAL(GYM.workout_seq), 2, 'Leg Day', '01:45:00', '2024-04-03');

-- Insert sample data into WorkoutExercise table
INSERT INTO GYM.WorkoutExercise (WorkoutExerciseID, WorkoutID, ExerciseID) VALUES
(NEXTVAL(GYM.workoutexercise_seq), 1, 1),
(NEXTVAL(GYM.workoutexercise_seq), 1, 4),
(NEXTVAL(GYM.workoutexercise_seq), 2, 3),
(NEXTVAL(GYM.workoutexercise_seq), 2, 2),
(NEXTVAL(GYM.workoutexercise_seq), 2, 5);

-- Insert sample data into Set table
INSERT INTO GYM.ExerciseSet (ExerciseSetID, WorkoutExerciseID, reps, weight) VALUES
(NEXTVAL(GYM.exerciseset_seq), 1, 10, 100),
(NEXTVAL(GYM.exerciseset_seq), 1, 10, 100),
(NEXTVAL(GYM.exerciseset_seq), 1, 8, 110),
(NEXTVAL(GYM.exerciseset_seq), 2, 12, 20),
(NEXTVAL(GYM.exerciseset_seq), 2, 12, 20),
(NEXTVAL(GYM.exerciseset_seq), 2, 10, 25),
(NEXTVAL(GYM.exerciseset_seq), 3, 8, 80),
(NEXTVAL(GYM.exerciseset_seq), 3, 8, 80),
(NEXTVAL(GYM.exerciseset_seq), 3, 6, 90),
(NEXTVAL(GYM.exerciseset_seq), 4, 5, 60),
(NEXTVAL(GYM.exerciseset_seq), 4, 5, 60),
(NEXTVAL(GYM.exerciseset_seq), 4, 5, 60),
(NEXTVAL(GYM.exerciseset_seq), 5, 12, 10),
(NEXTVAL(GYM.exerciseset_seq), 5, 12, 10),
(NEXTVAL(GYM.exerciseset_seq), 5, 12, 10);