from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    github_username = 'juliaNogueiraC'
    response = requests.get(f'https://api.github.com/users/{github_username}/repos')
    all_projects = response.json()

    # Lista de repositórios que você deseja exibir
    selected_repos = ['Analise-de-dados---Projeto-Segmento-Comercial-', 'Projeto-de-Analise-de-Demissoes-e-Ativos', 'AI-Previsoes-mercado-financeiro', 'Monitoramento-de-Chamados-com-Notificacoes-via-API-BOT-Telegram-e-Discord.', 'Analise-de-Dados-de-Motivos-de-Pedido-de-Desligamento', 'Previsao-de-Necessidade-de-Contratacoes', 'Analise-de-Desempenho-de-Funcionarios', 'Analise_de_Rotatividade_de_Funcionarios_Churn_Rate', 'Medical-Data-Visualizer', 'Sea-Level-Predictor', 'Banco-de-Dados-Departamento-Pessoal']  # Substitua pelos nomes dos seus repositórios

    projects = [repo for repo in all_projects if repo['name'] in selected_repos]
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
