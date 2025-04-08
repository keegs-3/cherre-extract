# 🏗️ Cherre ML Pipeline

This project builds a machine learning-ready dataset using property data from Cherre and Yardi to model **likelihood of sale**.

---

## 📦 Project Structure

```bash
cherre-ml-pipeline/
├── .env                    # 🔒 API key (CHERRE_API_KEY)
├── README.md               # 📖 This file
├── requirements.txt        # 🧰 Python deps
├── main.py                 # 🔁 Orchestrator
├── config/
│   └── fields.yaml         # 🎯 Field selector per endpoint
├── data/
│   ├── raw/                # 🧪 JSON dumps from Cherre
│   └── processed/          # 📊 Cleaned tabular CSVs
├── src/
│   ├── auth.py             # 🔐 Env + token
│   ├── cherre_api.py       # 🔌 GraphQL caller
│   ├── extract/            # 📤 Data pullers per table
│   ├── transform/          # 🧱 ML dataset builder
│   ├── match/              # 🔍 Yardi <> Cherre matchers
│   └── utils/              # 🧰 Helpers & logger

