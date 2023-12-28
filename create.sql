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
  PRIMARY KEY (AverageScore)
);

CREATE TABLE Person
(
  person_id VARCHAR(40),
  age INT,
  hours_per_day FLOAT,
  Music_id INT,
  AverageScore FLOAT,
  PRIMARY KEY (person_id),
  FOREIGN KEY (Music_id) REFERENCES Music(Music_id),
  FOREIGN KEY (AverageScore) REFERENCES Mental_Illness(AverageScore)
);
