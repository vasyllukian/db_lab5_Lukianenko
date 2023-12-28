CREATE TABLE Music
(
  Fav_Genre CHAR(40),
  BPM INT,
  Effects CHAR(40),
  Music_id INT,
  PRIMARY KEY (Music_id)
);

CREATE TABLE Mental_Illness
(
  Anxiety INT,
  Depression INT,
  OCD INT,
  Insomnia INT,
  AverageScore FLOAT,
  mental_illness_id INT,
  PRIMARY KEY (mental_illness_id)
);

CREATE TABLE Person
(
  person_id VARCHAR(40),
  age INT,
  hours_per_day FLOAT,
  Music_id INT,
  mental_illness_id INT,
  PRIMARY KEY (person_id),
  FOREIGN KEY (Music_id) REFERENCES Music(Music_id),
  FOREIGN KEY (mental_illness_id) REFERENCES Mental_Illness(mental_illness_id)
);
