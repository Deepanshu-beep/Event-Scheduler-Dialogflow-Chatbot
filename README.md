## Installation

Clone the repository and install the dependencies using [Poetry](https://python-poetry.org/) (you might have to [install Poetry](https://python-poetry.org/docs/#installation) first).

```bash
git clone https://github.com/Deepanshu-beep/Event-Scheduler-Dialogflow-Chatbot
cd textbase
poetry shell
poetry install
```
## Dialogflow Setup

Start here: https://cloud.google.com/dialogflow/
1. Head over to [DialogFlow console](https://dialogflow.cloud.google.com/) and create a new Project.
2. Create a new agent as per use case.
3. Move on to Intents section as specify the: Expressions for training, Actions & Parameters, and their corresponding responses.
4. Train your chatbot.
5. Enable API for Google Calendar, Google Dialogflow from Google Cloud console.
6. Create a new Google calendar with credentials JSON created after setting up above step.
7. Head back to Dialogflow console and click on Fulfillment and enable inline editor.
8. Copy the content of credentials json inside service_account.
9. Setup [Google cloud CLI](https://cloud.google.com/sdk/docs/install) and complete the setup as per wiki to authenticate your session.

## Start development server

Run the following command:

```bash
poetry run python textbase/textbase_cli.py test main.py
```

Now go to [http://localhost:4000](http://localhost:4000) and start chatting with your bot! The bot will automatically reload when you change the code.

## Demo

You can find a working demo of the chatbot [here](https://drive.google.com/file/d/1Gj2M7Lg62rauaZrhPtUD3eueprpHayuw/view?usp=sharing).
