from autogen import OpenAIWrapper, AssistantAgent, UserProxyAgent, ChatCompletion

config_list = [
    {
        "model": "gpt-4",
        "api_key": "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",
    }
]

client = OpenAIWrapper(config_list=config_list)

assistant = AssistantAgent(
    name="assistant",
    system_message="You are a brilliant and very helpful assistant. Reply TERMINATE when the task is done",
    llm_config=
    {
        "seed": 41,
        "config_list": config_list
    }
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    max_consecutive_auto_reply=1,
    human_input_mode="NEVER",
    code_execution_config={"work_dir":"_output" },
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE")
)

def handleChatMessages(messages):
    all_msgs = [item for sublist in messages.values() for item in sublist]
    return all_msgs

def use_autogen(user_prompt):
    #to initiate conversation with user
    chat_messages = []
    try:
        user_proxy.initiate_chat(assistant, message=user_prompt)
        print(user_proxy.chat_messages[user_proxy])
        chat_messages = handleChatMessages(user_proxy.chat_messages)
    except:
        print('error using autogen')

    return chat_messages
