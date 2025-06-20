# 🚜 Projeto Hermes Reply IoT Failures – Fase 4 (FIAP 2025.1 – 1TIAO)
[![Atualizar Docs e Deps](https://github.com/tiagoalvescordeiro/hermes_reply_iot_fase4_codex/actions/workflows/auto-update.yml/badge.svg)](https://github.com/tiagoalvescordeiro/hermes_reply_iot_fase4_codex/actions)


Sistema inteligente de irrigação baseado em IoT e Machine Learning, utilizando ESP32, sensores virtuais, modelo preditivo com Scikit-learn, interface com Streamlit e dashboard em tempo real. Este projeto é a continuação da Fase 3 da FarmTech Solutions, agora com foco em otimização, visualização e automação.

---

## 📌 Visão Geral

Nesta fase, aprimoramos a aplicação integrando:

- ✅ Predição de falha de sensores com **Scikit-learn**
- ✅ Interface interativa com **Streamlit**
- ✅ Hardware simulado com **ESP32 + Display LCD (I2C)**
- ✅ Gráfico em tempo real com **Serial Plotter**
- ✅ Banco de dados relacional e estrutura de dados em arquivos
- ✅ **Pipeline de automação no GitHub Actions**

---

## 🧠 Inteligência Artificial com Scikit-learn

- Modelo: `RandomForestClassifier`
- Features: temperatura, vibração (x, y, z), umidade
- Output: probabilidade de falha
- Treinamento feito localmente com dados simulados
- Código disponível em `scripts/modelo.py`

---

## 📊 Interface com Streamlit

A interface do usuário está localizada em `streamlit-app/app.py`. Execute com:

```bash
cd streamlit-app
streamlit run app.py
A aplicação coleta valores de sensores e retorna a probabilidade de falha com base no modelo treinado.

🧪 API Flask (opcional)
Disponível em api-flask/, permite chamadas REST para a predição, podendo ser integrada com outras aplicações, sensores físicos ou interfaces.

💡 Simulação no Wokwi com ESP32
Utilizamos ESP32 simulando sensores de umidade e nutrientes

Exibição de dados em LCD 16x2 com barramento I2C

Gráficos em tempo real via Serial Plotter

Código otimizado em C++ disponível em hardware/fase4.ino

🔧 Otimizações no Código do ESP32
Tipos de dados ajustados para economia de memória (int8_t, float, const)

Variáveis globais revisadas

Comentários incluídos justificando otimizações

🖼️ Imagens do Wokwi
Display LCD com dados do sensor


Serial Plotter com gráfico de umidade


🧩 Banco de Dados e Estrutura
Estrutura relacional armazenada em database/

Scripts SQL ou estrutura em CSV/JSON

Utilizado para armazenar histórico das leituras e falhas

🎬 Demonstração em Vídeo
📺 Clique aqui para assistir ao vídeo no YouTube (modo não listado)

🛠️ Execução da Pipeline (CI/CD)
O projeto conta com uma automação via GitHub Actions, responsável por:

Atualizar automaticamente o requirements.txt

Committar e dar push nas dependências

Rastrear mudanças em arquivos .py, .md e .txt

📁 Estrutura do Repositório
bash
Copiar
Editar
├── api-flask/               # Backend com Flask
├── hardware/                # Código otimizado ESP32 + LCD
│   ├── fase4.ino
│   └── prints_lcd/
├── scripts/                 # Código Python com Scikit-learn
├── streamlit-app/           # Interface interativa com Streamlit
│   ├── app.py
│   └── requirements.txt
├── .github/workflows/       # CI/CD com GitHub Actions
│   └── auto-update.yml
├── README.md
└── package.json             # Dependências auxiliares

## 👨‍💻 Integrantes do Grupo – 1TIAO

| Nome Completo                                   | RM       |
| ----------------------------------------------- | -------- |
| Matheus Parra                                   | RM561907 |
| Otavio Custodio de Oliveira                     | RM565606 |
| Tiago Alves Cordeiro (líder do repositório)     | RM561791 |
| Thiago Henrique Pereira de Almeida Santos       | RM563327 |
| Leandro Arthur Marinho Ferreira                 | RM565240 |


Projeto desenvolvido para a disciplina Inteligência Artificial Aplicada
FIAP – Fase 4 – 2025.1

💬 Contato
Dúvidas ou sugestões? Entre em contato conosco por GitHub.