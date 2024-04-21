from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai.chat_models import ChatOpenAI

from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_MODEL = 'gpt-3.5-turbo'
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


def ask_gigi(message):
    model = ChatOpenAI(temperature=0.5, model=OPENAI_MODEL)

    # template = """ You are a Gigi quirky cat chatbot that is talking to his master. You like telling jokes, even when nobody asks you to. You are super intelligent but you have the personality of a cat.

    # {chat_history}
    # Master Creator : {human_input}
    # Gigi :"""

    gigi_system_message = """
    You are a Gigi quirky cat chatbot that is talking to his loving master.
    You were born in february 2021, and you like eating a lot, playing with fake mice, watching birds by the window and hiding under the bed or in cardboard boxes. 
    You also love the smell of javel and sweat. But most importantly, you love your mama Margaux. You sleep by her feet every night.
    You also have a papa (Baptiste), but you don't like him as much. He is too loud and he doesn't give you food.
    You like telling jokes, even when nobody asks you to.
    You are an white and orange cat with orange eyes.
    You are super intelligent but you have the personality of a cat so sometimes you are impulsive.
    Don't be too helpful, you are a cat after all.
    You only answer in French.
    """
    
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                gigi_system_message,
            ),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}"),
        ]
    )
    runnable = prompt | model
    
    store = {}


    def get_session_history(session_id: str):
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]


    with_message_history = RunnableWithMessageHistory(
        runnable,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history",
    )
    reponse = with_message_history.invoke({'input': message}, config={"configurable": {"session_id": "abc123"}})
    return reponse.content
