from subprocess import call
import os
import argparse
from pathlib import Path
import requests

PWD = Path(os.getcwd())

def load_dotenv():
    env_path = Path('.') / '.env'
    print(f"Buscando archivo .env en: {env_path.absolute()}")
    try:
        with open(env_path, 'r') as f:
            for line in f.readlines():
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    if "\"" in value:
                        value = value.replace("\"", "")
                    os.environ[key] = value
    except FileNotFoundError:
        print(f"No se encontró el archivo .env en {env_path.absolute()}")
def last_two_commits_ids():
    cmd = "git log -2 --pretty=format:\"%H\""
    return os.popen(cmd).read().split()

def get_diff_log(commit_id, recent_id):
    cmd = f"git diff {commit_id} {recent_id}"
    return os.popen(cmd).read()

def compile_additional_params(params):
    result = 'Parámetros adicionales:\n\n'
    for key in params:
        result += f"{key}: {params[key]}\n"
    return {
        'text': result
    }

def compile_parts(parts):
    result = ""
    for part in parts['parts']:
        result += part['text']
    return result


def generate(parts):
    if os.environ.get('GEMINI_API_KEY') is None:
        raise Exception('GEMINI_API_KEY is not set, include in an .env file or as an environment variable')
    
    headers = {
        'Content-Type': 'application/json',
    }

    params = {
        'key': os.environ.get('GEMINI_API_KEY'),
    }

    json_data = {
        'contents': [
            {
                "parts": parts
            },
        ],
    }

    response = requests.post(
        'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent',
        params=params,
        headers=headers,
        json=json_data,
    )

    if response.status_code == 200:
        return response.json()['candidates'][0]['content']

    if response.status_code == 400:
        raise Exception(response.json()['error']['message'])
    
    if response.status_code == 403:
        raise Exception('Invalid API key')
    
    if response.status_code != 200:
        raise Exception('An error occurred while calling the API')

def generate_response(git_diff, additional_params):
    parts = []

    parts.append({'text': 'Eres un genio para hacer cambios en el código, pero no tanto para escribir mensajes de commit. Aquí tienes un resumen de los cambios que hiciste en los últimos dos commits:\n\n'})
    parts.append({'text': git_diff})
    parts.append({'text': f'Utiliza emojis, y puede ser el lenguaje de salida {additional_params['Output Language']}, se detallado riguroso y ludico, quiero causar impresión y mucha satisfaccion cuando presente tu trabajo, muchas gracias, <3'})
    parts.append(compile_additional_params(additional_params))

    return compile_parts(generate(parts))

def preprocess_response(response):
    if response.startswith('```'):
        # Quitar la primera y última línea
        response = response.split('\n')[1:-1]
        # Unir las líneas
        response = '\n'.join(response)
    return response

def save_to_file(output, response):
    path = PWD / output
    print("Save path", path.absolute())
    response = preprocess_response(response)
    
    response += f'\n\nEste es un mensaje automatizado creado por AutoGitDiff 🚀\n\n'

    with open(path, 'w') as f:
        f.write(preprocess_response(response))

if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(description='Change the last two commits of a git repository')
    parser.add_argument('-d', '--directory', type=str, help='The directory of the git repository', required=True)
    parser.add_argument('-l', '--language', type=str, help='The language of the commit messages', required=False)
    parser.add_argument('-p', '--prompt', type=str, help='The prompt for the AI', required=False)
    parser.add_argument('-o', '--output', type=str, help='The output file', required=False)

    args = parser.parse_args()
    os.chdir(args.directory)
    commit_ids = last_two_commits_ids()
    

    # Aditional params 
    additional_params = {
        'Output Language': args.language,
        'A wish from an user ': args.prompt
    }

    git_diff = get_diff_log(commit_ids[0], commit_ids[1])
    output = args.output

    response = generate_response(git_diff, additional_params)
    if output:
        save_to_file(output, response)
    else:
        save_to_file('changelog.md', response)
