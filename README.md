# NPCs com Decisões Psicologicamente Orientadas

Protótipo acadêmico inspirado no artigo **"A Framework for Creating Non-Player Characters That Make Psychologically-Driven Decisions"**.

## Sobre o projeto

Este projeto implementa, em pequena escala, um protótipo de NPC capaz de tomar decisões com base em:

- **emoção**
- **mood**
- **personalidade**
- **seleção de ação**

A proposta é reproduzir os conceitos centrais do framework **EmoBeT** em um cenário textual simples, permitindo observar como estímulos do jogador alteram o estado afetivo do NPC e, por consequência, a decisão tomada.

Em vez de responder apenas com regras fixas, o NPC processa o estímulo recebido, gera uma emoção, atualiza um estado afetivo interno e escolhe uma ação com base nesse estado.

---

## Objetivo do MVP

A primeira versão do projeto busca validar a seguinte hipótese:

> diferentes estímulos do jogador alteram o estado afetivo do NPC, e esse estado influencia a decisão tomada.

Além disso, o protótipo também busca verificar se NPCs com diferentes níveis de personalidade, especialmente no traço **neuroticism**, reagem de forma diferente ao mesmo evento.

---

## Conceitos principais implementados

### 1. Appraisal simplificado

Responsável por interpretar o estímulo textual do jogador e classificá-lo em uma categoria semântica simples.

Exemplos:
- pedido educado
- cobrança ríspida
- agradecimento
- insulto

### 2. Emotion Adder

Converte a categoria do estímulo em uma emoção do sistema.

Emoções usadas no MVP:
- `pride`
- `satisfaction`
- `resentment`
- `reproach`

### 3. Emotion Center

Representa o acúmulo afetivo recente do NPC.  
Esse componente recebe a emoção atual e mantém um histórico agregado que influencia o mood.

### 4. Mood Engine

Atualiza o mood do NPC com base no modelo **PAD**:

- **Pleasure**
- **Arousal**
- **Dominance**

Cada eixo varia entre `-1.0` e `1.0`.

### 5. Personality

Traços de personalidade modulam a intensidade do impacto emocional.  
No MVP, o foco principal está em **neuroticism**, usado para observar maior ou menor sensibilidade a estímulos negativos.

### 6. E-Selector

Seleciona a ação final do NPC com base no mood atual.

Ações possíveis:
- `ajudar_com_boa_vontade`
- `ajudar_de_forma_hostil`
- `hesitar`
- `recusar_ajuda`

---

## Fluxo geral do sistema

```text
Estímulo do jogador
   -> appraisal simplificado
   -> emoção gerada
   -> Emotion Center atualizado
   -> mood atualizado
   -> E-Selector escolhe a resposta
```

---

## Escopo da versão atual

O protótipo atual inclui:

- cenário textual simples
- conjunto reduzido de emoções
- mood baseado em PAD
- personalidade simplificada com foco em `neuroticism`
- seleção de ação baseada no mood
- logs em CSV para análise experimental
- experimento com e sem decay emocional

---

## Estrutura do projeto

```text
implementation-paper-a-Framework-for-Creating-Non-Player-Characters/
│
├─ docs/
│  └─ papers/
│     └─ belle-icce-22.pdf
│
├─ experiments/
│  ├─ __init__.py
│  ├─ baseline_rule_npc.py
│  ├─ experiment_1_single_npc.py
│  ├─ experiment_2_two_npcs.py
│  ├─ experiment_3_emotion_response_grid.py
│  ├─ experiment_4_neuroticism_sweep.py
│  ├─ experiment_5_order_effect.py
│  ├─ experiment_6_recovery_curve.py
│  └─ experiment_7_emotional_decay.py
│
├─ logs/
│  ├─ .gitignore
│  └─ *.csv
│
├─ src/
│  ├─ __init__.py
│  ├─ main.py
│  │
│  ├─ data/
│  │  ├─ __init__.py
│  │  ├─ emotions.py
│  │  ├─ reactions.py
│  │  └─ scenarios.py
│  │
│  ├─ engines/
│  │  ├─ __init__.py
│  │  ├─ appraisal_engine.py
│  │  ├─ e_selector.py
│  │  ├─ emotion_adder.py
│  │  ├─ emotion_center.py
│  │  └─ mood_engine.py
│  │
│  ├─ models/
│  │  ├─ __init__.py
│  │  ├─ emotion.py
│  │  ├─ npc_state.py
│  │  ├─ pad.py
│  │  ├─ personality.py
│  │  └─ stimulus.py
│  │
│  └─ utils/
│     ├─ __init__.py
│     ├─ clamp.py
│     └─ logger.py
│
├─ README.md
├─ requirements.txt
└─ .gitignore
```

