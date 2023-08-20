-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-08-2023 a las 20:17:19
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bdmedq`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `citas`
--

CREATE TABLE `citas` (
  `folio` int(11) NOT NULL,
  `id_paciente` int(11) DEFAULT NULL,
  `id_doctor` int(11) DEFAULT NULL,
  `fecha_agendada` date DEFAULT NULL,
  `id_consultorio` int(11) DEFAULT NULL,
  `hora_cita` varchar(50) DEFAULT NULL,
  `estatus` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `citas`
--

INSERT INTO `citas` (`folio`, `id_paciente`, `id_doctor`, `fecha_agendada`, `id_consultorio`, `hora_cita`, `estatus`) VALUES
(4567, 1, 1, '2013-12-12', 1, '14:15:13', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consultas`
--

CREATE TABLE `consultas` (
  `id` int(11) NOT NULL,
  `id_paciente` int(11) DEFAULT NULL,
  `id_doctor` int(11) DEFAULT 3,
  `id_zona` int(11) DEFAULT NULL,
  `sintomas` varchar(200) DEFAULT NULL,
  `tipo_dolor` varchar(100) DEFAULT NULL,
  `nivel_dolor` int(11) DEFAULT NULL,
  `fecha_consulta` date DEFAULT NULL,
  `alergias` varchar(200) DEFAULT NULL,
  `antecedentes` varchar(200) DEFAULT NULL,
  `Hora` time DEFAULT NULL,
  `estatus` int(11) DEFAULT NULL,
  `diagnostico` varchar(10000) DEFAULT NULL,
  `medicoVerifica` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `consultas`
--

INSERT INTO `consultas` (`id`, `id_paciente`, `id_doctor`, `id_zona`, `sintomas`, `tipo_dolor`, `nivel_dolor`, `fecha_consulta`, `alergias`, `antecedentes`, `Hora`, `estatus`, `diagnostico`, `medicoVerifica`) VALUES
(1, 1, 1, 1, 'Dolor de cabeza', 'Punzante', 5, '2023-12-12', 'N/A', 'NA', '16:10:12', 1, NULL, NULL),
(2, 1, 1, 1, 'Dolor de cabeza', 'Punzante', 5, '2023-12-12', 'N/A', 'NA', '15:15:10', 0, NULL, NULL),
(3, 2, 1, 1, 'Dolor de cabeza', 'Punzante', 5, '2023-12-12', 'N/A', 'NA', '15:15:10', 1, NULL, NULL),
(4, 1, 2, 1, 'Jaqueca', '', 5, '2023-08-09', 'NA', 'NA', '20:26:00', 1, NULL, NULL),
(5, 1, 3, 3, 'abcd', '', 4, '2023-08-03', 'abcd', 'abcd', '21:52:00', 1, NULL, NULL),
(8, 1, 3, 12, 'jajaja', '', 9, '2023-08-23', 'jajaja', 'jajaja', '20:56:00', 1, NULL, NULL),
(9, 1, 3, 12, 'hello', '', 10, '2023-08-11', 'soy', 'Edgar', '22:06:00', 1, NULL, NULL),
(12, NULL, 3, 1, 'Jaqueca. Dolor de cabeza.', 'Punzante', 3, '2023-08-20', 'Abejas', 'Ninguno', '17:00:00', 1, 'Basado en los síntomas que mencionas, es posible que estés experimentando una migraña. La migraña se caracteriza por un dolor de cabeza intenso y punzante, generalmente en un lado de la cabeza. Además, es común que las personas con migraña experimenten sensibilidad a la luz, náuseas y vómitos.\n\nDado que tu nivel de dolor es de 3 de 10, te recomendaría tomar medidas para aliviar el dolor en casa. Puedes intentar descansar en una habitación oscura y tranquila, aplicar compresas frías o calientes en la zona afectada, y tomar analgésicos de venta libre como el paracetamol o el ibuprofeno, siempre siguiendo las instrucciones del envase.\n\nSi los síntomas persisten o empeoran, te sugiero que consultes a un médico para una evaluación más detallada. Recuerda que solo un médico real puede proporcionar un diagnóstico preciso y recomendaciones específicas para tu situación.', NULL),
(13, NULL, 3, 1, 'Jaqueca. Dolor de cabeza.', 'Punzante', 3, '2023-08-20', 'Abejas', 'Ninguno', '17:00:00', 1, 'Basado en los síntomas que mencionas, es posible que estés experimentando una migraña. La migraña se caracteriza por un dolor de cabeza intenso y punzante, generalmente en un lado de la cabeza. Además, es común que las personas con migraña experimenten sensibilidad a la luz, náuseas y vómitos.\n\nDado que tu nivel de dolor es de 3 de 10, te recomendaría tomar medidas para aliviar el dolor en casa. Puedes intentar descansar en una habitación oscura y tranquila, aplicar compresas frías o calientes en la zona afectada, y tomar analgésicos de venta libre como el paracetamol o el ibuprofeno, siempre siguiendo las instrucciones del envase.\n\nSin embargo, es importante que consultes a un médico para obtener un diagnóstico preciso y un tratamiento adecuado. Un médico podrá evaluar tus síntomas, realizar un examen físico y, si es necesario, solicitar pruebas adicionales para descartar otras posibles causas de tu dolor de cabeza.\n\nRecuerda que esta respuesta es solo con fines informativos y no reemplaza la consulta médica. Si tus síntomas empeoran o persisten, te recomendaría buscar atención médica profesional.', NULL),
(14, NULL, 3, 1, 'Jaqueca. Dolor de cabeza.', 'Punzante', 3, '2023-08-20', 'Abejas', 'Ninguno', '17:00:00', 1, 'Basado en los síntomas que mencionas, es posible que estés experimentando una migraña. La migraña se caracteriza por un dolor de cabeza intenso y punzante, generalmente en un lado de la cabeza. Además, es común que las personas con migraña experimenten sensibilidad a la luz, náuseas y vómitos.\n\nDado que mencionas que tu nivel de dolor es de 3 de 10, esto indica que el dolor no es extremadamente intenso. En este caso, te recomendaría tomar medidas para aliviar el dolor en casa. Puedes intentar descansar en una habitación oscura y tranquila, aplicar compresas frías o calientes en la zona afectada, y tomar analgésicos de venta libre como el paracetamol o ibuprofeno, siempre siguiendo las instrucciones del envase.\n\nSin embargo, es importante tener en cuenta que esta recomendación se basa en la información proporcionada y no reemplaza una evaluación médica adecuada. Si los síntomas persisten o empeoran, te recomendaría buscar atención médica para una evaluación más completa y un diagnóstico preciso.', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consultorios`
--

CREATE TABLE `consultorios` (
  `id` int(11) NOT NULL,
  `descripcion` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `consultorios`
--

INSERT INTO `consultorios` (`id`, `descripcion`) VALUES
(1, 'Nuevo Consul');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estatus`
--

CREATE TABLE `estatus` (
  `id` int(11) NOT NULL,
  `descripcion` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estatus`
--

INSERT INTO `estatus` (`id`, `descripcion`) VALUES
(1, 'Administrador'),
(2, 'Medico'),
(3, 'Paciente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `generos`
--

CREATE TABLE `generos` (
  `id` int(11) NOT NULL,
  `descripcion` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `generos`
--

INSERT INTO `generos` (`id`, `descripcion`) VALUES
(1, 'hombre'),
(2, 'Mujer'),
(3, 'Otro');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medicos`
--

CREATE TABLE `medicos` (
  `id` int(11) NOT NULL,
  `id_persona` int(11) DEFAULT NULL,
  `cedula` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `medicos`
--

INSERT INTO `medicos` (`id`, `id_persona`, `cedula`) VALUES
(1, 2, 'soyunaCedula'),
(2, 3, 'soyunaCedulaqueexplorta'),
(3, 6, 'En proceso');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
--

CREATE TABLE `pacientes` (
  `id` int(11) NOT NULL,
  `id_persona` int(11) DEFAULT NULL,
  `nss` varchar(50) DEFAULT NULL,
  `estatura` decimal(5,2) DEFAULT NULL,
  `peso` int(11) DEFAULT NULL,
  `temperatura` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pacientes`
--

INSERT INTO `pacientes` (`id`, `id_persona`, `nss`, `estatura`, `peso`, `temperatura`) VALUES
(1, 5, '456789', '1.70', 70, '35.20'),
(2, 4, '456789', '1.70', 70, '35.20');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personas`
--

CREATE TABLE `personas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `ap` varchar(100) DEFAULT NULL,
  `am` varchar(100) DEFAULT NULL,
  `id_genero` int(11) DEFAULT NULL,
  `fecha_nac` date DEFAULT NULL,
  `telefono` varchar(100) DEFAULT NULL,
  `id_estatus` int(11) DEFAULT NULL,
  `correo` varchar(100) DEFAULT NULL,
  `contra` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `personas`
--

INSERT INTO `personas` (`id`, `nombre`, `ap`, `am`, `id_genero`, `fecha_nac`, `telefono`, `id_estatus`, `correo`, `contra`) VALUES
(1, 'Edgar', 'Escobedo', 'Zuñiga', 1, '2000-11-30', '44245678', 1, 'correo@gmail.com', '123456'),
(2, 'Isaac', 'Escobedo', 'Zuñiga', 1, '2000-11-30', '44245678', 2, '1234@gmail.com', '123456'),
(3, 'Santiago', 'Escobedo', 'Zuñiga', 1, '2000-11-30', '44245678', 3, 'abcd@gmail.com', '123456'),
(4, 'Jimena', 'Escobedo', 'Zuñiga', 1, '2000-11-30', '44245678', 3, 'jimena@gmail.com', '123456'),
(5, 'Elias', 'Jimenez', 'Roberto', 2, '2023-10-13', '4420987654', 3, 'elias@gmail.com', '123456'),
(6, 'En', 'Proceso', '.', 3, '2000-11-30', '99999999', 3, 'proceso@gmail.com', '123456'),
(7, 'María', 'Gonzalez', 'Márquez', 2, '2003-02-12', '98765423', 3, 'maria@gmail.com', '123456');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `zonacuerpos`
--

CREATE TABLE `zonacuerpos` (
  `id` int(11) NOT NULL,
  `descripcion` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `zonacuerpos`
--

INSERT INTO `zonacuerpos` (`id`, `descripcion`) VALUES
(1, 'Cabeza'),
(2, 'Cuello'),
(3, 'Pecho'),
(4, 'Brazo'),
(5, 'Antebrazo'),
(6, 'Mano'),
(7, 'Abdomen'),
(8, 'Pelvis'),
(9, 'Muslo'),
(10, 'Gluteo'),
(11, 'Pierna'),
(12, 'Pie'),
(13, 'Cabeza'),
(14, 'Cuello'),
(15, 'Pecho'),
(16, 'Brazo'),
(17, 'Antebrazo'),
(18, 'Mano'),
(19, 'Abdomen'),
(20, 'Pelvis'),
(21, 'Muslo'),
(22, 'Gluteo'),
(23, 'Pierna'),
(24, 'Pie');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `citas`
--
ALTER TABLE `citas`
  ADD PRIMARY KEY (`folio`),
  ADD KEY `id_paciente` (`id_paciente`),
  ADD KEY `id_doctor` (`id_doctor`),
  ADD KEY `id_consultorio` (`id_consultorio`);

--
-- Indices de la tabla `consultas`
--
ALTER TABLE `consultas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_paciente` (`id_paciente`),
  ADD KEY `id_doctor` (`id_doctor`),
  ADD KEY `id_zona` (`id_zona`),
  ADD KEY `medicoVerifica` (`medicoVerifica`);

--
-- Indices de la tabla `consultorios`
--
ALTER TABLE `consultorios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `estatus`
--
ALTER TABLE `estatus`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `generos`
--
ALTER TABLE `generos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `medicos`
--
ALTER TABLE `medicos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_persona` (`id_persona`);

--
-- Indices de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_persona` (`id_persona`);

--
-- Indices de la tabla `personas`
--
ALTER TABLE `personas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_genero` (`id_genero`),
  ADD KEY `id_estatus` (`id_estatus`);

--
-- Indices de la tabla `zonacuerpos`
--
ALTER TABLE `zonacuerpos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `citas`
--
ALTER TABLE `citas`
  MODIFY `folio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4568;

--
-- AUTO_INCREMENT de la tabla `consultas`
--
ALTER TABLE `consultas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `consultorios`
--
ALTER TABLE `consultorios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `estatus`
--
ALTER TABLE `estatus`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `generos`
--
ALTER TABLE `generos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `medicos`
--
ALTER TABLE `medicos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `personas`
--
ALTER TABLE `personas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `zonacuerpos`
--
ALTER TABLE `zonacuerpos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `citas`
--
ALTER TABLE `citas`
  ADD CONSTRAINT `citas_ibfk_1` FOREIGN KEY (`id_paciente`) REFERENCES `pacientes` (`id`),
  ADD CONSTRAINT `citas_ibfk_2` FOREIGN KEY (`id_doctor`) REFERENCES `medicos` (`id`),
  ADD CONSTRAINT `citas_ibfk_3` FOREIGN KEY (`id_consultorio`) REFERENCES `consultorios` (`id`);

--
-- Filtros para la tabla `consultas`
--
ALTER TABLE `consultas`
  ADD CONSTRAINT `consultas_ibfk_1` FOREIGN KEY (`id_paciente`) REFERENCES `pacientes` (`id`),
  ADD CONSTRAINT `consultas_ibfk_2` FOREIGN KEY (`id_doctor`) REFERENCES `medicos` (`id`),
  ADD CONSTRAINT `consultas_ibfk_3` FOREIGN KEY (`id_zona`) REFERENCES `zonacuerpos` (`id`),
  ADD CONSTRAINT `consultas_ibfk_4` FOREIGN KEY (`medicoVerifica`) REFERENCES `medicos` (`id`);

--
-- Filtros para la tabla `medicos`
--
ALTER TABLE `medicos`
  ADD CONSTRAINT `medicos_ibfk_1` FOREIGN KEY (`id_persona`) REFERENCES `personas` (`id`);

--
-- Filtros para la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD CONSTRAINT `pacientes_ibfk_1` FOREIGN KEY (`id_persona`) REFERENCES `personas` (`id`);

--
-- Filtros para la tabla `personas`
--
ALTER TABLE `personas`
  ADD CONSTRAINT `personas_ibfk_1` FOREIGN KEY (`id_genero`) REFERENCES `generos` (`id`),
  ADD CONSTRAINT `personas_ibfk_2` FOREIGN KEY (`id_estatus`) REFERENCES `estatus` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
