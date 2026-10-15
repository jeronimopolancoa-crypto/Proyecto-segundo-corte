# QuickDrop Logistics - Sistema Local de Mensajería (Problema 11)

**Asignatura:** Programación (G02) - Proyecto 2  
**Docente:** Breyner Posso Bautista  
**Integrantes (Grupo 4):**
* Sebastián Triviño Lucumi
* Emmanuel Payan Rivera
* Jerónimo Polanco Andrade

**Repositorio GitHub:** https://github.com/jeronimopolancoa-crypto/Proyecto-segundo-corte/upload/main

# Estructura del Proyecto
 `cliente.py`: Clase `Cliente` con atributos encapsulados y actualización de contacto.
 `repartidor.py`: Clase `Repartidor` con atributos encapsulados y validación de vehículo (`Moto`, `Bicicleta`, `Carro`).
* `domicilio.py`: Clase asociativa `Domicilio` con control de estados inmutables (`ACTIVO` -> `FINALIZADO` / `CANCELADO`).
* `gestion.py`: Funciones de gestión CRUD, cálculo dinámico de disponibilidad y persistencia en JSON.
* `main.py`: Interfaz de usuario por consola de comandos.
* `interfaz_mensajeria.py`: Interfaz gráfica de usuario con Tkinter que reutiliza `gestion.py`.
* `datos_mensajeria.json`: Archivo de persistencia con al menos 5 registros de prueba por colección.

# Dependencias
* Python 3.x (utiliza únicamente librerías estándar incluidas en Python: `json`, `datetime`, `tkinter`). No requiere instalar paquetes externos con `pip`.

# Instrucciones de Ejecución

1. Ubíquese en la carpeta raíz del proyecto desde la terminal.
2. **Para ejecutar la versión de Consola:**
   ```bash
   python main.py
   ```
3. **Para ejecutar la versión Gráfica:**
   ```bash
   python interfaz_mensajeria.py