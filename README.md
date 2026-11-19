<div align="center">

# SenseWay RJ

**Tecnologia assistiva para mobilidade urbana em Madureira, Rio de Janeiro**

Global Solution 2026 · FIAP  
Computational Thinking with Python · Turma **1ESSRQ-2026**

</div>

## Equipe

| Integrante | Registro acadêmico |
| :--- | :---: |
| **Samuel Dantas Silva de Medeiros** | **RM 576922** |
| **Felipe de Oliveira Corrêa** | **RM 574803** |

---

[Como executar](#como-executar) · [Lógica do protótipo](#lógica-do-protótipo) · [Demonstração](#demonstração) · [Arquivos da entrega](#arquivos-da-entrega)

## Sobre o projeto

O SenseWay RJ explora como uma pulseira assistiva poderia sinalizar a proximidade de obstáculos para pessoas com deficiência visual durante deslocamentos urbanos. Madureira, no Rio de Janeiro, é o cenário escolhido para o projeto.

Nesta entrega, a atividade **O Cérebro da CitizenTech** implementa a lógica de decisão em Python. O programa recebe uma lista de distâncias simuladas, classifica cada leitura e apresenta avisos e estatísticas no terminal.

## Como executar

Com o **Python 3** instalado, baixe ou clone o repositório. Abra um terminal na pasta principal do projeto e execute:

```bash
python python/main.py
```

Se o interpretador estiver disponível como `python3`, use `python3 python/main.py`. O programa usa recursos nativos do Python e roda sem instalar bibliotecas adicionais.

| Opção | O que aparece no terminal |
| :---: | :--- |
| **1** | Lista numerada com a distância em centímetros e a classificação de cada leitura |
| **2** | Média, maior distância, percentual de leituras em alerta e número de falhas |
| **3** | Classificação e aviso de uma leitura escolhida pelo número |
| **0** | Mensagem de encerramento e saída do programa |

## Lógica do protótipo

### Dados e classificação

A lista contém **13 distâncias simuladas em centímetros**. São **12 leituras válidas** e uma leitura de **0 cm**, usada para representar falha do sensor. A classificação verifica primeiro se o valor está fora do intervalo válido e depois aplica os limites de proximidade.

| Estado | Regra em centímetros | Exemplos | Interpretação |
| :--- | :--- | :--- | :--- |
| **LIVRE** | Acima de 120 até 400 | 121 cm e 220 cm | Nenhum obstáculo próximo detectado pelo sensor |
| **ATENÇÃO** | Acima de 50 até 120 | 65 cm e 120 cm | Obstáculo na faixa de alerta |
| **PRÓXIMO** | De 2 a 50 | 25 cm e 50 cm | Obstáculo muito próximo |
| **FALHA** | Abaixo de 2 ou acima de 400 | 0 cm | Leitura inválida. O caminho não deve ser considerado livre |

### Como o resumo é calculado

- **Média e maior distância** consideram apenas leituras válidas.
- **Percentual em alerta** divide o total de leituras ATENÇÃO e PRÓXIMO pelo total de leituras válidas e multiplica por 100.
- **Falhas** são contadas separadamente. O registro de 0 cm fica fora da média e do percentual.

O código aplica listas, estruturas condicionais, laços de repetição, contadores e validação de entradas. O menu permanece ativo até a opção **0**.

## Demonstração

A sessão registrada usa a sequência **1 → 2 → 3 → 13 → 0**. Ela lista os estados, exibe o resumo, consulta a leitura **13** para demonstrar o tratamento de uma falha e encerra o programa.

| Indicador | Resultado |
| :--- | ---: |
| Média das distâncias válidas | **106,75 cm** |
| Maior distância válida | **220 cm** |
| Leituras válidas em alerta | **7 de 12 (58,3%)** |
| Falhas | **1** |

![Captura do terminal mostrando as opções do programa e o resumo das leituras](python/execucao.png)

Os dados e limites são ilustrativos e foram usados para a demonstração acadêmica. O protótipo não substitui a bengala nem foi validado para uso em deslocamentos reais.

## Arquivos da entrega

| Arquivo | Conteúdo |
| :--- | :--- |
| [`main.py`](python/main.py) | Código-fonte da simulação, do menu e dos cálculos |
| [`README.md`](python/README.md) | Documentação técnica da disciplina e integração com as demais partes do projeto |
| [`prompts.md`](python/prompts.md) | Registro dos prompts usados no desenvolvimento |
| [`registro_da_execucao.txt`](python/registro_da_execucao.txt) | Saída em texto da sessão de demonstração |
| [`execucao.png`](python/execucao.png) | Captura da execução no terminal |
