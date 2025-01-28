# Practica_Final_Cristian
## Monitorización de Recursos del Sistema en Python

Este proyecto proporciona una herramienta para monitorear en tiempo real el uso de la CPU, la memoria RAM y el disco en tu sistema. Está diseñado para ejecutarse en un entorno Python y puede ser extendido para integrarse con herramientas de visualización como **Grafana** y **Prometheus** para crear paneles gráficos y obtener métricas en tiempo real.

## Requisitos

- Python 3.x
- Paquete `psutil` para monitoreo de recursos del sistema
- (Opcional) **Prometheus** y **Grafana** para visualización avanzada de métricas

## Instalación

1. **Clonar o descargar el proyecto:**
   
   Puedes clonar este repositorio o descargar el archivo `.py` del proyecto a tu máquina.

2. **Instalar las dependencias necesarias:**

   El proyecto depende del paquete `psutil`, que puedes instalar usando `pip`:

   ```bash
   pip install psutil

