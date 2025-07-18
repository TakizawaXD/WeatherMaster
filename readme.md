# WeatherMaster – Sistema de Clima en Tiempo Real

## 📌 Descripción General

**WeatherMaster** es una solución de backend desarrollada con **FastAPI** que proporciona información detallada del clima actual, sensación térmica y pronósticos futuros. Su enfoque está en la eficiencia, escalabilidad y compatibilidad multiplataforma mediante API REST. Utiliza **MySQL** como base de datos relacional y está contenida para entornos locales mediante **Docker** y **Docker Compose**. El despliegue en producción se realiza sobre la capa gratuita de **Amazon Web Services (AWS)**.

---

## 🎯 Propósito del Proyecto

- Consultar el clima actual, sensación térmica y pronóstico.
- Consultar por ciudad, localidad o coordenadas (mapa).
- Usar desde navegador web o aplicación móvil vía web.
- Brindar información en tiempo real desde cualquier parte del mundo.

---

## 👥 Público Objetivo

- **Usuarios finales** que desean consultar el clima desde cualquier dispositivo.
- **Desarrolladores** que necesiten integrar datos climáticos en sus plataformas.
- **Empresas** que requieren visualizar o analizar información meteorológica.

---

## 🛠️ Tecnologías Utilizadas

| Componente        | Tecnología     |
|-------------------|----------------|
| Backend API       | FastAPI        |
| Base de Datos     | MySQL          |
| Contenedores      | Docker + Compose |
| Despliegue Cloud  | AWS (EC2/Elastic Beanstalk) |
| Comunicación API  | REST + JSON    |

---

## 🗂️ Diagrama de la estructura del Proyecto

![Diagrama de la estructura del Proyecto](/img/clime.png)