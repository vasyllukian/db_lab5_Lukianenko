-------------------------------------------------------------
-- Populate mental_illness table
-------------------------------------------------------------
INSERT INTO mental_illness(anxiety, depression, insomnia, ocd, averagescore, mental_illness_id)
VALUES('3','0','1','0','1', '1');
INSERT INTO mental_illness(anxiety, depression, insomnia, ocd, averagescore, mental_illness_id)
VALUES('7','2','2','1','3', '2');
INSERT INTO mental_illness(anxiety, depression, insomnia, ocd,  averagescore, mental_illness_id)
VALUES('7','7','10','1','6.25', '3');
INSERT INTO mental_illness(anxiety, depression, insomnia, ocd, averagescore, mental_illness_id)
VALUES('9','7','3','3','5.5',  '4');
INSERT INTO mental_illness(anxiety, depression, insomnia, ocd, averagescore, mental_illness_id)
VALUES('7','2','5','9','6.5', '5');
INSERT INTO mental_illness(anxiety, depression, insomnia, ocd, averagescore, mental_illness_id)
VALUES('8','8','7','7','7.5',  '6');
INSERT INTO mental_illness(anxiety, depression, insomnia, ocd, averagescore, mental_illness_id)
VALUES('4','8','6','0','4.5', '7');
INSERT INTO mental_illness(anxiety, depression, insomnia, ocd, averagescore, mental_illness_id)
VALUES('7','5','4','1','4.25', '8');
-------------------------------------------------------------
-- Populate music table
-------------------------------------------------------------
INSERT INTO music(fav_genre, bpm, effects, music_id)
VALUES('Latin','156', NULL ,'1');
INSERT INTO music(fav_genre, bpm, effects, music_id)
VALUES('Rock','119', NULL ,'2');
INSERT INTO music(fav_genre, bpm, effects, music_id)
VALUES('Video game music','132', 'No effect' ,'3');
INSERT INTO music(fav_genre, bpm, effects, music_id)
VALUES('Jazz','84', 'Improve' ,'4');
INSERT INTO music(fav_genre, bpm, effects, music_id)
VALUES('R&B','107', 'Improve','5');
INSERT INTO music(fav_genre, bpm, effects, music_id)
VALUES('Jazz','86', 'Improve' ,'6');
INSERT INTO music(fav_genre, bpm, effects, music_id)
VALUES('Video game music','66', 'Improve','7');
INSERT INTO music(fav_genre, bpm, effects, music_id)
VALUES('Pop',NULL, 'Worsen','8');
-------------------------------------------------------------
-- Populate person table
-------------------------------------------------------------
INSERT INTO person(person_id, age, hours_per_day, music_id, mental_illness_id)
VALUES('8/27/2022 19:29:02','18','3','1','1');
INSERT INTO person(person_id, age, hours_per_day, music_id, mental_illness_id)
VALUES('8/27/2022 19:57:31','63','1.5','2','2');
INSERT INTO person(person_id, age, hours_per_day, music_id, mental_illness_id)
VALUES('8/27/2022 21:28:18','18','4','3','3');
INSERT INTO person(person_id, age, hours_per_day, music_id, mental_illness_id)
VALUES('8/27/2022 21:40:40','61','2.5','4','4');
INSERT INTO person(person_id, age, hours_per_day, music_id, mental_illness_id)
VALUES('8/27/2022 21:54:47','18','4','5','5');
INSERT INTO person(person_id, age, hours_per_day, music_id, mental_illness_id)
VALUES('8/27/2022 21:56:50','18','5','6','6');
INSERT INTO person(person_id, age, hours_per_day, music_id, mental_illness_id)
VALUES('8/27/2022 22:00:29','18','3','7','7');
INSERT INTO person(person_id, age, hours_per_day, music_id, mental_illness_id)
VALUES('8/27/2022 23:19:52','17','2','8','8');
