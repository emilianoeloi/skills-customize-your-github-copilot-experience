---
applyTo: "assignments/**/*.md"
---

# Diretrizes de Estrutura para Markdowns de Tarefas

Todos os arquivos markdown de tarefas devem seguir estas diretrizes:

## 1. Uso do Template

- Os arquivos markdown de tarefas devem seguir a estrutura em [`templates/assignment-template.md`](../../templates/assignment-template.md).
- A tarefa deve ser criada como um arquivo `README.md`.
- Não remova ou pule seções obrigatórias do template.
- Preserve a ordem das seções exatamente como no template.

## 2. Orientação das Seções

Os cabeçalhos e subtítulos estruturais devem usar EXATAMENTE o mesmo texto do template, incluindo os emojis. Não traduza esses títulos.

- `# 📘 Assignment: [Assignment Title]` — Substitua `[Assignment Title]` por um nome curto e descritivo.
- `## 🎯 Objective` — Escreva 1 ou 2 frases resumindo o que o aluno aprenderá ou construirá.
- `## 📝 Tasks` — Agrupe as atividades práticas da tarefa.
- `### 🛠️ [Task Title]` — Use um título curto, específico e orientado à ação para cada tarefa.
- `#### Description` — Explique com clareza o que o aluno precisa fazer.
- `#### Requirements` — Introduza uma lista objetiva de critérios verificáveis.

## 3. Conteúdo Esperado

- O conteúdo descritivo pode estar em português para manter o material amigável aos alunos.
- Os títulos estruturais do template devem permanecer em inglês, exatamente como definidos no template.
- Em `Requirements`, use bullets curtos, específicos e mensuráveis.
- Inclua exemplos em blocos de código quando isso ajudar a esclarecer entrada, saída ou comportamento esperado.
- Evite seções extras, notas longas ou variações de formatação que desviem do template.

## 4. Estrutura Mínima Esperada

Cada arquivo deve seguir este formato base:

```md
# 📘 Assignment: [Assignment Title]

## 🎯 Objective

[Breve objetivo da tarefa]

## 📝 Tasks

### 🛠️ [Task Title]

#### Description
[Descrição da tarefa]

#### Requirements
Completed program should:

- [Requirement 1]
- [Requirement 2]
```