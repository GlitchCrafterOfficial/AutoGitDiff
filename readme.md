# AutoGitDiff 🚀

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

> Genera mensajes de commit y changelogs inteligentes con IA a partir de tus diferencias de código.

## 📋 Descripción

AutoGitDiff es una herramienta de línea de comandos que utiliza la API de Gemini (Google AI) para analizar las diferencias entre commits en un repositorio Git y generar automáticamente mensajes de commit creativos o archivos changelog detallados.

Cuando trabajas en proyectos donde la documentación de cambios es crucial, AutoGitDiff te ayuda a transformar diferenciales de código en descripciones expresivas y profesionales, ahorrándote tiempo y mejorando la calidad de tus registros de cambios.

## ✨ Características

- Genera changelogs basados en las diferencias entre dos commits
- Personaliza el idioma de salida (inglés, español, etc.)
- Añade prompts personalizados para orientar el tono y estilo del resultado
- Guarda los resultados en archivos markdown
- Compatible con cualquier repositorio Git
- Usa emojis y lenguaje amigable para hacer los changelogs más atractivos

## 🛠️ Requisitos

- Python 3.6 o superior
- Cuenta con acceso a la API de Gemini (Google AI)
- Clave API de Gemini almacenada en un archivo `.env`
- Git instalado en el sistema

## 📦 Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/GlitchCrafterOfficial/AutoGitDiff.git
cd AutoGitDiff
```

2. Instala las dependencias

```bash 
pip instal -r requirements.txt
```

3. Crea un archivo .env en la raiz del proyecto con tu clave de API.

```bash
GEMINI_API_KEY=tu_clave_api_aquí
```

Si no tienes una clave de API deberás generar una totalmente gratis en el siguiente sitio web: https://aistudio.google.com/apikey.

# 📋 Uso

**Ejemplo Básico**: 

```bash
python autogitdiff.py -d /ruta/a/tu/repositorio
```

Con opciones personalizadas:
```
python autogitdiff.py -d /ruta/a/tu/repositorio -l "Español" -p "Estilo formal para cliente empresarial" -o informe_cambios.md
```

Parámetros disponibles

| Parámetro | Descripción |
|----------|------------|
|-d, --directory| Es el directorio del repositorio Git (obligatorio)|
|-l, --langague | Es el idioma para el mensaje generado|
|-p. --prompt | Es el prompt adicional para personalizar el resultado|
|-o, --output | Nombre del archivo de salida (por defecto: changelog.md)|


# 🔧 Tecnologías utilizadas

- Python
- Gemini API (Google AI)
- Git
- Requests (librería HTTP)
- Argparse

# 📝  Ejemplo de salida
El formato de salida típico incluye:

- Título descriptivo del cambio
- Explicación detallada de las modificaciones
- Secciones organizadas por tipo de cambio (añadidos, eliminados, modificados)
- Emojis para mejorar la legibilidad
- Firma de la herramienta que generó el informe

# 🤝  Contribuciones
Las contribuciones son bienvenidas. Para cambios importantes, abra primero un issue para discutir qué le gustaría cambiar.

# 📄 Licencia
Este proyecto está licenciado bajo la Licencia MIT - vea el archivo LICENSE para más detalles.

# ❤️ Apoya mi trabajo

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/H2H2ITQJK)

Desarrollado con ❤️ por @GlitchCrafterOfficial