---

## Requisitos

- Python 3.10 ou superior
- Git instalado
- VS Code ou outro editor

Atualmente o projeto roda apenas com a biblioteca padrão do Python.

---

## Como executar

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m src.main
```

### Linux / WSL

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m src.main
```

---

## Como executar os experimentos

### Windows

```bash
python -m experiments.experiment_1_single_npc
python -m experiments.experiment_2_two_npcs
python -m experiments.experiment_3_emotion_response_grid
python -m experiments.experiment_4_neuroticism_sweep
python -m experiments.experiment_5_order_effect
python -m experiments.experiment_6_recovery_curve
python -m experiments.experiment_7_emotional_decay
```

### Linux / WSL

```bash
python3 -m experiments.experiment_1_single_npc
python3 -m experiments.experiment_2_two_npcs
python3 -m experiments.experiment_3_emotion_response_grid
python3 -m experiments.experiment_4_neuroticism_sweep
python3 -m experiments.experiment_5_order_effect
python3 -m experiments.experiment_6_recovery_curve
python3 -m experiments.experiment_7_emotional_decay
```

Os logs são salvos automaticamente na pasta `logs/`.

---

## Cenário textual utilizado

O MVP usa um pequeno conjunto de falas para testar a resposta do NPC:

- `por favor, me ajuda`
- `faz seu trabalho logo`
- `obrigado`
- `inútil`

Esses estímulos são mapeados para emoções diferentes e afetam o estado afetivo do NPC de forma distinta.

---

## Experimentos implementados

### Experimento 1 — Single NPC

**Arquivo:** `experiments/experiment_1_single_npc.py`

**Objetivo:**  
Verificar se diferentes sequências de estímulos alteram emoção, mood e ação do NPC.

**Como funciona:**  
Executa uma sequência positiva e uma sequência negativa sobre o mesmo tipo de NPC, medindo as mudanças de estado a cada turno.

**O que testa:**  
Se o fluxo `estímulo -> emoção -> mood -> ação` está funcionando.

---

### Experimento 2 — Two NPCs

**Arquivo:** `experiments/experiment_2_two_npcs.py`

**Objetivo:**  
Comparar dois NPCs com valores diferentes de `neuroticism` diante da mesma sequência negativa.

**Como funciona:**  
Um NPC é criado com `neuroticism` alto e outro com `neuroticism` baixo. Ambos recebem os mesmos estímulos.

**O que testa:**  
Se a personalidade altera a intensidade da reação emocional e o comportamento final.

---

### Experimento 3 — Emotion Response Grid

**Arquivo:** `experiments/experiment_3_emotion_response_grid.py`

**Objetivo:**  
Testar cada entrada isoladamente em NPCs com diferentes níveis de `neuroticism`.

**Como funciona:**  
Cada fala do jogador é aplicada separadamente em NPCs recém-criados.

**O que testa:**  
Se cada emoção puxa o mood na direção esperada e se esse efeito muda com a personalidade.

---

### Experimento 4 — Neuroticism Sweep

**Arquivo:** `experiments/experiment_4_neuroticism_sweep.py`

**Objetivo:**  
Observar como a sensibilidade emocional varia conforme o valor de `neuroticism` cresce.

**Como funciona:**  
Executa a mesma sequência negativa em NPCs com `neuroticism` variando de `0.0` a `1.0`.

