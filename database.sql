CREATE DATABASE isnccmailup;
CREATE TABLE mail_status (
  id INTEGER PRIMARY KEY,
  status TINYINT(1),
  time TIMESTAMP DEFAULT NOW()
) ENGINE InnoDb CHARACTER SET UTF8;