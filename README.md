# Ethics Conversation Analysis System

This repository is home to the Ethics Conversation Analysis System, a comprehensive suite of scripts and files designed to scrutinize and evaluate conversations based on predefined ethical parameters. The output of the analysis is a detailed report assessing the ethics of conversation participants.

## Overview of Repository Contents

This project is organized into various files, each serving a unique role:

1. **scoreAnalysis.py**: This script encompasses the functions `getSubParameterScoreAnalysis` and `getParameterScoreAnalysis` that are used to calculate scores for each parameter and subparameter from the ethics report.
2. **getReport.py**: A script responsible for synthesizing an overall ethics report using the data analysis provided by `scoreAnalysis.py`. This script takes a conversation transcript and participant names as inputs, delivering the report in a JSON format.
3. **conversation.txt**: A sample conversation that can be processed by the system for analysis.

Moreover, the project features HTML, CSS, and JS files, required for the web-based report visualization, and example PDFs reports derived from the `conversation.txt` file.

## Prerequisites

Ensure the following are installed:

- Python 3.6 or later versions
- Packages including `python-dotenv`, `openai`, `langchain`, and `jinja2`.

## Usage

Follow the steps below to setup and run the system:

### Installation Guide

1. **Establish a Virtual Environment**:

   Choose an appropriate directory for your project. Navigate to this directory in the terminal and execute the following command to instantiate a new virtual environment:

   ```bash
   python3 -m venv venv
   ```

   Note: Replace `venv` with your chosen name for the virtual environment.

2. **Activate the Virtual Environment**:

   Launch the environment using:

   - Windows:

     ```bash
     venv\Scripts\activate
     ```
   - Unix or MacOS:

     ```bash
     source venv/bin/activate
     ```

3. **Install the Required Packages**:

   While your virtual environment is active, install the necessary packages using pip. For ease of installation, a `requirements.txt` file is provided:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure OpenAI API Key**:

   To leverage the power of OpenAI GPT, you need to specify your OpenAI API Key. [Use this link to create an OpenAI API key](https://platform.openai.com/account/api-keys) if you haven't already. Add the key to your `.env` file:

   ```env
   OPENAI_API_KEY="your-openai-api-key"
   ```

5. **Initiate the Report Generation**:
   
   Run the `getReport.py` script to generate the entire ethics report. You will need to provide the path to the conversation file (default is `conversation.txt`) and the name of the user.

   ```bash
   python getReport.py --user <Name of the User> --conversation <path to the conversation file>
   ```

6. **Visualize the Report**:
   
   To view the report, navigate to the report folder in the repository. After executing the `getReport.py` file, look for the `ethicsReport.json` file. If it is present, start a local web server:

   ```bash
   python -m http.server
   ```
   
   This initiates a local web server, accessible via the link `http://localhost:8000`.
