-- Drop tables in reverse order to maintain referential integrity

DROP TABLE IF EXISTS GYM.ExerciseSet;
DROP TABLE IF EXISTS GYM.WorkoutExercise;
DROP TABLE IF EXISTS GYM.Exercise;
DROP TABLE IF EXISTS GYM.Workout;
DROP TABLE IF EXISTS GYM.User;
DROP TABLE IF EXISTS GYM.MuscleGroup;

drop sequence GYM.user_seq;
drop sequence GYM.workout_seq;
drop sequence GYM.workoutexercise_seq;
drop sequence GYM.exerciseset_seq;
drop sequence GYM.exercise_seq;
drop sequence GYM.exercisemusclegroup_seq;
drop sequence GYM.musclegroup_seq;

drop user GYMUser;

drop database GYM;