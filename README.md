# Status API

API sencilla desarrollada con Flask para simular el estado de un servicio. El proyecto integra Linux, Git/GitHub y Docker.

## Funcionalidades

### GET /health

Devuelve el estado de la aplicación.

Ejemplo:

```json
{
  "status": "ok"
}
```

### GET /info

Devuelve información básica del servicio.

Ejemplo:

```json
{
  "service": "Network Status API",
  "hostname": "server-name",
  "current_time": "2026-10-21 20:00:00"
}
```

### GET /version

Devuelve la versión actual de la API.

Ejemplo:

```json
{
  "version": "1.0"
}
```

---

## Construir la imagen Docker

```bash
docker build -t status-api .
```

---

## Ejecutar el contenedor

```bash
docker run -p 5000:5000 status-api
```

---

## Ejemplos de uso

Consultar estado:

```bash
curl http://localhost:5000/health
```

Consultar información:

```bash
curl http://localhost:5000/info
```

Consultar versión:

```bash
curl http://localhost:5000/version
```

---

## Tecnologías utilizadas

- Python 3.12
- Flask
- Docker
- Git
- GitHub

---

## Autor

Alex Montano
