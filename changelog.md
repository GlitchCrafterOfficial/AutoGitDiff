**Refactorización de la configuración de archivos estáticos y corrección de URL de medios**

*   **Resumen:**
    *   Se ha optimizado la configuración de archivos estáticos para mejorar la gestión y el despliegue de la aplicación.
    *   Se ha corregido la URL de los archivos multimedia para asegurar el correcto acceso y visualización de estos recursos.
    *   Se eliminaron archivos obsoletos y migraciones innecesarias.

*   **Detalles:**
    *   La configuración de `STATICFILES_DIRS` en `settings.py` ha sido modificada para apuntar directamente a la carpeta `backend/static`, eliminando la redundancia y posibles conflictos en la resolución de archivos estáticos.
    *   Se ha corregido un problema en `urls.py` que podría haber afectado la correcta visualización de los archivos multimedia alojados en la aplicación.
    *   Se elimina un archivo PDF del sistema.

**Refactorización y Simplificación de Modelos de Formulario**

*   **Resumen:**
    *   Se ha simplificado la estructura de los modelos de formulario para mejorar la eficiencia y la mantenibilidad del código.
    *   Se eliminó información redundante de los modelos.
    *   Se corrigieron errores de validación en los campos RUT y Teléfono, haciendo los campos rut y telefono configurables desde el form.

*   **Detalles:**
    *   Los modelos `AreaOperacional`, `AreaGestionVial` y `AreaSSO` en `forms/models.py` han sido refactorizados para eliminar campos redundantes como `numero_de_reporte`, `fecha_de_ingreso`, `estado_del_reporte`, `tipo_de_reporte` y `frecuencia`. Esta simplificación reduce la complejidad del modelo y facilita su gestión.
    *   Se eliminó el modelo Actividad dado que su relacion ya no se necesita en el modelo actual.
    *   Se actualizó el modelo Participantes para que sea más configurable y con los atributos Rut, Telefono, correo, nombre, apellido paterno y vinculo.
    *   Se modificó el endpoint de los forms a `create-form`.


Este es un mensaje automatizado creado por AutoGitDiff 🚀

