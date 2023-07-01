import os
import json
import argparse
from dotenv import load_dotenv
from langchain.llms import OpenAI
from scoreAnalysis import getParameterScoreAnalysis , getSubParameterScoreAnalysis

parser = argparse.ArgumentParser()
parser.add_argument("--conversation", type=str, default="conversation.txt", help="Add path to the conversation file")
parser.add_argument("--user", type=str, help="Name of the Participant")
args = parser.parse_args()

load_dotenv()

def load_file(file_path):
    _, ext = os.path.splitext(file_path)
    if ext == '.json':
        with open(file_path, "r") as f:
            return json.load(f)
    elif ext == '.txt':
        with open(file_path, "r") as f:
            return f.read().strip()
    else:
        raise ValueError('Invalid file extension. Only .json and .txt are supported.')


def calculate_scores(EthicsReport, conversation, llm, user):
    TotalScore = 0.0
    for i , parameter in enumerate(EthicsReport['Parameters']):
        ParamScore = 0.0
        paramData = None
        for j , subparameter in enumerate(parameter['SubParameters']):
            subParamData= None
            while subParamData == None:
                subParamData= getSubParameterScoreAnalysis(user=user, 
                                                        conversation=conversation, 
                                                        EthicsReport=EthicsReport, 
                                                        paramIdx=i, 
                                                        subParamIdx=j, 
                                                        llm=llm)
            subparameter['SubParameterScore'] = float(subParamData['SubParameterScore'])
            subparameter['SubParameterAnalysis'] = subParamData['SubParameterAnalysis']
            ParamScore += float(subParamData['SubParameterScore'])
        parameter['ParameterScore'] = ParamScore
        TotalScore += ParamScore
        while paramData == None:
            paramData = getParameterScoreAnalysis(user=user, 
                                            conversation=conversation, 
                                            EthicsReport=EthicsReport, 
                                            paramIdx= i, 
                                            llm=llm)
        parameter['ParameterAnalysis'] = paramData['ParameterAnalysis']
        print(f"Parameter= {parameter['ParameterName']}\nScore= {parameter['ParameterScore']}\nAnalysis= {parameter['ParameterAnalysis']}\n\n")
    return TotalScore


def main():

    with open('promptTemplate.json' , "r") as f:
        EthicsReport = json.load(f)
    conversation = load_file(args.conversation)

    llm= OpenAI(temperature=0.2)
    EthicsReport['participant'] = args.user

    TotalScore = calculate_scores(EthicsReport, conversation, llm, args.user)
    EthicsReport['TotalScore'] = TotalScore / 5

    with open('report/EthicsReport.json' , "w") as f:
        json.dump(EthicsReport , f , indent=4)

if __name__ == "__main__":
    main()
