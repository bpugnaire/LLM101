import os

from dotenv import load_dotenv

from langchain.llms import OpenAI

from langchain.chat_models import ChatOpenAI

from langchain.prompts.chat import HumanMessagePromptTemplate, ChatPromptTemplate

from pydantic import BaseModel, Field

from langchain.output_parsers import PydanticOutputParser

class Country(BaseModel):
    capital: str = Field(description='capital of the country')
    gastronomy: str = Field(description='national dish of the country')
    name: str = Field(description='capital of the country')

load_dotenv()

OPENAI_MODEL = 'gpt-3.5-turbo'
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

PROMPT_TEMPLATE = """
    Give me infos about {country}. 
    {format_instruction}
    """

def main():
    # llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model=OPENAI_MODEL)

    # set up parser
    parser = PydanticOutputParser(pydantic_object=Country)

    # user input
    country_name = input('Enter the name of a country : ')

    # result = llm.predict(text="Give me 5 conversation starters about AI")
    message = HumanMessagePromptTemplate.from_template(PROMPT_TEMPLATE)

    chat_prompt = ChatPromptTemplate.from_messages(messages=[message])
    
    chat_prompt_with_value = chat_prompt.format_prompt(
        country=country_name, format_instruction=parser.get_format_instructions()
        )
    
    responses = llm(chat_prompt_with_value.to_messages())
    
    data = parser.parse(responses.content)

    # print the result
    
    print(data)

if __name__ == '__main__':
    main()