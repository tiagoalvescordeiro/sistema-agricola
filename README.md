# 🌱 Sistema de Irrigação Inteligente - Entrega 1

## 🔧 Visão Geral

Este projeto simula um sistema inteligente de irrigação usando ESP32, sensores analógicos e digitais, com controle automático da bomba d'água.

## 🧩 Componentes Simulados no Wokwi

| Função | Componente | Pino ESP32 |
|--------|------------|-------------|
| Sensor de Fósforo (P) | Botão       | GPIO 22 |
| Sensor de Potássio (K) | Botão       | GPIO 23 |
| Sensor de pH          | LDR | GPIO 34 |
| Sensor de Umidade     | DHT22       | GPIO 14 |
| Bomba de Irrigação    | LED + relé | GPIO 12 |

## ⚙️ Lógica de Funcionamento

A bomba de irrigação é ativada **quando qualquer** uma das seguintes condições for detectada:

- Umidade do solo < 30%
- Ausência de fósforo (botão de fósforo solto)
- Ausência de potássio (botão de potássio solto)
- pH fora da faixa ideal (5.5 a 7.5)



if (umidade < 30 || !fosforo || !potassio || ph < 5.5 || ph > 7.5) {
  digitalWrite(RELE_PIN, HIGH); // Liga a bomba
} else {
  digitalWrite(RELE_PIN, LOW);  // Desliga a bomba
}

## 🎥 Simulação do Circuito

![Simulação do sistema](./simulacao.gif)
