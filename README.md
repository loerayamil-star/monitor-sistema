# Monitor de Sistema en Tiempo Real

Monitor de recursos del sistema desarrollado en Python con interfaz gráfica. Muestra el uso de CPU, RAM y disco con barras de progreso y colores que cambian según el nivel de uso.

## Descripción

Aplicación de escritorio que permite visualizar en tiempo real el estado de los recursos del sistema. Cada métrica se actualiza automáticamente cada segundo y cambia de color según el nivel de uso para facilitar la lectura rápida del estado del equipo.

## Funcionalidades

- **CPU**: porcentaje de uso en tiempo real
- **RAM**: porcentaje y GB usados / disponibles
- **Disco**: porcentaje y GB usados / disponibles
- Actualización automática cada segundo
- Colores indicadores:
  - Verde: uso normal (0–60%)
  - Amarillo: uso moderado (60–80%)
  - Rojo: uso elevado (80–100%)
- Barras de progreso visuales para cada recurso

## Tecnologías

- Python 3
- Tkinter (interfaz gráfica)
- psutil (lectura de recursos del sistema)
- POO — Programación Orientada a Objetos (clases)

## Requisitos

- Python 3.x instalado
- Instalar dependencia:

```bash
pip install psutil
```

## Cómo ejecutar

```bash
python monitor.py
```

## Nota

Proyecto educativo desarrollado como primer acercamiento al uso de clases y Programación Orientada a Objetos en Python.
