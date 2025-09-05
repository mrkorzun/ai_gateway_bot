# 🤖 AI-Gateway-Bot

Telegram bot with full OpenAI API integration designed for **reselling AI services**.  
The project provides a convenient interface for using Chat, Vision, and Image Generation models directly in Telegram, while handling billing, balance management, and request logging.

This bot is aimed at developers, entrepreneurs, and businesses that want to **monetize AI usage** without building everything from scratch.  
It includes a built-in billing system with a 50% markup, user cabinet for balance management, complete request history stored in PostgreSQL, and proxy support for stable API access.  

Deployed with Docker/GitHub, the bot ensures scalable, maintainable, and production-ready infrastructure.  

<p align="center">
  <img src="https://img.shields.io/badge/python-3.11%2B-blue.svg" />
  <img src="https://img.shields.io/badge/aiogram-3.x-brightgreen.svg" />
  <img src="https://img.shields.io/badge/OpenAI-API-orange.svg" />
  <img src="https://img.shields.io/badge/PostgreSQL-16%2B-blue.svg" />
  <img src="https://img.shields.io/badge/docker-ready-2496ED.svg" />
  <img src="https://img.shields.io/badge/proxy-supported-important.svg" />
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" />
</p>


---

## 🚀 Features

- 💬 **Chat** — interact with any selected OpenAI model.  
- 👁 **Vision** — analyze an image (1 request → response → back to main menu).  
- 🎨 **Image Generation (DALL·E)** — create images from prompts.  
- 👤 **Personal Cabinet**:
  - view user ID and balance,
  - top-up balance via payment link,
  - verify payment.  
- ⚙️ **Model Selection** — switch between available models stored in the database.  
- 💾 **Request History**:
  - logs every request, user, cost, and tokens spent.  
- 💸 **Monetization**:
  - each model is priced **50% higher** than official OpenAI API rates,
  - balance is deducted automatically.  
- 🌐 **Proxy support** for stable API access.

---

## 💰 Pricing Model & Payments

- Each OpenAI model is billed **50% higher** than the official OpenAI API price.  
  Example: if the API price is $0.01, the user is charged $0.015.  
- User balance is stored in the database and automatically deducted after each request.  
- Payment workflow:
  1. User clicks **Top Up Balance** in the Personal Cabinet.  
  2. Enters the desired amount and receives a payment link.  
  3. After payment, clicks **Verify Payment**:  
     - if successful → balance is updated, success message is shown;  
     - if failed → nothing changes.  
- All transactions are logged (user ID, amount, status).  
- Statistics dashboard will be available in the admin panel.

---

## 🛠 Tech Stack

- Python 3.11+  
- Aiogram (Telegram Bot API)  
- OpenAI API (ChatGPT, GPT-Vision, DALL·E)  
- PostgreSQL + SQLAlchemy + Alembic  
- Docker + docker-compose  
- GitHub Actions (CI/CD)  

---

## 📂 Project Structure

```text
repo/
├─ bot/          # Telegram handlers
├─ services/     # business logic (balance, billing, AI)
├─ providers/    # OpenAI API + proxy
├─ db/           # SQLAlchemy models, Alembic migrations
├─ admin/        # admin panel (stats, CRUD)
├─ tests/        # unit tests
├─ docker/       # Dockerfile and scripts
├─ deploy/       # docker-compose.prod.yml and configs
├─ .env.example  # example environment variables
├─ README.md
└─ requirements.txt
```

---

## ⚙️ Installation & Run
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

cp .env.example .env
# fill in keys and settings

docker-compose up --build -d
```

---

## 📊 Roadmap

- [x] Basic Telegram bot
- [ ] OpenAI API integration (chat/vision/image)
- [ ] Personal cabinet + balance tracking
- [ ] Balance top-up & payment verification
- [ ] PostgreSQL + SQLAlchemy + Alembic
- [ ] Token & cost tracking
- [ ] Admin panel (stats, users)
- [ ] Docker + server deployment
- [ ] CI/CD via GitHub Actions
