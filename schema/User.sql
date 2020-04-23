CREATE TABLE IF NOT EXISTS `user` (
  `id` INT NOT NULL auto_increment,
  `username` VARCHAR(64) NOT NULL,
  `email` VARCHAR(120) NOT NULL,
  `password_hash` VARCHAR(128) NOT NULL,
  `login_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `username` (`username`))
ENGINE = InnoDB;