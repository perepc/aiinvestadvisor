# AI Invest Advisor

This is a basic company invest advisor, powered by [crewAI](https://crewai.com).

It is very simple. You just start the application by executing

``` bash
streamlit run src/aiinvestadvisor/main.py
```

You put a company you want the AI Invest Advisor to analyze and it will do for you. Follow the advice at your own risk. :-)

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:

```bash
poetry lock
```

```bash
poetry install
```

### Customizing

I developed the application using Groq, so you need to add your Groq API key into the .env file

## Running the Project

I created a simple Streamlit application and can be started by executing:

```bash
streamlit run src/aiinvestadvisor/main.py
```

You can also modify the same ```main.py``` to set your own parameters inside the ```run()``` function and execute as Poetry script:

```bash
poetry run aiinvestadvisor
```

Both commands initialize the aiinvestadvisor Crew, assembling the agents and assigning them tasks as defined in the configuration.

## Understanding Your Crew

The crewailab Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Crewailab Crew or crewAI.

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
