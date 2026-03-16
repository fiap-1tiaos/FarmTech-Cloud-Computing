# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

## Sistema de Monitoramento e Previsão de Safra usando Machine Learning

## Grupo: FarmTech Solutions

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/gabriel-oliveira-b6353a16b/">Gabriel Oliveira dos Santos</a>
- <a href="https://www.linkedin.com/in/roberson-pedrosa-304ab523a/">Roberson Pedrosa de Oliveira Junior</a>
- <a href="https://www.linkedin.com/in/arthur-bruttel-7171b8381">Arthur Bruttel Nascimento</a> 
- <a href="https://www.linkedin.com/in/jonviotti/">Jonatan Viotti Rodrigues da Silva</a> 
- <a href="https://www.linkedin.com/in/eusamuelrocha/">Samuel Nicolas Oliveira Rocha</a>

## Vídeo demonstrativo:

- <a href="https://youtu.be/lI096I3a-KI"> Execução e dados - Jupyter Notebook</a>
- <a href="https://youtu.be/IwPJJlkNaDY?si=h9mY4XDt-yoDEiHJ"> Estimativa AWS Calculator</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/sabrina-otoni-22525519b/">Sabrina Otoni</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">André Godoi Chiovato</a>

---

## 📜 Descrição - Entrega 1

Este projeto de Ciência de Dados é parte integrante de uma atividade acadêmica voltada para a FarmTech Solutions. A solução utiliza técnicas avançadas de Inteligência Artificial para analisar dados climáticos e produtivos de uma fazenda, permitindo a gestão otimizada do cultivo por meio de scripts desenvolvidos em Python no ambiente Jupyter Notebook.

---

## 1. Introdução

O projeto visa aplicar modelos de Machine Learning sobre um dataset de rendimento agrícola, integrando duas frentes principais de estudo:

Aprendizado Não Supervisionado (Fase 5): Utilização de algoritmos de Clusterização (K-Means) para identificar perfis de produtividade, tendências e outliers na operação rural.

Aprendizado Supervisionado (Fase 4): Implementação e comparação de modelos de Regressão (como Random Forest e Decision Trees) para prever o rendimento futuro das safras com base em variáveis climáticas como precipitação, temperatura e umidade.

A solução final entrega uma análise robusta que transforma dados históricos em insights preditivos, auxiliando na redução de incertezas e no planejamento estratégico da produção agrícola.

## 2. Fontes Utilizadas

A base de dados foi analisada a partir do arquivo "crop_yield.csv", conforme exigido pela atividade

---

## 📜 Descrição - Entrega 2

---

Nessa segunda entrega, foi solicitada uma estimativa de custo on-demand (sob demanda) de uma estrutura de Linux simples em nuvem no servidor do AWS Calculator — ferramenta da Amazon Web Services que permite estimar custos de arquitetura em nuvem.

## 1. Introdução

Para a estimativa, foi necessária a configuração manual nas regiões solicitadas **(São Paulo - BR e Virgínia do Norte - EUA)** com base nos seguintes itens:

- 2 CPUs
- 1 GiB
- Até 5 GB de rede
- 50 GB de armazenamento 
- Restrições legais para armazenamento no exterior

## 2. Configurações

**Serviço Utilizado:** EC2

O EC2 oferece uma ótima performance e preço, atendendo a área de treinamento de Machine Learning e, também, os itens solicitados conforme listados na introdução, além de possuir uma infraestrutura confiável e escalável on-demand (sob demanda).

**Locação:** Instância compartilhada

O compartilhamento de instância utiliza uma estrutura física compartilhada entre diversos clientes da AWS, reduzindo significativamente o custo. Como o objetivo do projeto é a hospedagem de uma API simples, não há a necessidade de um isolamento completo.

**Sistema Operacional:** Linux

Escolhido conforme solicitado no projeto.

**Carga de Trabalho:** Uso constante

Como o intuito é a hospedagem em nuvem que coletará os dados dos sensores da entrega 1 para uma futura Machine Learning, é necessária uma workload (carga de trabalho) constante para o processamento contínuo de dados de modo que traga previsões de rendimento mais exatas.

**Número de Instâncias:** 1

O fato de ser uma API simples, tira a necessidade de um maior número, pois uma única instância é suficiente para atender a demanda.

**Tipo de Instância:** t4g.micro

