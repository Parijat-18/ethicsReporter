from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
import json

load_dotenv()

llm = OpenAI(temperature=0.8)

def getSubParameterScoreAnalysis(user, conversation , EthicsReport , paramIdx , subParamIdx , llm=llm):

    parameter = EthicsReport['Parameters'][paramIdx]['ParameterName']
    parameterDefinition = EthicsReport['Parameters'][paramIdx]['ParameterDefinition']
    subparameter = EthicsReport['Parameters'][paramIdx]['SubParameters'][subParamIdx]
    rules = EthicsReport['Rules']


    template = """
    Your task is to analyse and then score `{{user}}` for how ethical his/her \
    conversation was based on the parameter `{{parameter}}` to {{parameterDefinition}}. The conversation is given \
    between the triple backticks:
    "
    Conversation: ```{{conversation}}```
    "

    Below is the subparameter in a json format between triple backticks ``` which you need to score \
    between 0 and 1 with 0.5 being neutral by following the rules. \
    "
    Subparameter: ``` {{subparameter}} ```
    "

    Follow the rules given between triple backticks accurately to analyze and score each subparameter:
    "
    Rules: ```{{rules}}```
    "

    Process to Follow:"
    Step 1: Create a deep understanding analysis of {user} by following the rules laid out above, \
    subparameter definition and subparameter Question. \
    Step 2: Generate the analysis for the conversation based on that subparameter. Follow the rules, \
    subparameter definition and subparameter question. \
    Step 3: Generate the subparameter score based on your analysis. The analysis should give precise \
    reasons with examples. \
    Step 4: Summarize the subparameter analysis in less than 50 words. And stick to this rule \
    Step 5: The response should be a dictionary with the keys `SubParameterScore` and `SubParameterAnalysis`.
    "

    Please return a dictionary in the following format:
    "
    {
        'SubParameterName': '<Name of the subparameter>',
        'SubParameterScore': '<score>',
        'SubParameterAnalysis': '<analysis>'
    }
    "
    Note: Replace '<Name of the subparameter>', '<score>', and '<analysis>' with the actual values.
    """

    prompt = PromptTemplate(input_variables=["user", "parameter", "parameterDefinition", "conversation", "subparameter", "rules"],
                        template=template, 
                        template_format="jinja2"
                    )
    
    chain = LLMChain(llm=llm , prompt=prompt)
    try:
        response = chain.run(
            user=user,
            parameter=parameter,
            parameterDefinition=parameterDefinition,
            conversation= conversation,
            subparameter= subparameter,
            rules=rules
        )
        lines = response.split('\n')

        response = {}
        for line in lines:
            if line and ': ' in line:
                key, value = line.split(': ', 1)
                key = key.strip().strip("'")
                value = value.strip().strip("',")
                response[key] = value
        
        return response
    except:
        print('Failed to retrieve a response. Try Again...\n')
        return None



def getParameterScoreAnalysis(user, conversation , EthicsReport , paramIdx, llm=llm):

    parameter = EthicsReport['Parameters'][paramIdx]['ParameterName']
    parameterDefinition = EthicsReport['Parameters'][paramIdx]['ParameterDefinition']
    subparameters = EthicsReport['Parameters'][paramIdx]['SubParameters']
    rules = EthicsReport['Rules']


    template = """
        Your task is to analyse the conversation of `{{user}}` based on the parameter `{{parameter}}` to {{parameterDefinition}}. \
        The conversation is given between the triple backticks:
        "
        Conversation: ```{{conversation}}```
        "

        You are provided with the analyses of the subparameters in a json format between triple backticks which you need to use to generate \
        the final parameter analysis.:
        "
        Subparameters: ``` {{subparameters}} ```
        "

        Follow the rules given between triple backticks accurately to analyze the parameter:
        "
        Rules: ```{{rules}}```
        "

        Process to Follow:"
        Step 1: Review the analyses of each subparameter. \
        Step 2: Consider the conversation and the subparameter analyses to generate the final analysis for the parameter. \
        Step 3: The response should be a dictionary with the keys `ParameterName` and `ParameterAnalysis`.
        "

        Please return a dictionary in the following format:
        "
        {
            'ParameterName': '<Name of the parameter>',
            'ParameterAnalysis': '<analysis>'
        }
        "
        Note: Replace '<Name of the parameter>' and '<analysis>' with the actual values.
        """


    prompt = PromptTemplate(input_variables=["user", "parameter", "parameterDefinition", "conversation", "subparameters", "rules"],
                        template=template, 
                        template_format="jinja2"
                    )
    
    chain = LLMChain(llm=llm , prompt=prompt)
    try:
        response = chain.run(
            user=user,
            parameter=parameter,
            parameterDefinition=parameterDefinition,
            conversation= conversation,
            subparameters= subparameters,
            rules=rules
        )

        lines = response.split('\n')

        response = {}
        for line in lines:
            if line and ': ' in line:
                key, value = line.split(': ', 1)
                key = key.strip().strip("'")
                value = value.strip().strip("',")
                response[key] = value
        
        return response
    except:
        print('Failed to retrieve a response. Try Again...\n')
        return None






if __name__ == "__main__":
    pass
