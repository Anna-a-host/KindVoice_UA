## Problem Statement

Millions of Ukrainians experience stress, panic, isolation, and emotional exhaustion caused by war, displacement, uncertainty, and constant exposure to danger. While professional psychological support is important, it is often inaccessible, expensive, unavailable at night, or difficult to reach during crisis situations.

At the same time, many people simply need calm human-like presence, emotional grounding, and someone to talk to in moments of fear or loneliness.

KindVoice UA was created to address this issue by providing accessible, multilingual, emotionally supportive AI conversations directly inside Telegram — a platform already widely used by Ukrainians daily.

The project focuses not on replacing therapy, but on offering immediate emotional support, calming communication, and safe conversational interaction during stressful situations.
______________________________________________________________________________________________________________

## Solution Overview

KindVoice UA is an AI-powered Telegram bot designed to provide emotionally adaptive conversations for users experiencing stress, panic, wartime anxiety, loneliness, or emotional overwhelm.

The bot uses multiple AI providers with automatic failover to ensure reliability and uninterrupted availability. Conversations are generated using Gemini as the primary AI provider, with OpenRouter and Groq serving as fallback providers when needed.

Users can interact through both text and voice messages in Ukrainian or English.

The system dynamically adapts its conversational behavior depending on the emotional mode selected by the user, such as:

* panic support
* anxiety support
* wartime situations
* emotional grounding
* calm conversation
* support for internally displaced people (IDPs)

Voice messages are transcribed using Whisper speech recognition before being processed by the AI system.

To improve realism and reduce repetitive or inappropriate responses, the bot maintains lightweight rolling conversation memory that preserves recent context while remaining computationally efficient for deployment.

The project also includes a local SQLite database for user management and usage analytics, allowing future expansion toward personalized support experiences.

______________________________________________________________________________________________________________

## Key Features

💬 Emotionally Adaptive Conversations
🇺🇦 Multilingual Support (Ukrainian & English)
🎤 Voice Message Support
🧠 Contextual Memory
🔄 Multi-Provider AI Reliability
⚡ Fast AI Inference
📱 Telegram-Native Accessibility
📊 User Analytics & Statistics
💙 Human-Centered Design

The conversational tone was carefully engineered to feel calm, emotionally steady, and non-judgmental rather than robotic or overly clinical.

______________________________________________________________________________________________________________

## Technologies Used

**Programming Language:** Python

**Backend & Bot Framework:**

* PyTelegramBotAPI

**AI & Machine Learning:**

* Google Gemini API (Primary AI Provider)
* OpenRouter API (Fallback Provider)
* Groq API (Fallback Provider)
* Gemini 2.5 Flash
* DeepSeek Chat V3
* Llama 3.3 70B Versatile
* OpenAI Whisper Speech-to-Text

**Database:**

* SQLite

**Architecture:**

* Modular service-based architecture
* Multi-provider AI routing
* Automatic failover system
* Prompt routing system
* Contextual memory handling
* Mode-based conversational design

**Additional Tools:**

* GitHub
* VS Code
* FFmpeg
* Replit (Deployment)


______________________________________________________________________________________________________________

## Target Users

KindVoice UA is designed primarily for:

Ukrainians experiencing wartime stress or anxiety
Internally displaced people (IDPs)
Teenagers and young adults seeking emotional support
Individuals experiencing panic or loneliness
Users needing calm conversational grounding during crisis situations

The project especially focuses on accessibility, simplicity, and emotional comfort for users who may not have immediate access to professional support systems.