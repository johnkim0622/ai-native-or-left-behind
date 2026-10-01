# AI-Native or Left Behind? How Young Workers Really Use AI

🚧 **Status: in progress (Sept–Dec 2026)**

## The question
AI capabilities are advancing faster than experts predicted, but adoption at work is uneven.
This project asks: **is the AI gap between young and older workers really about age, or is it
explained by education and job type?** It also looks at who actually saves time with AI, and
whether the jobs the U.S. Bureau of Labor Statistics rates as "highly AI-exposed" actually show more AI use.


## Data
- **Epoch AI / Ipsos "AI at work" survey (July 2026):** 1,103 employed U.S. adults from a
  probability-based panel, with survey weights. [Source](https://epoch.ai/data/polling) (CC-BY 4.0)
- **BLS AI exposure categories (Aug 2026):** exposure ratings for 831 occupations.
  [Source](https://www.bls.gov/emp/publications/ai-exposure-categories.htm)

## Approach
- Survey-weighted estimates with 95% confidence intervals
- Validation: reproduce Epoch's published figures before any new analysis
- Stratified comparisons (age × education, age × job type) + logistic regression
- Analysis plan and expectations written **before** looking at results

## Progress
- [x] Project brief and analysis plan
- [x] Data verification (`notebooks/00_verify.ipynb`)
- [ ] Cleaning + validation against published figures
- [ ] Analysis (Q1–Q3) and figures
- [ ] Findings, recommendations, limitations
- [ ] Interactive "Where do you stand?" tool

## Repository structure
- `data/raw/`: original files, never edited
- `notebooks/`: 00_verify → 01_clean → 02_analysis → 03_figures
- `src/`: reusable functions


## Transparency
Utilized AI as a collaborator for brainstorming, code drafts and syntax explanations. 
I chose the question, made the design and analysis decisions, and verified every result.
