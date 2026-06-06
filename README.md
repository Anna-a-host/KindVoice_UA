# KindVoice UA 💙💛

## Problem Statement
Millions of Ukrainians experience stress, panic, isolation, and emotional exhaustion caused by war, displacement, uncertainty, and constant exposure to danger. While professional psychological support is crucial, it is often inaccessible, expensive, unavailable at night, or difficult to reach during sudden crisis situations.

At the same time, many individuals simply need a calm, human-like presence, emotional grounding, and a safe space to talk in moments of intense fear or loneliness.

**KindVoice UA** was created to address this issue by providing accessible, multilingual, emotionally supportive AI conversations directly inside **Telegram** — a platform already integrated into the daily lives of millions of Ukrainians. 

*Remember: This project does not aim to replace professional therapy, but rather to offer immediate emotional support, calming communication, and grounding interaction during acute stress situations.*

---

## Solution Overview

**KindVoice UA** is an AI-powered Telegram companion designed to provide emotionally adaptive conversations for users experiencing trauma, wartime anxiety, and emotional overwhelm. 

### Key Architectural Solutions:
* **Multi-Provider AI Resilience:** To maximize uptime and cost-efficiency on a free tier, the backend features a robust **automatic failover system**. It prioritizes **Groq** as the primary provider and dynamically routes traffic to **OpenRouter** or **Gemini** if API quotas are exceeded or connections drop.

* **Multimodal Webhook Delivery:** Users can interact seamlessly via both text and voice. 

* **Dynamic Contextual Memory:** The bot maintains a lightweight, rolling 8-message conversation memory, preserving recent user context while strictly protecting performance limits.

* **Data storage:** Integrates a serverless **PostgreSQL (Neon)** database to handle user states and anonymously track support engagement metrics.

* **Webhook Deployment:** Implements a modern webhook-based architecture hosted on **Render**, eliminating the latency and resource drain of traditional polling frameworks.

---

## Emotional Adaptation Modes

The system dynamically adapts its conversational behavior, empathy levels, and response formatting based on the specific emotional mode selected by the user:

* **Panic Support** (Acute crisis intervention)
* **Wartime Situations** (Direct coping mechanisms for ongoing danger)
* **Anxiety Support** (Stress reduction and breathing cues)
* **Emotional Grounding** (Somatic and environmental awareness)
* **Calm Conversation** (Casual, distracting, friendly dialog)
* **Support for IDPs** (Targeted empathy for internally displaced people)

---

## Technologies Used

* **Programming Language:** Python 
* **Backend & Bot Framework:** PyTelegramBotAPI, Flask (Webhook Handler)
* **Databases:** PostgreSQL (Hosted via Neon Serverless Postgres)
* **Cloud AI Providers:** 
  * Groq Cloud API (Primary Engine & Audio Transcriptions)
  * Google Gemini API (First Fallback)
  * OpenRouter API (Secondary Fallback)
* **AI Models Integrated:**
  * `llama-3.3-70b-versatile` (via Groq)
  * `whisper-large-v3` (via Groq Audio API)
  * `gemini-2.5-flash` (via Google Gemini API)
  * `deepseek/deepseek-chat-v3-0324` (via OpenRouter)
* **Deployment & Environments:** Render, Git/GitHub, VS Code

---

## Target Users
KindVoice UA is built with safety, privacy, and accessibility in mind for:
1. Ukrainians coping with chronic wartime stress, rocket attacks, or anxiety.
2. Internally Displaced Persons (IDPs) navigating relocation and isolation.
3. Teenagers and young adults looking for an anonymous, non-judgmental space to express difficult feelings.
4. Individuals needing rapid, localized mental grounding techniques when professional care is unavailable.

---

## Inspiration
My project was deeply inspired by the desire to help people living in Ukraine who unfortunately have to cope with panic, fear, stress, and emotional exhaustion on a regular basis because of the war. Being Ukrainian myself, I realize how desperate the need for emotional support can be when experiencing an attack. While KindVoiceUA is not intended to replace professional psychological support, I believe it can become a small source of comfort and emotional grounding for people during difficult moments.

I wanted to create something accessible, human, and supportive — a space where people could feel heard even when they feel alone. I also strongly believe that even if this project helps just one Ukrainian feel calmer, safer, or less isolated, then it is already deeply meaningful.