A instância t4g.micro atende aos requisitos da introdução (2 CPUs, 1 GiB, até 5 GB de rede, ) e apresenta um baixo custo sob demanda. Portanto, se torna adequada para aplicações leves e simples.

**Opção de Pagamento:** On-demand

Selecionado conforme solicitado no projeto. 

**Armazenamento:** Amazon Elastic Block Store (Amazon EBS), SSD de uso geral (gp3), capacidade de 50 GB

O EBS é onde ocorre o armazenamento dos bancos de dados e arquivos, nele foi utilizado o gp3 pois atende aplicações gerais e possui um bom equilíbrio entre desempenho e custo. E, conforme solicitado, foi configurado para uma capacidade de armazenamento de 50 GB.

**Snapshots:** Não utilizado

Como o objetivo é apenas estimar o custo da infraestrutura, não foi necessário o uso de snapshots de backup.

**Monitoramento Detalhado:** Não utilizado

A estimativa de uma API simples em nuvem tira a necessidade de um monitoramento detalhado.

**Transferência de Dados:** Não utilizado

Como não foi estipulado um valor de tráfego de rede, a transferência de dados não foi considerada. 

**Custos Adicionais:** Não utilizado

O objetivo da análise foi calcular apenas o custo da infraestrutura principal necessária para hospedar a API.

## 3. Valores da Estimativa

Resumo Geral da Estimativa:

![Resumo da Estimativa](assets/imagens_entrega2/resumo_estimativa.png)

Estimativa Individual:

![Estimativa Individual](assets/imagens_entrega2/estimativa_individual.png)

Gráfico Representativo:

![Gráfico da Estimativa Individual Mensal](assets/imagens_entrega2/grafico_custo.png)

## 4. Conclusão

A estimativa teve um custo anual de **330,12 USD** com um custo mensal de **17,38 USD** para São Paulo e **10,13 USD** para Virgínia do Norte, totalizando um custo geral mensal de **27,51 USD**. Sendo assim, a região da Virgínia do Norte apresenta um custo **41,7%** inferior ao da região de São Paulo para a mesma configuração de infraestrutura. Contudo, mesmo que Virgínia do Norte possua um valor inferior, a região de São Paulo pode ser considerada melhor devido às restrições legais relacionadas à transferência internacional de dados e à necessidade de menor latência no acesso às informações coletadas pelos sensores.

---

## 📖 Pontos Gerais

## 1. Estrutura do Projeto

* Arquivo `.ipynb` principal com a análise, clusterização e regressão

* Base `crop_yield.csv` com dados climáticos e de rendimento da fazenda.

* Arquivo `grafico.py` com a estruturação do gráfico.

* Arquivo `LICENSE` com a descrição da licença do projeto.

* Arquivo `todo.md` com os checklists do que tem que ser feito

* Arquivo `README.md`com as instruções do projeto.

## 2. Tecnologias Utilizadas

**Entrega 1:**

* Python 3.x
* Jupyter Notebook
* Pandas (Manipulação de Dados)
* Scikit-Learn (Machine Learning)
* GitHub (Controle de Versão e Hospedagem)

**Entrega 2:**

* Python 3.x
* AWS Calculator
* Matplotlib (construção do gráfico)

---

## 🗂️ Localização dos Arquivos de Dados

Os arquivos da base de dados e o script estão localizados no repositório:

* **Base de Dados:** [Acessar crop_yield.csv](assets/crop_yield.csv)

* **Jupyter Notebook:** [Abrir Projeto](assets/GabrielOliveira_RM567166_RobersonPedrosa_RM567216_ArthurBruttel_RM568484_JonatanViotti_RM566787_SamuelRocha_RM568552_pbl_fase5.ipynb)

---

## 🎯 Fases do Projeto Cobertas

Este trabalho integra os conhecimentos das seguintes fases do curso:
* **Fase 5 (Clusterização):** Identificação de perfis de produtividade e análise de outliers via K-Means (Machine Learning Sem Supervisão).
* **Fase 4 (Regressão):** Implementação e comparação de modelos preditivos para estimar a colheita (Machine Learning Supervisionado).

---

## 📋 Licença

Este projeto está licenciado sob a licença MIT.  
Consulte o arquivo LICENSE para mais detalhes.

Este repositório foi baseado no template da FIAP, originalmente licenciado sob Creative Commons Attribution 4.0.

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