**O que testa:**  
Se há progressão coerente do impacto emocional com a variação do traço de personalidade.

---

### Experimento 5 — Order Effect

**Arquivo:** `experiments/experiment_5_order_effect.py`

**Objetivo:**  
Verificar se a ordem dos estímulos altera o estado final do NPC.

**Como funciona:**  
Compara duas sequências com o mesmo conjunto de falas:
- positiva -> negativa
- negativa -> positiva

**O que testa:**  
Se o histórico afetivo acumulado realmente influencia o comportamento.

---

### Experimento 6 — Recovery Curve

**Arquivo:** `experiments/experiment_6_recovery_curve.py`

**Objetivo:**  
Avaliar se o NPC consegue se recuperar após uma sequência negativa seguida por interações positivas.

**Como funciona:**  
Aplica dois estímulos negativos e depois uma série de estímulos positivos.

**O que testa:**  
Se o sistema representa bem a recuperação do mood ao longo do tempo.

---

### Experimento 7 — Emotional Decay

**Arquivo:** `experiments/experiment_7_emotional_decay.py`

**Objetivo:**  
Comparar o comportamento do NPC com e sem dissipação temporal do Emotion Center.

**Como funciona:**  
Executa a mesma sequência de recuperação em duas condições:
- sem decay (`decay_factor = 1.0`)
- com decay (`decay_factor = 0.85`)

**O que testa:**  
Se o decay melhora a recuperação do mood sem eliminar o efeito do histórico emocional.

---

## Resultados observados

### Resultado geral

Os experimentos mostraram que o protótipo foi capaz de:

- alterar a emoção em função do estímulo do jogador
- alterar o mood com base na emoção acumulada
- mudar a ação escolhida a partir do mood atual
- responder de forma diferente ao mesmo estímulo quando o `neuroticism` muda
- preservar histórico afetivo entre turnos
- recuperar o comportamento cooperativo com mais plausibilidade quando o decay emocional é ativado

---

### Experimento 1 — Single NPC

**Sequência positiva**
- `por favor, me ajuda` gerou `pride` e manteve resposta cooperativa
- `obrigado` gerou `satisfaction`, levou o mood para `cooperative` e manteve `ajudar_com_boa_vontade`

**Sequência negativa**
- `faz seu trabalho logo` gerou `resentment`, mas o NPC ainda permaneceu funcionalmente cooperativo no primeiro turno
- `inútil` gerou `reproach`, levou o mood para `hostile` e mudou a ação para `ajudar_de_forma_hostil`

**Conclusão**  
O sistema respondeu de forma diferente a sequências positivas e negativas, validando a hipótese principal do MVP.

---

### Experimento 2 — Two NPCs

**NPC com neuroticism alto (`0.80`)**
- já no primeiro estímulo negativo o mood ficou `hostile`
- a resposta virou `ajudar_de_forma_hostil`

**NPC com neuroticism baixo (`0.10`)**
- no primeiro estímulo negativo o mood permaneceu `neutral`
- a ação continuou `ajudar_com_boa_vontade`
- só no segundo estímulo o NPC se tornou `hostile`

**Conclusão**  
O traço `neuroticism` influenciou claramente a sensibilidade ao evento negativo.

---

### Experimento 3 — Emotion Response Grid

**Com `neuroticism = 0.10`**
- estímulos positivos produziram estados neutros ou cooperativos
- estímulos negativos tiveram impacto moderado

**Com `neuroticism = 0.50`**
- insultos já foram suficientes para gerar hostilidade
- estímulos positivos ainda mantiveram ajuda cooperativa

**Com `neuroticism = 0.80`**
- `faz seu trabalho logo` e `inútil` geraram `hostile`
- estímulos positivos ainda ajudaram, mas com impacto mais fraco

**Conclusão**  
O efeito das emoções negativas cresce conforme o `neuroticism` aumenta.

---

### Experimento 4 — Neuroticism Sweep

Foi observada uma progressão coerente:

- de `0.00` a `0.60`, o primeiro estímulo negativo ainda não gerava hostilidade
- em `0.80` e `1.00`, o NPC já se tornava hostil no primeiro turno

