import textbase
from textbase.message import Message
from textbase import models
from typing import List
import uuid
from constants import project_id, language_code
from google.cloud import dialogflow


def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.
    project_id: Project ID of the project create in Google Cloud Platform.
    session_id: Unique ID of current session of conversation.
    texts: List of user messages
    language_code: Language of conversation, default: English (en)
    
    Return a string of response from bot."""

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)

    bot_response = ""

    for text in texts:
        text_input = dialogflow.TextInput(text="Hi i am traveling tomorrow.", language_code=language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        bot_response = " ".join([bot_response, response.query_result.fulfillment_text])
    
    return bot_response

# [END dialogflow_es_detect_intent_text]

@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information

    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """

    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1
    
    session_id=str(uuid.uuid4())

    bot_response = detect_intent_texts(project_id, session_id, message_history, language_code)

    return bot_response, state
