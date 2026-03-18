# TODO - PROJETO FASE 5 MACHINE LEARNING NA CABEÇA


## 🎯 ENTREGA 1 — OBJETIVO:

Analisar uma base de dados com informações de condições de solo e temperatura, relacionadas com o tipo de produto agrícola de uma fazenda. Deverá ser feito uma previsão do rendimento de safra e a exploração da tendência de produtividade.

---

## 💻 O QUE PRECISA SER FEITO:

- ✅ Fazer uma análise exploratória na base para se familiarizar com os dados.

- ✅ Encontrar tendências para os rendimentos das plantações, por meio de clusterizações, e identificar se existem cenários discrepantes (outliers).

- ✅ Fazer cinco modelos preditivos **(cada um com um algoritmo diferente)** que, dadas as condições, prevejam qual será o rendimento da safra. **Necessário seguir as boas práticas dos projetos de Machine Learning, assim como avaliar o modelo com métricas pertinentes ao problema.**

---

## 📋 ENTREGÁVEIS:

- ✅ Link de um novo repositório do GitHub em nome do seu grupo **(de 1 a 5 pessoas)** com:

    - ✅ Upload do link do notebook Jupyter **(será executado na correção)** contendo:

        - ✅ Células de códigos executadas, com o código Python otimizado e com comentários das linhas.
        - ✅ Células de markdown organizando seu relatório e discorrendo textualmente sobre os achados a partir dos dados, e conclusões a respeito dos pontos fortes e limitações do trabalho.
        - ✅ O nome do arquivo deve conter seu nome completo, RM e pbl_fase4.ipynb. Exemplo: “JoaoSantos_rm76332_pbl_fase4.ipynb”.


- ✅ Um vídeo de até 5 minutos demonstrando o funcionamento desse entregável, postado no YouTube de forma **“não listado”**, e deverá possuir o link no seu GitHub, dentro do README.

- ✅ README com uma documentação introdutória, conduzindo o leitor para o Jupiter, onde lá, estará todo o passo a passo da solução e descrição completa **(Não necessário a repetição da descrição do Jupiter no README do GitHub. Deixar sempre os repositórios públicos para que eles sejam acessíveis pela equipe interna da FIAP, mas cuidado com seus links para que não vazem e sejam compartilhados e plagiados)**.


---


## 🎯 ENTREGA 2 — OBJETIVO:

Realizar uma estimativa de custos (On-Demand – 100%) para usar uma máquina Linux simples, comparando os valores cotados para a região de São Paulo (BR) e para a região da Virgínia do Norte (EUA). A máquina será utilizada para hospedar uma API que receberá dados dos sensores que coletam as variáveis da Entrega 1 e onde rodará a Machine Learning.

---

## 💻 O QUE PRECISA SER FEITO:

- ✅ Configuração da calculadora AWS com os seguintes itens: 

    - 2 CPUs.
    - 1 GIB de memória.
    - Até 5 Gigabit de rede.
    - 50 GB de armazenamento (HD).

- ✅ Estimativa entre um servidor em São Paulo (BR) e o outro na Virgínia do Norte (EUA).

---

## 📋 ENTREGÁVEIS:

- ✅ **Acrescentar esses dados no mesmo README da Entrega 1** em nome do seu grupo (de 1 a 5 pessoas). **Deverá conter imagens, gráficos e textos** suficientes para entender a justificativa em escolher recursos na nuvem AWS.
    
- ✅ Um segundo vídeo de até 5 minutos demonstrando a comparação de recursos usando a calculadora AWS, postado no YouTube de forma **“não listado”** e deverá possuir o link no seu GitHub, dentro do README.


---

## 🎯 IR ALÉM — OBJETIVO:

Desenvolver um sistema IoT completo de coleta e comunicação de dados climáticos utilizando ESP32 integrado ao Wi-Fi, com sensores de temperatura, umidade e luminosidade, publicando os dados via MQTT e exibindo em um dashboard web em tempo real.

---

## 💻 O QUE PRECISA SER FEITO:

- ✅ Definição dos sensores (DHT11 para temperatura/umidade e LDR para luminosidade) com justificativa de escolha.

- ✅ Montagem do circuito com ESP32, DHT11 e LDR na protoboard.

- ✅ Programação do ESP32 em C/C++ para leitura dos sensores e publicação via MQTT (broker HiveMQ).

- ✅ Desenvolvimento do servidor Python com Flask para receber os dados MQTT e exibir em um dashboard web.

- ✅ Diagrama de arquitetura do sistema IoT.

- ✅ Esquema de montagem dos componentes.

---

## 📋 ENTREGÁVEIS:

- ✅ Código fonte do ESP32 (`ir-alem/esp32_sensor.ino`) com leitura dos sensores e envio via MQTT.

- ✅ Servidor dashboard em Python (`ir-alem/servidor_dashboard.py`) com interface web para visualização em tempo real.

- ✅ Arquivo de dependências Python (`ir-alem/requirements.txt`).

- ✅ Documentação completa no README com arquitetura, montagem, instalação e configuração.

- ⬜ Vídeo demonstrativo do sistema funcionando, postado no YouTube de forma **"não listado"** com link no README.
