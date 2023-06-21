-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 21-06-2023 a las 03:54:51
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `basededatos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `authtoken_token`
--

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `authtoken_token`
--

INSERT INTO `authtoken_token` (`key`, `created`, `user_id`) VALUES
('255432cf1b0b6417550bd21866214473f9bfab35', '2023-06-20 23:54:01.139561', 5),
('3df487f983beaabeeae7512784a640b264fd6e00', '2023-06-20 20:30:53.388275', 1),
('4afa8a3bf6dd934e9904a8a06a8f27e891b20a44', '2023-06-21 01:53:22.610258', 8),
('57e4797e11499c03979bc8bb4420a1b493c6021d', '2023-06-21 01:41:59.486251', 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'grupofull');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 5),
(6, 1, 6),
(7, 1, 7),
(8, 1, 8),
(9, 1, 9),
(10, 1, 10),
(11, 1, 11),
(12, 1, 12),
(13, 1, 13),
(14, 1, 14),
(15, 1, 15),
(16, 1, 16),
(17, 1, 17),
(18, 1, 18),
(19, 1, 19),
(20, 1, 20),
(21, 1, 21),
(22, 1, 22),
(23, 1, 23),
(24, 1, 24),
(25, 1, 25),
(26, 1, 26),
(27, 1, 27),
(28, 1, 28),
(29, 1, 29),
(30, 1, 30),
(31, 1, 31),
(32, 1, 32),
(33, 1, 33),
(34, 1, 34),
(35, 1, 35),
(36, 1, 36),
(37, 1, 37),
(38, 1, 38),
(39, 1, 39),
(40, 1, 40),
(41, 1, 41),
(42, 1, 42),
(43, 1, 43),
(44, 1, 44),
(45, 1, 45),
(46, 1, 46),
(47, 1, 47),
(48, 1, 48),
(49, 1, 49),
(50, 1, 50),
(51, 1, 51),
(52, 1, 52),
(53, 1, 53),
(54, 1, 54),
(55, 1, 55),
(56, 1, 56);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_user'),
(22, 'Can change user', 6, 'change_user'),
(23, 'Can delete user', 6, 'delete_user'),
(24, 'Can view user', 6, 'view_user'),
(25, 'Can add Token', 7, 'add_token'),
(26, 'Can change Token', 7, 'change_token'),
(27, 'Can delete Token', 7, 'delete_token'),
(28, 'Can view Token', 7, 'view_token'),
(29, 'Can add token', 8, 'add_tokenproxy'),
(30, 'Can change token', 8, 'change_tokenproxy'),
(31, 'Can delete token', 8, 'delete_tokenproxy'),
(32, 'Can view token', 8, 'view_tokenproxy'),
(33, 'Can add Terapia', 9, 'add_terapia'),
(34, 'Can change Terapia', 9, 'change_terapia'),
(35, 'Can delete Terapia', 9, 'delete_terapia'),
(36, 'Can view Terapia', 9, 'view_terapia'),
(37, 'Can add Plan', 10, 'add_plan'),
(38, 'Can change Plan', 10, 'change_plan'),
(39, 'Can delete Plan', 10, 'delete_plan'),
(40, 'Can view Plan', 10, 'view_plan'),
(41, 'Can add Paciente', 11, 'add_paciente'),
(42, 'Can change Paciente', 11, 'change_paciente'),
(43, 'Can delete Paciente', 11, 'delete_paciente'),
(44, 'Can view Paciente', 11, 'view_paciente'),
(45, 'Can add Profesional', 12, 'add_profesional'),
(46, 'Can change Profesional', 12, 'change_profesional'),
(47, 'Can delete Profesional', 12, 'delete_profesional'),
(48, 'Can view Profesional', 12, 'view_profesional'),
(49, 'Can add Localidad', 13, 'add_localidades'),
(50, 'Can change Localidad', 13, 'change_localidades'),
(51, 'Can delete Localidad', 13, 'delete_localidades'),
(52, 'Can view Localidad', 13, 'view_localidades'),
(53, 'Can add Provincia', 14, 'add_provincias'),
(54, 'Can change Provincia', 14, 'change_provincias'),
(55, 'Can delete Provincia', 14, 'delete_provincias'),
(56, 'Can view Provincia', 14, 'view_provincias');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `core_user`
--

CREATE TABLE `core_user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(200) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `name` varchar(100) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `core_user`
--

