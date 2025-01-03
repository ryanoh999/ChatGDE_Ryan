# ChatGDE

This repo contains the implementation of ChatGDE.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Experiments](#experiments)

## Introduction

Efficient groundwater management is essential for environmental sustainability, particularly in regions like California. Groundwater-dependent ecosystems (GDEs) are critical for biodiversity, water quality, and carbon storage but are vulnerable to groundwater depletion. The California Sustainable Groundwater Management Act (SGMA) mandates Groundwater Sustainability Agencies (GSAs) to develop and review Groundwater Sustainability Plans (GSPs), a time-consuming and costly process.

ChatGDE was developed to automate portions of the GSP review process, leveraging large language models (LLMs) like GPT to improve efficiency and reduce costs. By employing techniques like Retrieval Augmented Generation (RAG), fine-tuning, and prompt engineering, ChatGDE provides preliminary evaluations aligned with human reviews, achieving up to 73% agreement with expert evaluations. This represents a significant advancement in applying AI to streamline environmental policy tasks.

## Features

```
ChatGDE
├── GSP_Drafts
│   ├── Rubrics
│   │   ├── 1_BigValley_DraftGSP_ScoringRubric.csv
│   │   ├── 11_Butte_DraftGSP_ScoringRubric.csv
│   │   ├── 14_EastContraCosta_DraftGSP_ScoringRubric.csv
│   │   ├── 15_Fillmore_DraftGSP_ScoringRubric.csv
│   │   ├── 30_SonomaValley_DraftGSP_ScoringRubric.csv
│   │   ├── 46_Modesto_DraftGSP_ScoringRubric.csv
│   │   ├── 50_SanLuisObispoValley_DraftGSP_ScoringRubric.csv
│   │   └── 55_SantaMargarita_DraftGSP_ScoringRubric.csv
│   ├── 1_BigValley.pdf
│   ├── 11_Butte.pdf
│   ├── 14_ECC.pdf
│   ├── 15_Fillmore.pdf
│   ├── 30_Sonoma.pdf
│   ├── 46_Modesto.pdf
│   ├── 50_SLO.pdf
│   └── 55_SanMargarita.pdf
├── FinalPaperExperimentsNoKey.ipynb
├── FinalPaperVisualizationsNoKey.ipynb
├── prompts3.py
└── prompts_2.py
```



This repo is composed of the following:
- `GSP_Drafts/` Contains PDF files of Groundwater Sustainability Plans (GSPs) for various counties. Add or update files here based on the plans you want to evaluate.
- `Rubrics/' Contains CSV files of human-scored rubrics corresponding to the GSPs. Add or update files here based on which county’s scoring rubric you want to include.
- `FinalPaperExperimentsNoKey.ipynb` A Jupyter Notebook containing the experiments performed for the paper, focusing on model optimization and evaluation techniques.
- `FinalPaperVisualizationsNoKey.ipynb` A Jupyter Notebook containing the visualizations used in the research paper, detailing results and performance metrics.
- `prompts3.py` Contains the third version of prompts used for the model, reflecting binary classification.
- `prompts_2.py` Contains the second version of prompts used for the model, with our best prompt engineering results. Includes the "No", "Somewhat" and "Yes" categories.

## Experiments

To optimize ChatGDE’s performance, we conducted a series of experiments, focusing on vector storage, prompt engineering, and model fine-tuning:

## **Structural Experiments**:

	1.	Vector Storehouse:
	•	Levels: Compared CHROMA and FAISS for storing text embeddings.
	•	Results: FAISS achieved higher accuracy (52.8%) compared to CHROMA (33.9%).
	2.	Vector Split Strategy:
	•	Levels: Split GSPs by page vs. fixed chunk sizes.
	•	Results: Page-based splitting provided better accuracy by retaining context integrity.
	3.	Vector Retrieval Quantity:
	•	Levels: Set k = 5, 10, 15, where k is the number of vectors retrieved per query.
	•	Results: k=10 yielded the best balance between accuracy and avoiding context length errors.
	4.	ChatGPT Model Versions:
	•	Levels: Tested GPT-3.5 Turbo, GPT-4, and GPT-4o.
	•	Results: Fine-tuned GPT-4o outperformed others, particularly in precision and recall metrics.

## **Prompt Engineering**:

	1.	Standardizing Prompts:
	•	Adjusted formatting for consistency and spelled out acronyms.
	•	Results: Standardization had minimal impact on model accuracy.
	2.	Critical Instruction Emphasis:
	•	Modified prompts to encourage “skeptical evaluation.”
	•	Results: Improved response distribution and accuracy modestly.
	3.	Confidence Levels:
	•	Levels: Added instructions for models to include confidence levels with responses.
	•	Results: Enabled better evaluation of model certainty and performance trade-offs.

## **Fine-Tuning and Simplification**:

	1.	Binary Classification:
	•	Merged “No” and “Somewhat” into a single category.
	•	Results: Improved accuracy to 64% but reduced precision and recall.
	2.	Fine-Tuning:
	•	Models: Fine-tuned GPT-3.5 and GPT-4o using custom GSP training data.
	•	Results: Fine-tuned GPT-4o achieved the highest performance (accuracy: 73%, AUCROC: 0.77).

These experiments demonstrate the potential of LLMs to augment, though not entirely replace, human expertise in environmental policy reviews. Future work will focus on ensemble approaches and testing updated LLMs, possibly outside of the OpenAI ecosystem.