Além disso, as intensidades emocionais negativas aumentaram gradualmente com o valor de `neuroticism`.

**Conclusão**  
O modelo respondeu de forma consistente à variação contínua de personalidade.

---

### Experimento 5 — Order Effect

**Sequência positiva -> negativa**
- o NPC chegou a `cooperative`
- depois dos estímulos negativos, terminou em `neutral`
- a ação final continuou `ajudar_com_boa_vontade`

**Sequência negativa -> positiva**
- o NPC ficou `hostile` no segundo turno
- mesmo após interações positivas, permaneceu `hostile`
- a ação final continuou `ajudar_de_forma_hostil`

**Conclusão**  
A ordem dos estímulos alterou o resultado final, mostrando que o modelo mantém histórico afetivo.

---

### Experimento 6 — Recovery Curve

Após dois estímulos negativos iniciais, o NPC entrou em estado `hostile`.  
Mesmo com várias interações positivas em seguida, o mood permaneceu hostil até o final da sequência.

**Conclusão**  
A versão sem decay mostrou recuperação lenta demais, sugerindo acúmulo excessivo de emoção negativa.

---

### Experimento 7 — Emotional Decay

**Sem decay (`decay_factor = 1.0`)**
- o Emotion Center acumulou fortemente os efeitos negativos
- o NPC permaneceu `hostile` até o final
- a ação não voltou para um comportamento cooperativo

**Com decay (`decay_factor = 0.85`)**
- o impacto das emoções passadas foi gradualmente reduzido
- o Emotion Center se recuperou com mais rapidez
- no turno final, o mood voltou para `neutral`
- a ação final voltou para `ajudar_com_boa_vontade`

**Conclusão**  
O decay emocional melhorou significativamente a plausibilidade temporal do modelo.

---

## Principais conclusões

Com base nos experimentos, o protótipo validou os seguintes pontos:

- estímulos diferentes geram emoções diferentes
- emoções influenciam o mood
- o mood influencia a ação escolhida
- `neuroticism` altera a sensibilidade emocional
- o histórico de interações afeta o estado futuro do NPC
- a introdução de decay melhora a recuperação do mood

---

## Limitações atuais

Apesar dos resultados positivos, o protótipo ainda possui limitações:

- appraisal textual simplificado, sem NLP real
- conjunto pequeno de emoções
- foco principal em apenas um traço de personalidade
- seleção de ação baseada em regras fixas
- ausência de memória de longo prazo
- ausência de avaliação com usuários ou em engine de jogo
- calibração ainda manual dos thresholds e intensidades

Além disso, sem decay emocional, o sistema tende a manter estados negativos por tempo excessivo.

---

## Próximos passos

Possíveis extensões do projeto:

### Curto prazo
- ajustar melhor os thresholds do seletor
- exportar gráficos do PAD ao longo dos turnos
- comparar sistematicamente baseline vs modelo afetivo
- testar novos valores de `decay_factor`

### Médio prazo
- adicionar mais emoções
- incluir mais traços de personalidade do modelo Big Five
- implementar memória de curto prazo
- enriquecer o appraisal textual

### Longo prazo
- portar o protótipo para uma engine como Unity ou Godot
- testar comportamento em tempo real
- avaliar percepção de believability com usuários
- comparar diferentes estratégias de atualização de mood

---

## Tecnologias utilizadas

- Python
- `dataclasses`
- CSV para logging experimental
- arquitetura modular com separação entre modelos, motores e experimentos

---

## Referência principal

Belle, S.; Gittens, C.; Graham, T. C. N.  
**A Framework for Creating Non-Player Characters That Make Psychologically-Driven Decisions**.

---

## Observação final

Este repositório representa uma **implementação inspirada no artigo**, e não uma reprodução literal de todos os detalhes do framework original.

O objetivo principal foi construir um protótipo pequeno, compreensível e experimentalmente observável, capaz de demonstrar a influência de emoção, mood, personalidade e histórico na tomada de decisão de NPCs.