INSERT INTO `core_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `email`, `name`, `is_active`, `is_staff`) VALUES
(1, 'pbkdf2_sha256$600000$HXwcmutvj1I9tujHSHIsUH$41dVVwT3bRpAMGp9VOFFT7dF8kNKdoQFe4PUDjNV7yM=', '2023-06-20 20:31:19.000000', 1, 'admin', 'admin@tupsi.com', 'Administrador', 1, 1),
(2, 'paciente1@', NULL, 0, 'edguazzetti', 'edguazzetti@gmail.com', 'Emiliano', 1, 0),
(3, 'profesional1@', NULL, 0, 'tuprofesional', 'tuprofesional@gmail.com', 'Profesional', 1, 0),
(4, 'password1@', NULL, 0, 'elpaciente', 'elpaciente@gmail.com', 'elpaciente', 1, 0),
(5, 'pbkdf2_sha256$600000$ADWyo5YNHSfFLqCx4k01Co$sqYAGnZeaRV6QaZ0dOYXsWCtYM5tGYTWl65Q1iYZS98=', NULL, 0, NULL, 'ejemplo@example.com', '', 1, 0),
(6, 'Tercerpaciente1@', NULL, 0, 'tres', 'tres@gmail.com', 'tercero', 1, 0),
(7, 'pbkdf2_sha256$600000$iDmCEHjAop8zl3vzmjYQdR$MK93SSJnGj0AczDZOJxIr4hGMSNc9b5rmMR6ToItMak=', NULL, 0, 'robertosanchez', 'robertosanchez@gmail.com', 'roberto', 1, 0),
(8, 'pbkdf2_sha256$600000$aStaxoZ5pAXeGeBuHAOVsK$BBBfOCPDGP7XYXUJdl8WwDjwn+GOrJtjMzAaNdV4bB8=', NULL, 0, 'PriscilaTeruel', 'pri@gmail.com', 'Priscila', 1, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `core_user_groups`
--

CREATE TABLE `core_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `core_user_groups`
--

