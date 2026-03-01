# W&B at Mistral Worldwide Hackathon 2026
# DPO Data protection officer assistant fine tune

Data Protection Officer (DPO) and Data Protection Assistant (DPA Assistant) are key roles in ensuring an organization's compliance with data protection laws such as the UK GDPR and the Data Protection Act 2018.

### What we did
1. Built a private dataset with our in‑house GDPR expert (UK/US focus) including real‑world style queries, answers, and redacted case analyses.

Dataset details:
Train and eval set - 50 and 50 professional curated questions and answers with quote to describe the answer. 

2. Fine‑tuned `unsloth/mistral-7b-instruct-v0.2-bnb-4bit` for a GDPR‑aware legal assistant focused on practical Q&A and drafting.

3. Achieved higher precision and recall on a legal QA set after a single PEFT epoch, while keeping training efficient and reproducible with W&B tracking.

