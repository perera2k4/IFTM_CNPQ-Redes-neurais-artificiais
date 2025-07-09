<div align="center">
  <img src="./assets/if-logo.png" alt="Logo da Instituição" width="450"/>
  <h3>Instituto Federal de Educação, Ciência e Tecnologia do Triângulo Mineiro - Campus Ituiutaba</h3>
</div>

# 🤖 Redes Neurais Artificiais e Suas Aplicações Práticas: Um Estudo com Estudantes do Ensino Médio

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![PyTorch](https://img.shields.io/badge/pytorch-%23EE4C2C.svg?logo=pytorch&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?logo=scikit-learn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-%23150458.svg?logo=pandas&logoColor=white)
![matplotlib](https://img.shields.io/badge/matplotlib-%230077B5.svg?logo=matplotlib&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-Ativo-brightgreen.svg)

**Autor:** Bruno Pereira Carvalho  
**Orientador:** Prof. Dr. André Luiz França Batista  
**Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Triângulo Mineiro - Campus Ituiutaba  
**Ano:** 2020

---

## 🎓 Apresentação do Projeto

Este repositório apresenta um estudo prático e didático sobre Redes Neurais Artificiais (RNAs), voltado para estudantes do ensino médio. O objetivo é demonstrar, de forma acessível, como construir, treinar e avaliar RNAs utilizando Python e conjuntos de dados clássicos da ciência de dados.

O projeto, originalmente desenvolvido em notebooks Jupyter (`.ipynb`), foi completamente convertido para scripts Python (`.py`) funcionais, com melhorias significativas na estrutura, documentação e funcionalidades.

---

## 🛠️ Bibliotecas e Tecnologias

- **Python 3.8 ou superior**
- **PyTorch** — Construção e treinamento das redes neurais
- **scikit-learn** — Datasets, pré-processamento e utilitários de Machine Learning
- **NumPy** — Manipulação de arrays e computação numérica
- **Matplotlib** — Visualização de gráficos e resultados
- **pandas** — Manipulação e análise de dados tabulares
- **yfinance** — Obtenção de dados financeiros do Yahoo Finance

---

## 📁 Estrutura do Projeto

```
├── #1 Íris/                    # Classificação de flores Íris
│   ├── setosa.py              # Detecção de Iris Setosa
│   ├── versicolor.py          # Detecção de Iris Versicolor
│   └── virginica.py           # Detecção de Iris Virginica
├── #2 Wine/                   # Classificação de vinhos
│   ├── wine.py                # Classificação principal
│   ├── wine_class_1.py        # Foco na classe 1
│   └── wine_class_2.py        # Foco na classe 2
├── #3 Breast cancer/          # Classificação de câncer de mama
│   └── breast_cancer.py       # Detecção de câncer maligno/benigno
├── #4 Previsão de séries temporais/  # Previsão de preços de ações
│   ├── magazine_luiza.py      # Previsão MGLU3.SA
│   ├── csn.py                 # Previsão CSNA3.SA
│   └── jbs.py                 # Previsão JBSS3.SA
├── #5 Interface gráfica/      # Interfaces GUI (PyQt)
├── #6 Vazões/                 # Análise de vazões
├── #7 Yahoo finance/          # Dados financeiros
├── requirements.txt           # Dependências do projeto
├── run_projects.bat           # Executor em lote para Windows (CMD)
├── run_projects.ps1           # Executor em lote para PowerShell
├── test_conversion.py         # Script de teste de conversão
└── LICENSE                    # Licença MIT
```

---

## 🧪 Experimentos Realizados e Especificações Técnicas

### 🌸 1. Dataset Iris

- **Descrição:** Previsão da espécie de flores a partir de quatro atributos morfológicos.
- **Objetivo:** Classificação binária para cada uma das três espécies (Setosa, Versicolor, Virginica).
- **Arquitetura:** 4 neurônios de entrada → 5 na camada oculta → 1 de saída.
- **Acurácia Esperada:** >95%.

### 🍷 2. Dataset Wine

- **Descrição:** Classificação de vinhos em três classes, utilizando 13 atributos físico-químicos.
- **Objetivo:** Classificação das 3 classes de vinho.
- **Arquitetura:** 13 neurônios de entrada → 13 na camada oculta → 1 de saída.
- **Acurácia Esperada:** >90%.

### 🩺 3. Dataset Breast Cancer

- **Descrição:** Classificação de tumores malignos e benignos a partir de 30 atributos clínicos.
- **Objetivo:** Classificação binária para diagnóstico (maligno/benigno).
- **Arquitetura:** 30 neurônios de entrada → 30 na camada oculta → 1 de saída.
- **Acurácia Esperada:** >95%.

### 💹 4. Dataset Yahoo Finance (Séries Temporais)

- **Descrição:** Previsão de preços de ações da BOVESPA (Magazine Luiza, CSN, JBS).
- **Objetivo:** Prever o valor de uma ação com base em seu histórico de preços.
- **Método:** Janela deslizante de 50 dias para prever o próximo dia.
- **Período dos Dados:** 2016-2020.
- **Arquitetura:** 50 neurônios de entrada → 100 na camada oculta → 1 de saída.

---

## ⚙️ Parâmetros de Treinamento

| Experimento      | Épocas   | Taxa de Aprendizado | Momentum | Neurônios (Oculta) | Otimizador | Função de Perda |
|------------------|----------|---------------------|----------|--------------------|------------|-----------------|
| Íris             | 10.000   | 0.9                 | -        | 5                  | SGD        | MSELoss         |
| Wine             | 100.000  | 0.9                 | 0.3      | 13                 | SGD        | MSELoss         |
| Breast Cancer    | 100.000  | 0.9                 | 0.3      | 30                 | SGD        | MSELoss         |
| Séries Temporais | 100.001  | 0.09                | 0.03     | 100                | SGD        | MSELoss         |

---

## 🚀 Como Executar

### 1. Pré-requisitos

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
# Ou manualmente:
pip install torch numpy scikit-learn matplotlib pandas yfinance
```

### 2. Métodos de Execução

**Execução Direta (PowerShell/CMD):**
```powershell
"C:/Program Files/Python313/python.exe" "#1 Íris/setosa.py"
"C:/Program Files/Python313/python.exe" "#3 Breast cancer/breast_cancer.py"
```

**Menu Interativo (PowerShell):**
```powershell
.\run_projects.ps1
```

**Menu Interativo (CMD):**
```cmd
run_projects.bat
```

---

## 📊 Resultados Esperados

A execução de cada script exibirá informações do dataset, progresso do treinamento, acurácia final e gráficos.

### Exemplo de Saída (Terminal)

```
Dataset Iris carregado:
Formato dos dados: (150, 4)
Classes: ['setosa' 'versicolor' 'virginica']
Número de amostras por classe: [50 50 50]
Distribuição das classes convertidas: [100  50]
Dados de treinamento: torch.Size([120, 4])
Dados de teste: torch.Size([30, 4])
Modelo criado - Input size: 4, Hidden size: 5
Iniciando treinamento...
Epoch 0: train loss: 0.2791103422641754
Epoch 1000: train loss: 0.0007284045568667352
...
Epoch 9000: train loss: 5.3008032409707084e-05
Testando o modelo...
Acurácia: 100.00%
```

### Gráficos Gerados

- **Curva de Erro:** Mostra a diminuição da perda (erro) do modelo durante o treinamento.
- **Comparação Real vs. Predito:** Compara visualmente os valores previstos pelo modelo com os valores reais.

---

## 🩻 Solução de Problemas

- **Erro de Importação:** Certifique-se de que as dependências foram instaladas corretamente.
- **Erro de Conexão (yfinance):** Verifique sua conexão com a internet, firewall ou proxy.
- **Erro de Memória:** Reduza o número de épocas, o tamanho do batch ou a complexidade da rede neural.
- **Erro de Caminho:** Verifique se você está no diretório correto ao executar os comandos.

---

## 📚 Considerações Finais

Os experimentos demonstraram que redes neurais artificiais são ferramentas poderosas para classificação e previsão. Para séries temporais, o aumento do número de épocas tende a melhorar a precisão, com destaque para o desempenho do modelo na previsão das ações da CSN. O projeto reforça a importância do ajuste de hiperparâmetros e da análise crítica dos resultados.

---

## 👨‍🏫 Créditos e Contato

Este projeto foi desenvolvido por **Bruno Pereira Carvalho**, sob orientação do **Prof. Dr. André Luiz França Batista** (IFTM - Campus Ituiutaba).

Para dúvidas ou sugestões, utilize as [issues do GitHub](https://github.com/).

---

## 🤝 Contribuição

1. Faça um fork do repositório.
2. Crie uma branch para sua feature.
3. Faça commit de suas mudanças.
4. Faça push para a branch.
5. Abra um Pull Request.

---

## 📝 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.