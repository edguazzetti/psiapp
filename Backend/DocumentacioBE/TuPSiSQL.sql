CREATE DATABASE  IF NOT EXISTS TUPSI;

USE TUPSI;

CREATE TABLE ADMINISTRADOR(
DNI_ADMINISTRADOR INT UNIQUE NOT NULL,
NOMBRE_A VARCHAR (100) NOT NULL,
APELLIDO_A VARCHAR(100),
EMAIL_A VARCHAR(45) UNIQUE NOT NULL,
CONTRASENA_A VARCHAR(45) NOT NULL,
CONSTRAINT PK_ID_ADM PRIMARY KEY (DNI_ADMINISTRADOR)
);

CREATE TABLE TIPOS_DE_TERAPIA(
ID_T INT  AUTO_INCREMENT,
NOMBRE_RAMA VARCHAR(45),
CONSTRAINT PK_ID_T PRIMARY KEY (ID_T)
);


CREATE TABLE UBICACION(
ID_U INT  AUTO_INCREMENT,
PROVINCIA VARCHAR(45),
LOCALIDAD VARCHAR (45),
CONSTRAINT PK_ID_U PRIMARY KEY (ID_U)
);



CREATE TABLE USUARIO_PACIENTE(
DNI_PACIENTE INT UNIQUE NOT NULL,
NOMBRE_P VARCHAR (100) NOT NULL,
APELLIDO_P VARCHAR(100),
EMAIL_P VARCHAR(45) UNIQUE NOT NULL,
CONTRASEÑA_P VARCHAR(45) NOT NULL,
PROVINCIA_P VARCHAR,
CONSTRAINT PK_ID_PACIENTE PRIMARY KEY (DNI_PACIENTE),
CONSTRAINT FK_PROVINCIA_P FOREIGN KEY (PROVINCIA_P) REFERENCES UBICACION (ID_U)
);

CREATE TABLE PROFESIONAL(
MATRICULA_PR INT UNIQUE NOT NULL,
NOMBRE_PR VARCHAR(100) NOT NULL,
APELLIDO_PR VARCHAR (100) NOT NULL,
EMAIL_PR VARCHAR(45),
CONTRASEÑA_PR VARCHAR(8),
PROVINCIA_PR VARCHAR(45),
LOCALIDAD_PR VARCHAR(45),
TIPOS_DE_TERAPIA_PR VARCHAR(45),
CONSTRAINT PK_MATRICULA PRIMARY KEY (MATRICULA_PR),
CONSTRAINT FK_TIPOS_DE_TERAPIA_PR FOREIGN KEY (TIPOS_DE_TERAPIA_PR) REFERENCES TIPOS_DE_TERAPIA(ID_T),
CONSTRAINT FK_PROVINCIA_PR FOREIGN KEY (PROVINCIA_PR) REFERENCES UBICACION (ID_U)
 );

CREATE TABLE PLANES (
ID_PLAN INT AUTO_INCREMENT NOT NULL,
PRECIO_PLAN INT (12),
DNI_ADM_P INT UNIQUE NOT NULL,
NOMBRE_PLAN VARCHAR (50),
CONSTRAINT PK_ID_PLAN PRIMARY KEY (ID_PLAN),
CONSTRAINT FK_DNI_ADM_P FOREIGN KEY (DNI_ADM_P) REFERENCES ADMINISTRADOR (DNI_ADMINISTRADOR)
);

CREATE TABLE PAGOS_SUSCRIPCIONES (
ID_PAGO INT AUTO_INCREMENT NOT NULL,
TIPO_PAGO VARCHAR (20),
ID_PLAN_P INT (12),
FECHA_INICIO DATE,
FECHA_CADUCIDAD DATE,
DNI_PAC INT UNIQUE NOT NULL,
CONSTRAINT PK_ID_PAGO PRIMARY KEY (ID_PAGO),
CONSTRAINT FK_DNI_PAC FOREIGN KEY (DNI_PAC) REFERENCES USUARIO_PACIENTE (DNI_PACIENTE),
CONSTRAINT FK_ID_PLAN FOREIGN KEY (ID_PLAN_P) REFERENCES PLANES (ID_PLAN)
);
