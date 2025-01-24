# LLM Response Optimizer

## Overview
The **LLM Response Optimizer** is a Python-based tool designed to streamline and automate the process of improving responses from large language models (LLMs). It takes an initial user prompt, enhances it to elicit better results, and iteratively refines the generated responses using multiple LLMs, including OpenAI's GPT-4, Google's Gemini, DeepSeek, and Anthropic's Claude.

This program was created to address the repetitive and time-consuming process of manually improving prompts and responses, enabling users to obtain high-quality outputs in a fraction of the time.

---

## Features
- **Automated Prompt Improvement:** Uses GPT-4 to refine the user-provided prompt for better clarity and effectiveness.
- **Iterative Response Refinement:** Processes the response through multiple LLMs, each improving it in terms of accuracy, completeness, and clarity.
- **Multi-Model Pipeline:** Leverages the unique strengths of different LLMs (GPT-4, Gemini, DeepSeek, and Claude) to achieve a high-quality final result.
- **Error Handling:** Includes robust error handling to ensure reliability across different stages of the pipeline.

---

## How It Works
1. The user enters a prompt.
2. GPT-4 improves the prompt to maximize response quality.
3. The improved prompt generates an initial response via GPT-4.
4. The response is iteratively enhanced using:
   - **Google Gemini** for accuracy, clarity, and completeness.
   - **DeepSeek** for further refinement.
   - **Anthropic Claude** for final optimization.
5. The final improved response is displayed to the user.

---

## Dependencies
To use this program, you need:

### Python Libraries
- `openai` (for GPT-4 integration)
- `google-generativeai` (for Google Gemini integration)
- `anthropic` (for Claude integration)
- `requests` (for DeepSeek API requests)
- `python-dotenv` (to manage environment variables)
- `logging` (for centralized error and status messages)

Install the dependencies using pip:
```bash
pip install openai google-generativeai anthropic requests python-dotenv
```

### Environment Variables
Set the following environment variables in a `.env` file to configure API keys:
```
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
DEEPSEEK_API_KEY=your_deepseek_api_key
```
Ensure the `.env` file is in the root directory of the project.

---

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/llm-response-optimizer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd llm-response-optimizer
   ```
3. Create and populate the `.env` file with your API keys.
4. Run the program:
   ```bash
   python main.py
   ```
5. Enter a prompt when prompted. The tool will process it and output the final optimized response.

---

## Why This Tool?
As someone who frequently interacts with LLMs, I often find myself manually refining prompts and responses to achieve the best results. While this process is effective, it can be repetitive and time-consuming. By automating the workflow, this tool saves me time by ensuring consistency in generating high-quality outputs that have been check by multiple different models. 
