# Personal Agent

A Python-based intelligent meeting assistant that integrates with your calendar to help you prepare, conduct, and follow up on meetings. Built using LangChain, LangGraph, and Ollama for local LLM execution.

## Features

- **Calendar Integration**: Read and analyze your calendar meetings from ICS files
- **Meeting Preparation**: Research meeting topics using web search and generate preparation notes
- **File Management**: Create and save meeting notes as Markdown files
- **Date Intelligence**: Smart date handling for calendar queries (today, tomorrow, etc.)
- **Local LLM**: Uses Ollama for privacy-focused AI processing

## Tools & Capabilities

The agent comes equipped with several tools:

- **Calendar Tools**: Fetch upcoming meetings from your calendar
- **Date Tools**: Get current date and handle date-based queries
- **Filesystem Tools**: Create and save Markdown files locally
- **Web Search**: Research meeting topics using DuckDuckGo search

## Installation

### Requirements

- Python >= 3.12
- Ollama installed locally
- An ICS calendar file

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd personal_agent
```

2. Install dependencies using uv (recommended) or pip:
```bash
# Using uv
uv sync

# Or using pip
pip install -e .
```

3. Install and setup Ollama:
```bash
# Install Ollama (macOS)
brew install ollama

# Pull the required model
ollama pull gpt-oss
```

4. Create a `.env` file in the root directory:
```env
CALENDAR_PATH=/path/to/your/calendar.ics
FILES_FOLDER_PATH=/path/to/save/notes
```

## Usage

### Command Line Interface

Run the interactive CLI:

```bash
python src/personal_agent/main.py
```

The agent will start an interactive session where you can ask questions like:
- "What meetings do I have today?"
- "Prepare notes for my 2 PM meeting"
- "Show me all meetings this week"

### LangGraph Integration

The project is configured to work with LangGraph CLI:

```bash
# Install LangGraph CLI
pip install langgraph-cli

# Run the graph
langgraph dev
```

## Project Structure

```
personal_agent/
├── src/personal_agent/
│   ├── agent.py          # Main agent implementation
│   ├── main.py           # CLI entry point
│   └── tools/            # Agent tools
│       ├── calendar_tools.py    # Calendar integration
│       ├── date_tools.py        # Date utilities
│       └── filesystem_tools.py  # File operations
├── prompts/              # System prompts
├── pyproject.toml        # Python project configuration
├── langgraph.json        # LangGraph configuration
└── README.md
```

## Configuration

### Environment Variables

- `CALENDAR_PATH`: Path to your ICS calendar file
- `FILES_FOLDER_PATH`: Directory where meeting notes will be saved

### Model Configuration

The agent uses the "gpt-oss" model by default with a temperature of 0.2. You can modify these settings in `main.py` or `agent.py`.

## Examples

### Getting Today's Meetings
```
You: What meetings do I have today?
Agent: Based on your calendar, you have the following meetings today:

| Time | Meeting |
|------|---------|
| 09:00-09:30 | Daily Standup |
| 14:00-15:00 | Project Review |
```

### Preparing for a Meeting
```
You: Help me prepare for my project review meeting
Agent: I'll research the project review topic and create preparation notes for you.
[Agent searches web and creates a markdown file with relevant information]
```

## Dependencies

- **langchain**: Core LLM framework
- **langchain-ollama**: Ollama integration
- **langchain-community**: Community tools including DuckDuckGo search
- **langgraph**: Graph-based agent framework
- **icalendar**: ICS calendar file parsing
- **ddgs**: DuckDuckGo search functionality
- **python-dotenv**: Environment variable management
