# 🌾 FarmTech Solutions - Sistema Agrícola Inteligente (Fase 4)

## 📚 Introdução

Este repositório corresponde à **Fase 4** do projeto da startup fictícia **FarmTech Solutions**, desenvolvido como parte da disciplina de Inteligência Artificial da FIAP.

O projeto evolui a solução criada na Fase 3, implementando recursos avançados de **Data Science aplicada ao agronegócio**, com integração de sensores, predição de irrigação com **Scikit-learn**, visualização em tempo real com **Streamlit**, monitoramento via **Serial Plotter**, display **LCD I2C no Wokwi** e **otimizações de código C++ no ESP32**.

---

## 🎯 Objetivos da Fase 4

- 💡 Aplicar **Machine Learning com Scikit-learn** para prever a necessidade de irrigação;
- 🖥️ Desenvolver um **Dashboard interativo com Streamlit**;
- 📟 Integrar **display LCD via barramento I2C no Wokwi** para exibir métricas em tempo real;
- 📈 Monitorar sensores com **Serial Plotter** no ambiente do ESP32;
- ⚙️ Otimizar o uso de memória no código C/C++ do microcontrolador;
- 🔗 Consolidar e integrar os dados ao banco de dados relacional da FarmTech Solutions;
- 🎥 Documentar e demonstrar via vídeo o funcionamento da solução.

---

## 🛠️ Tecnologias Utilizadas

| Componente       | Descrição                                      |
|------------------|-----------------------------------------------|
| ESP32 + Wokwi    | Simulação de sensores físicos                 |
| Python 3         | Linguagem principal do backend                 |
| Streamlit        | Interface gráfica web para visualização       |
| Scikit-learn     | Biblioteca de aprendizado de máquina           |
| SQLite / MySQL   | Banco de dados relacional                     |
| C/C++            | Lógica embarcada no ESP32                     |
| Serial Plotter   | Monitoramento de sinais dos sensores          |
| GitHub           | Versionamento e documentação                  |

---

## 📦 Estrutura do Repositório

```
sistema-agricola/
│
├── fase4/
│   ├── esp32/
│   │   └── main.cpp         # Código otimizado do ESP32
│   │   └── lcd_display.ino  # Integração com display LCD
│   │
│   ├── python/
│   │   └── streamlit_app.py # Interface interativa
│   │   └── model.pkl        # Modelo preditivo treinado
│   │   └── train_model.py   # Treinamento com Scikit-learn
│   │
│   ├── database/
│   │   └── schema.sql       # Estrutura do banco de dados
│   │   └── insert_data.py   # Inserção e coleta de dados
│
├── imagens/
│   └── serial_plotter.png   # Gráficos do monitoramento
│   └── lcd_print.png        # Display Wokwi em funcionamento
│
├── README.md
└── video_apresentacao.mp4   # Link do vídeo no YouTube
```

---

## 🤖 Modelo de Machine Learning

Utilizamos um modelo de classificação Random Forest, treinado com dados simulados de umidade e nutrientes do solo. O modelo realiza predições sobre a **necessidade de irrigação nas próximas horas** com base em padrões históricos.

> 📁 O modelo está salvo como `model.pkl` e pode ser carregado pelo Streamlit.

---

## 📊 Streamlit – Dashboard Interativo

A interface web foi desenvolvida com Streamlit, permitindo:
- Visualização dos dados dos sensores;
- Gráficos de histórico e predições;
- Integração com banco de dados para exibição de registros anteriores;
- Interface amigável para agricultores.

> 🎯 Execute com: `streamlit run streamlit_app.py`

---

## 🖥️ Integração com LCD no Wokwi

- Display LCD 16x2 integrado via barramento I2C (pinos SDA/SCL);
- Exibe em tempo real:
  - Umidade do solo
  - Nível de nutrientes
  - Status da irrigação

📷 Imagem da simulação:

![Display LCD no Wokwi](imagens/lcd_print.png)

---

## 📈 Monitoramento via Serial Plotter

Implementado monitoramento gráfico da variável de umidade em tempo real no ambiente do ESP32:

![Serial Plotter](imagens/serial_plotter.png)

---

## ⚙️ Otimização no ESP32

- Tipos de dados ajustados: uso de `uint8_t` e `float` apenas quando necessário;
- Redução de variáveis globais;
- Comentários no código justificando otimizações.

📂 Código principal: `fase4/esp32/main.cpp`

---

## 🧠 Banco de Dados

- Estrutura otimizada com tabelas para sensores, eventos de irrigação e logs;
- Armazenamento de dados históricos para uso no modelo de ML;
- Scripts disponíveis em `fase4/database/`.



## 👨‍💻 Integrantes do Grupo – 1TIAO

| Nome Completo                                   | RM       |
| ----------------------------------------------- | -------- |
| Matheus Parra                                   | RM561907 |
| Otavio Custodio de Oliveira                     | RM565606 |
| Tiago Alves Cordeiro (líder do repositório)     | RM561791 |
| Thiago Henrique Pereira de Almeida Santos       | RM563327 |
| Leandro Arthur Marinho Ferreira                 | RM565240 |

---

## ✅ Conclusão

A **Fase 4** da FarmTech Solutions marca um salto em inteligência, eficiência e usabilidade, demonstrando como a integração entre sensores, algoritmos de IA, banco de dados e interfaces pode revolucionar a agricultura de precisão.

Este projeto é um passo concreto em direção à **transformação digital no campo**, aliando tecnologia à sustentabilidade e produtividade.

---

## 📌 Requisitos para Execução

- Python 3.9+
- Scikit-learn
- Streamlit
- SQLite ou MySQL
- Simulador Wokwi

---

## 📝 Licença

Projeto acadêmico sob licença MIT. Uso restrito à FIAP e fins educacionais.
