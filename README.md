# mistral-ai-dpo


### What we did
1. Built a private dataset with our in‑house GDPR expert (UK/US focus) including real‑world style queries, answers, and redacted case analyses.

2. Fine‑tuned `unsloth/mistral-7b-instruct-v0.2-bnb-4bit` for a GDPR‑aware legal assistant focused on practical Q&A and drafting.

3. Achieved higher precision and recall on a legal QA set after a single PEFT epoch, while keeping training efficient and reproducible with W&B tracking.

