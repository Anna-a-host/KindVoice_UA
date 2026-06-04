## Problem Statement

Millions of Ukrainians experience stress, panic, isolation, and emotional exhaustion caused by war, displacement, uncertainty, and constant exposure to danger. While professional psychological support is important, it is often inaccessible, expensive, unavailable at night, or difficult to reach during crisis situations.

At the same time, many people simply need calm human-like presence, emotional grounding, and someone to talk to in moments of fear or loneliness.

KindVoice UA was created to address this issue by providing accessible, multilingual, emotionally supportive AI conversations directly inside Telegram — a platform already widely used by Ukrainians daily.

The project focuses not on replacing therapy, but on offering immediate emotional support, calming communication, and safe conversational interaction during stressful situations.
______________________________________________________________________________________________________________

## Solution Overview

KindVoice UA is an AI-powered Telegram bot designed to provide emotionally adaptive conversations for users experiencing stress, panic, wartime anxiety, loneliness, or emotional overwhelm.

The bot uses multiple AI providers with automatic failover to improve reliability and availability. Conversations are generated using Gemini as the primary AI provider, with OpenRouter and Groq serving as fallback providers when needed.

Users can interact through both text and voice messages in Ukrainian or English.

The system dynamically adapts its conversational behavior depending on the emotional mode selected by the user, such as:

panic support
anxiety support
wartime situations
emotional grounding
calm conversation
support for internally displaced people (IDPs)

Voice messages are processed using Groq's Whisper speech-to-text model before being passed to the AI conversation pipeline.

To improve realism and reduce repetitive or irrelevant responses, the bot maintains lightweight rolling conversation memory that preserves recent context while remaining efficient for deployment.

The project includes a PostgreSQL database hosted on Neon for persistent user management and analytics. 

The bot is deployed using webhook-based architecture, allowing continuous operation without requiring a local machine to stay online.
______________________________________________________________________________________________________________

## Key Features

Emotionally Adaptive Conversations
Multilingual Support (Ukrainian & English)
Voice Message Transcription
Contextual Memory
Multi-Provider AI Reliability
Telegram Accessibility in Ukraine
Persistent PostgreSQL User Database
Webhook-Based Deployment
Human-Centered Design

______________________________________________________________________________________________________________

## Technologies Used

**Programming Language:**

Python

**Backend & Bot Framework:**

PyTelegramBotAPI

**AI & Machine Learning:**

Google Gemini API (Primary AI Provider)
OpenRouter API (Fallback Provider)
Groq API (Fallback Provider)

**AI Models used:**

Gemini 2.5 Flash
DeepSeek Chat V3
Llama 3.3 70B Versatile
Whisper Large V3 Speech-to-Text

**Database:**

PostgreSQL (Neon Serverless PostgreSQL)

**Architecture:**

Modular service-based architecture
Multi-provider AI routing
Automatic failover system
Prompt routing system
Contextual memory handling
Mode-based conversational design
Webhook-based Telegram bot architecture

**Deployment & Tools:**

Render (Deployment)
GitHub (Pushed code)
VS Code (Local project)
PostgreSQL (Neon Database)

______________________________________________________________________________________________________________

## Target Users

KindVoice UA is designed primarily for:

Ukrainians experiencing wartime stress or anxiety
Internally displaced people (IDPs)
Teenagers and young adults seeking emotional support
Individuals experiencing panic or loneliness
Users needing calm conversational grounding during difficult situations

The project focuses on accessibility, reliability, privacy-conscious data handling, and emotional comfort for users who may not have immediate access to professional support systems.

______________________________________________________________________________________________________________


## Inspiration

My project was deeply inspired by the desire to help people living in Ukraine who unfortunately have to cope with panic, fear, stress, and emotional exhaustion on a regular basis because of the war. Being Ukrainian myself, I realise how desperate the need for emotional support can be when experiencing an attack. While KindVoiceUA is not intended to replace professional psychological support, I believe it can become a small source of comfort and emotional grounding for people during difficult moments.

I wanted to create something accessible, human, and supportive — a space where people could feel heard even when they feel alone. I also strongly believe that even if this project helps just one Ukrainian feel calmer, safer, or less isolated, then it is already meaningful.