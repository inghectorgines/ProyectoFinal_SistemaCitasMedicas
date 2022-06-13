CREATE DATABASE IF NOT EXISTS ffm_citasMedicas;
USE ffm_citasMedicas;

CREATE TABLE medicos(
    id          int(25) auto_increment not null,
    nombre      varchar(100),
    apellidos   varchar(255),
    num_consultorio varchar(255),
    email       varchar(255) not null,
    user        varchar(255) not null,
    pass        varchar(255) not null,
    fecha       date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email),
    CONSTRAINT uq_user UNIQUE(user)
)ENGINE=InnoDb;

CREATE TABLE citas(
    id          int(25) auto_increment not null,
    medico_id  int(25) not null,
    paciente    varchar(255) not null,
    diagnostico     varchar(255) not null,
    descripcion MEDIUMTEXT,
    proxima_cita    varchar(255),
    fecha       date not null,
    CONSTRAINT pk_citas PRIMARY KEY(id),
    CONSTRAINT fk_cita_medico FOREIGN KEY(medico_id) REFERENCES medicos(id)
)ENGINE=InnoDb;