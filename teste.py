from flask import Flask, request, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota para executar a análise de dados
@app.route('/analise', methods=['POST'])
def analise():
    # Carregando os dados - exemplo com dados fictícios
    data = {
        'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela'],
        'Idade': [23, 35, 45, 30],
        'Salário': [50000, 60000, 65000, 70000]
    }
    df = pd.DataFrame(data)

    # Realizando uma análise simples - Exemplo: Estatísticas descritivas
    estatisticas = df.describe()

    # Gerando um gráfico - Exemplo: Gráfico de barras do salário
    plt.figure()
    df.plot(kind='bar', x='Nome', y='Salário')
    plt.title('Salário por Nome')
    plt.xlabel('Nome')
    plt.ylabel('Salário')

    # Salvando o gráfico em um objeto bytes
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    # Renderizando o template com os resultados
    return render_template('resultado.html', estatisticas=estatisticas.to_html(), plot_url=plot_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