INSERT INTO `core_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 7, 1),
(2, 8, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `core_user_user_permissions`
--

CREATE TABLE `core_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-06-20 22:30:19.645368', '1', 'admin@tupsi.com', 2, '[{\"changed\": {\"fields\": [\"Username\", \"Name\"]}}]', 6, 1),
(2, '2023-06-20 22:31:46.121322', '1', 'Terapia: Pareja', 1, '[{\"added\": {}}]', 9, 1),
(3, '2023-06-20 22:31:54.235994', '2', 'Terapia: Invididual', 1, '[{\"added\": {}}]', 9, 1),
(4, '2023-06-20 22:31:59.098751', '3', 'Terapia: Psicoanalisis', 1, '[{\"added\": {}}]', 9, 1),
(5, '2023-06-20 22:32:32.061491', '1', 'Provincia: Buenos Aires', 1, '[{\"added\": {}}]', 14, 1),
(6, '2023-06-20 22:32:40.275299', '2', 'Provincia: Cordoba', 1, '[{\"added\": {}}]', 14, 1),
(7, '2023-06-20 22:32:45.055585', '3', 'Provincia: Entre Rios', 1, '[{\"added\": {}}]', 14, 1),
(8, '2023-06-20 22:33:06.096892', '4', 'Provincia: Tucuman', 1, '[{\"added\": {}}]', 14, 1),
(9, '2023-06-20 22:33:08.821865', '5', 'Provincia: Salta', 1, '[{\"added\": {}}]', 14, 1),
(10, '2023-06-20 22:33:13.486961', '6', 'Provincia: Jujuy', 1, '[{\"added\": {}}]', 14, 1),
(11, '2023-06-20 22:33:27.507808', '1', 'Localidad: Mar del Plata', 1, '[{\"added\": {}}]', 13, 1),
(12, '2023-06-20 22:33:38.412494', '2', 'Localidad: Cordoba', 1, '[{\"added\": {}}]', 13, 1),
(13, '2023-06-20 22:33:44.892711', '3', 'Localidad: Colon', 1, '[{\"added\": {}}]', 13, 1),
(14, '2023-06-20 22:33:52.806933', '4', 'Localidad: salta', 1, '[{\"added\": {}}]', 13, 1),
(15, '2023-06-20 22:34:01.114440', '5', 'Localidad: jujuy', 1, '[{\"added\": {}}]', 13, 1),
(16, '2023-06-20 22:34:43.478652', '1', 'Plan: 4 consultas', 1, '[{\"added\": {}}]', 10, 1),
(17, '2023-06-20 22:34:58.990068', '2', 'Plan: 8 consultas', 1, '[{\"added\": {}}]', 10, 1),
(18, '2023-06-20 22:35:38.907555', '3', 'Plan: Acceso Total', 1, '[{\"added\": {}}]', 10, 1),
(19, '2023-06-20 22:37:24.682686', '2', 'edguazzetti@gmail.com', 1, '[{\"added\": {}}]', 11, 1),
(20, '2023-06-20 22:38:32.779992', '3', 'tuprofesional@gmail.com', 1, '[{\"added\": {}}]', 12, 1),
(21, '2023-06-20 23:03:22.600655', '4', 'elpaciente@gmail.com', 1, '[{\"added\": {}}]', 11, 1),
(22, '2023-06-20 23:17:55.611858', '1', 'grupofull', 1, '[{\"added\": {}}]', 3, 1),
(23, '2023-06-21 00:15:08.209638', '6', 'tres@gmail.com', 1, '[{\"added\": {}}]', 11, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(7, 'authtoken', 'token'),
(8, 'authtoken', 'tokenproxy'),
(4, 'contenttypes', 'contenttype'),
(13, 'core', 'localidades'),
(11, 'core', 'paciente'),
(10, 'core', 'plan'),
(12, 'core', 'profesional'),
(14, 'core', 'provincias'),
(9, 'core', 'terapia'),
(6, 'core', 'user'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-06-20 20:30:04.119804'),
(2, 'contenttypes', '0002_remove_content_type_name', '2023-06-20 20:30:04.170927'),
(3, 'auth', '0001_initial', '2023-06-20 20:30:04.453094'),
(4, 'auth', '0002_alter_permission_name_max_length', '2023-06-20 20:30:04.501679'),
(5, 'auth', '0003_alter_user_email_max_length', '2023-06-20 20:30:04.507120'),
(6, 'auth', '0004_alter_user_username_opts', '2023-06-20 20:30:04.512216'),
(7, 'auth', '0005_alter_user_last_login_null', '2023-06-20 20:30:04.517248'),
(8, 'auth', '0006_require_contenttypes_0002', '2023-06-20 20:30:04.518582'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2023-06-20 20:30:04.523392'),
(10, 'auth', '0008_alter_user_username_max_length', '2023-06-20 20:30:04.528322'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2023-06-20 20:30:04.533115'),
(12, 'auth', '0010_alter_group_name_max_length', '2023-06-20 20:30:04.558501'),
(13, 'auth', '0011_update_proxy_permissions', '2023-06-20 20:30:04.563642'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2023-06-20 20:30:04.568594'),
(15, 'core', '0001_initial', '2023-06-20 20:30:04.870674'),
(16, 'admin', '0001_initial', '2023-06-20 20:30:04.993108'),
(17, 'admin', '0002_logentry_remove_auto_add', '2023-06-20 20:30:04.999534'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2023-06-20 20:30:05.006703'),
(19, 'authtoken', '0001_initial', '2023-06-20 20:30:05.085002'),
(20, 'authtoken', '0002_auto_20160226_1747', '2023-06-20 20:30:05.111996'),
(21, 'authtoken', '0003_tokenproxy', '2023-06-20 20:30:05.114118'),
(22, 'sessions', '0001_initial', '2023-06-20 20:30:05.159323'),
(23, 'core', '0002_plan_provincias_terapia_profesional_paciente_and_more', '2023-06-20 20:50:17.620327');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('larfqqzadmzrnywyd27z5e6ui54wgqwb', '.eJxVjDsOwjAQBe_iGln-JHZMSc8Zol3vLg4gR4qTCnF3iJQC2jcz76VG2NYybo2XcSJ1VladfjeE_OC6A7pDvc06z3VdJtS7og_a9HUmfl4O9--gQCvfOmPXxWAxJQrZp5BTLy5KR4Mz4ikYg56JxRob7TAIiweAHl1kQnJWvT_lhzhi:1qBi0V:DGbIEV79qp-eCnhquGY5IMCD27aUxLhMqd87Uic-AX4', '2023-07-04 20:31:19.749136');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `localidad`
--

CREATE TABLE `localidad` (
  `id` bigint(20) NOT NULL,
  `localidad` varchar(255) NOT NULL,
  `id_provincia_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `localidad`
--

INSERT INTO `localidad` (`id`, `localidad`, `id_provincia_id`) VALUES
(1, 'Mar del Plata', 1),
(2, 'Cordoba', 2),
(3, 'Colon', 3),
(4, 'salta', 5),
(5, 'jujuy', 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente`
--

CREATE TABLE `paciente` (
  `user_ptr_id` bigint(20) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `localidad` varchar(255) NOT NULL,
  `provincia` varchar(255) NOT NULL,
  `sexo` varchar(9) NOT NULL,
  `dni` int(10) UNSIGNED NOT NULL CHECK (`dni` >= 0),
  `suscripto` tinyint(1) NOT NULL,
  `planactual_id` bigint(20) DEFAULT NULL,
  `terapiapaciente_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `paciente`
--

INSERT INTO `paciente` (`user_ptr_id`, `lastname`, `localidad`, `provincia`, `sexo`, `dni`, `suscripto`, `planactual_id`, `terapiapaciente_id`) VALUES
(2, 'Guazzetti', 'Mar del Plata', 'Buenos Aires', 'masculino', 11222333, 1, 1, 2),
(4, 'feliz', 'Mar del Plata', 'Buenos Aires', 'masculino', 66555321, 1, 3, 1),
(6, 'tres', 'Buenos Aires', 'Mar del plata', 'masculino', 13456987, 1, 1, 1),
(7, 'sanchez', '1', '1', 'masculino', 16777890, 0, NULL, 2),
(8, 'Teruel', '1', '1', 'fmenino', 32443765, 0, NULL, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `plan`
--

CREATE TABLE `plan` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `precio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `plan`
--

INSERT INTO `plan` (`id`, `nombre`, `precio`) VALUES
(1, '4 consultas', 20000),
(2, '8 consultas', 35000),
(3, 'Acceso Total', 45000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesional`
--

CREATE TABLE `profesional` (
  `user_ptr_id` bigint(20) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `localidad` varchar(255) NOT NULL,
  `provincia` varchar(255) NOT NULL,
  `sexo` varchar(9) NOT NULL,
  `dni` int(10) UNSIGNED NOT NULL CHECK (`dni` >= 0),
  `matricula` bigint(20) NOT NULL,
  `terapiaprofesional_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `profesional`
--

INSERT INTO `profesional` (`user_ptr_id`, `lastname`, `localidad`, `provincia`, `sexo`, `dni`, `matricula`, `terapiaprofesional_id`) VALUES
(3, 'Uno', 'Buenos Aires', 'Mar del plata', 'masculino', 22555444, 555666, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `provincias`
--

CREATE TABLE `provincias` (
  `id` bigint(20) NOT NULL,
  `provincia` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `provincias`
--

INSERT INTO `provincias` (`id`, `provincia`) VALUES
(1, 'Buenos Aires'),
(2, 'Cordoba'),
(3, 'Entre Rios'),
(4, 'Tucuman'),
(5, 'Salta'),
(6, 'Jujuy');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `terapia`
--

CREATE TABLE `terapia` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `terapia`
--

INSERT INTO `terapia` (`id`, `nombre`) VALUES
(2, 'Invididual'),
(1, 'Pareja'),
(3, 'Psicoanalisis');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `core_user`
--
ALTER TABLE `core_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `core_user_groups`
--
ALTER TABLE `core_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `core_user_groups_user_id_group_id_c82fcad1_uniq` (`user_id`,`group_id`),
  ADD KEY `core_user_groups_group_id_fe8c697f_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `core_user_user_permissions`
--
ALTER TABLE `core_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `core_user_user_permissions_user_id_permission_id_73ea0daa_uniq` (`user_id`,`permission_id`),
  ADD KEY `core_user_user_permi_permission_id_35ccf601_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_core_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `localidad`
--
ALTER TABLE `localidad`
  ADD PRIMARY KEY (`id`),
  ADD KEY `localidad_id_provincia_id_e19b3c5c_fk_provincias_id` (`id_provincia_id`);

--
-- Indices de la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`user_ptr_id`),
  ADD UNIQUE KEY `dni` (`dni`),
  ADD KEY `paciente_planactual_id_5bd5c564_fk_plan_id` (`planactual_id`),
  ADD KEY `paciente_terapiapaciente_id_e570ff8a_fk_terapia_id` (`terapiapaciente_id`);

--
-- Indices de la tabla `plan`
--
ALTER TABLE `plan`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `profesional`
--
ALTER TABLE `profesional`
  ADD PRIMARY KEY (`user_ptr_id`),
  ADD UNIQUE KEY `dni` (`dni`),
  ADD UNIQUE KEY `matricula` (`matricula`),
  ADD KEY `profesional_terapiaprofesional_id_6a81df67_fk_terapia_id` (`terapiaprofesional_id`);

--
-- Indices de la tabla `provincias`
--
ALTER TABLE `provincias`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `terapia`
--
ALTER TABLE `terapia`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT de la tabla `core_user`
--
ALTER TABLE `core_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `core_user_groups`
--
ALTER TABLE `core_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `core_user_user_permissions`
--
ALTER TABLE `core_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `localidad`
--
ALTER TABLE `localidad`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `plan`
--
ALTER TABLE `plan`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `provincias`
--
ALTER TABLE `provincias`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `terapia`
--
ALTER TABLE `terapia`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `core_user_groups`
--
ALTER TABLE `core_user_groups`
  ADD CONSTRAINT `core_user_groups_group_id_fe8c697f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `core_user_groups_user_id_70b4d9b8_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`);

--
-- Filtros para la tabla `core_user_user_permissions`
--
ALTER TABLE `core_user_user_permissions`
  ADD CONSTRAINT `core_user_user_permi_permission_id_35ccf601_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `core_user_user_permissions_user_id_085123d3_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`);

--
-- Filtros para la tabla `localidad`
--
ALTER TABLE `localidad`
  ADD CONSTRAINT `localidad_id_provincia_id_e19b3c5c_fk_provincias_id` FOREIGN KEY (`id_provincia_id`) REFERENCES `provincias` (`id`);

--
-- Filtros para la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD CONSTRAINT `paciente_planactual_id_5bd5c564_fk_plan_id` FOREIGN KEY (`planactual_id`) REFERENCES `plan` (`id`),
  ADD CONSTRAINT `paciente_terapiapaciente_id_e570ff8a_fk_terapia_id` FOREIGN KEY (`terapiapaciente_id`) REFERENCES `terapia` (`id`),
  ADD CONSTRAINT `paciente_user_ptr_id_cd0c4b98_fk_core_user_id` FOREIGN KEY (`user_ptr_id`) REFERENCES `core_user` (`id`);

--
-- Filtros para la tabla `profesional`
--
ALTER TABLE `profesional`
  ADD CONSTRAINT `profesional_terapiaprofesional_id_6a81df67_fk_terapia_id` FOREIGN KEY (`terapiaprofesional_id`) REFERENCES `terapia` (`id`),
  ADD CONSTRAINT `profesional_user_ptr_id_883fa544_fk_core_user_id` FOREIGN KEY (`user_ptr_id`) REFERENCES `core_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
