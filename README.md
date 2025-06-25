[![Release](https://img.shields.io/github/v/release/tosodo/lomaautos-ai-agent)](https://github.com/tosodo/lomaautos-ai-agent/releases)
[![MIT License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
[![CI/CD](https://github.com/tosodo/lomaautos-ai-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/tosodo/lomaautos-ai-agent/actions)


# lomaautos-ai-agent
Multichannel AI receptionist powered by LangChain, GPT, n8n, and Auto Trader APIs. Features agent reasoning, Google Workspace automation, and plug-and-play lead workflows.


## 🚀 Key Features

- 🤖 AI receptionist (voice, chat, email, WhatsApp)
- 🧠 LangChain-powered specialist agents (valuation, booking, finance, service)
- 📊 Real-time analytics dashboard
- 🔗 Google Workspace integration (Gmail, Sheets, Chat, Calendar)
- ⚙️ Automated workflows with n8n
- 💬 Conversation memory & sentiment analysis
- 🌐 Multi-language support

## 🏗️ Architecture Overview


> See: [docs/architecture.md](docs/architecture.md)

## 📦 Tech Stack

| Layer | Tools |
|-------|-------|
| Workflow Engine | n8n (custom nodes) |
| AI Framework | LangChain + OpenAI |
| Backend | FastAPI, Redis, PostgreSQL |
| Comms | Twilio (WhatsApp/SMS/Voice) |
| Integration | Google Workspace APIs |
| Dashboard | Lovable.dev + React |
| Deploy | Docker, Kubernetes |
| Monitoring | Prometheus, OpenTelemetry |

## 🛠️ Getting Started'''

```bash
git clone https://github.com/tosodo/lomaautos-ai-agent.git
cd lomaautos-ai-agent
chmod +x scripts/setup/install.sh
./scripts/setup/install.sh


