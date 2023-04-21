CREATE DATABASE  IF NOT EXISTS TU_PSI;

USE TU_PSI;

CREATE TABLE TIPOS_DE_TERAPIA(
ID INT PRIMARY KEY AUTO_INCREMENT,
NOMBRE_RAMA VARCHAR(45)
);
INSERT INTO tipos_de_terapia(NOMBRE_RAMA) VALUES('Terapia Familiar');
INSERT INTO tipos_de_terapia(NOMBRE_RAMA) VALUES('Terapia de pareja');
INSERT INTO tipos_de_terapia(NOMBRE_RAMA) VALUES('Individual');
INSERT INTO tipos_de_terapia(NOMBRE_RAMA) VALUES('Consultoría de empresas');
INSERT INTO tipos_de_terapia(NOMBRE_RAMA) VALUES('Deportiva');

CREATE TABLE UBICACION(
ID INT PRIMARY KEY AUTO_INCREMENT,
PROVINCIA VARCHAR(45)
);
INSERT INTO UBICACION(PROVINCIA) VALUES('BUENOS AIRES');
INSERT INTO UBICACION(PROVINCIA) VALUES('Ciudad Autónoma de Buenos Aires');
INSERT INTO UBICACION(PROVINCIA) VALUES('Catamarca');
INSERT INTO UBICACION(PROVINCIA) VALUES('Chaco');
INSERT INTO UBICACION(PROVINCIA) VALUES('Chubut');
INSERT INTO UBICACION(PROVINCIA) VALUES('Córdoba');
INSERT INTO UBICACION(PROVINCIA) VALUES('Corrientes');
INSERT INTO UBICACION(PROVINCIA) VALUES('Entre Ríos');
INSERT INTO UBICACION(PROVINCIA) VALUES('Formosa');
INSERT INTO UBICACION(PROVINCIA) VALUES('Jujuy');
INSERT INTO UBICACION(PROVINCIA) VALUES('La Pampa');
INSERT INTO UBICACION(PROVINCIA) VALUES('La Rioja');
INSERT INTO UBICACION(PROVINCIA) VALUES('Mendoza');
INSERT INTO UBICACION(PROVINCIA) VALUES('Misiones');
INSERT INTO UBICACION(PROVINCIA) VALUES('Neuquén');
INSERT INTO UBICACION(PROVINCIA) VALUES('Río Negro');
INSERT INTO UBICACION(PROVINCIA) VALUES('Salta');
INSERT INTO UBICACION(PROVINCIA) VALUES('San Juan');
INSERT INTO UBICACION(PROVINCIA) VALUES('San Luis');
INSERT INTO UBICACION(PROVINCIA) VALUES('Santa Cruz');
INSERT INTO UBICACION(PROVINCIA) VALUES('Santa Fe');
INSERT INTO UBICACION(PROVINCIA) VALUES('Tierra del Fuego');
INSERT INTO UBICACION(PROVINCIA) VALUES('Tucuman');



CREATE TABLE PACIENTE_CONSULTOR(
DNI_PACIENTE INT UNIQUE NOT NULL,
NOMBRE VARCHAR (100) NOT NULL,
APELLIDO VARCHAR(100),
EMAIL VARCHAR(45),
TELEFONO BIGINT,
FECHA_NAC DATE,
SEXO VARCHAR (50),
UBICACION_ID INT,
CONSTRAINT PK_ID_PACIENTE PRIMARY KEY (DNI_PACIENTE),
CONSTRAINT FK_UBICACION FOREIGN KEY (UBICACION_ID) REFERENCES UBICACION (ID));

INSERT INTO PACIENTE_CONSULTOR(DNI_PACIENTE,NOMBRE,APELLIDO,EMAIL,TELEFONO,FECHA_NAC,SEXO, UBICACION_ID ) VALUES
(8888888, 'Taoufik','Saidi', 'esun-mail-deprueba@gnail.com', 045678987,'1999-01-01','Masculino',1);
CREATE TABLE PSICOLOGO(
NOMBRE VARCHAR(100) NOT NULL,
APELLIDO VARCHAR (100) NOT NULL,
EMAIL VARCHAR(45),
CONTRASEÑA VARCHAR(8),
MATRICULA INT UNIQUE NOT NULL,
SEXO VARCHAR(15) NOT NULL,
UBICACION INT,
TIPOS_DE_TERAPIA INT,
PACIENTE_CONSULTOR INT,
CONSTRAINT PK_MATRICULA PRIMARY KEY (MATRICULA),
CONSTRAINT FK_UBIC_ID FOREIGN KEY (UBICACION) REFERENCES UBICACION (ID),
CONSTRAINT FK_TIPOS_DE_TERAPIA FOREIGN KEY (TIPOS_DE_TERAPIA) REFERENCES TIPOS_DE_TERAPIA(ID),
CONSTRAINT FK_PACIENTE_CONSULTOR FOREIGN KEY (PACIENTE_CONSULTOR) REFERENCES PACIENTE_CONSULTOR (DNI_PACIENTE));

INSERT INTO PSICOLOGO(NOMBRE, APELLIDO, EMAIL, CONTRASEÑA, MATRICULA, SEXO, UBICACION, TIPOS_DE_TERAPIA, PACIENTE_CONSULTOR) 
VALUES
('Sigmund', 'Freud','freud@gmail.com','freud88',75689, 'Masculino', 1, 1,8888888);


