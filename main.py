import os

import requests
from flask import Flask, render_template

app = Flask(__name__)
my_secret = os.environ['token']

@app.route('/')
def index():
    github_token = os.getenv('token')
    headers = {'Authorization': f'token {github_token}'}

    # Lista de URLs dos repositórios que você deseja exibir
    selected_repos_urls = [
        'https://github.com/juliaNogueiraC/Meu-Portfolio-em-Flask',
        'https://github.com/juliaNogueiraC/Analise-de-dados---Projeto-Segmento-Comercial-', 
        'https://github.com/juliaNogueiraC/Projeto-de-Analise-de-Demissoes-e-Ativos', 
        'https://github.com/juliaNogueiraC/AI-Previsoes-mercado-financeiro', 
        'https://github.com/juliaNogueiraC/Analise-de-Dados-de-Motivos-de-Pedido-de-Desligamento', 
        'https://github.com/juliaNogueiraC/Previsao-de-Necessidade-de-Contratacoes', 
        'https://github.com/juliaNogueiraC/Analise-de-Desempenho-de-Funcionarios',                 
        'https://github.com/juliaNogueiraC/Analise_de_Rotatividade_de_Funcionarios_Churn_Rate', 
        'https://github.com/juliaNogueiraC/Medical-Data-Visualizer', 
        'https://github.com/juliaNogueiraC/Sea-Level-Predictor', 
        'https://github.com/juliaNogueiraC/Banco-de-Dados-Departamento-Pessoal'
    ]

    projects = []

    for repo_url in selected_repos_urls:
        repo_name = repo_url.split('/')[-1]
        response = requests.get(f'https://api.github.com/repos/juliaNogueiraC/{repo_name}', headers=headers)
        if response.status_code == 200:
            projects.append(response.json())
        else:
            print(f'Erro ao obter o repositório: {repo_name}, Status Code: {response.status_code}')

    return render_template('index.html', projects=projects)

@app.route('/contact')
def about():
    return render_template('contact.html')

@app.route('/')
def home():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
