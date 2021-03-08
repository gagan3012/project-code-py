import torch
import streamlit as st
from transformers import GPT2Tokenizer, GPT2LMHeadModel

st.set_page_config(
    page_title="AI Leetcode",
    layout="wide",
    initial_sidebar_state="expanded", )


@st.cache(suppress_st_warning=True)
def modelgpt(sequence, temp, top_p):
    tokenizer = GPT2Tokenizer.from_pretrained("gagan3012/project-code-py-small")
    model = GPT2LMHeadModel.from_pretrained("gagan3012/project-code-py-small")
    inputs = tokenizer.encode(sequence, return_tensors='pt')
    outputs = model.generate(inputs, max_length=1024, do_sample=True, temperature=temp, top_p=top_p)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text

def display():
    st.write('# Using AI to Generate Leetcode solutions')
    st.sidebar.write('## Options:')
    tokens = st.sidebar.slider(label='Number of Tokens', min_value=1, max_value=15, value=3, step=1)
    samples = st.sidebar.slider(label='Number of Samples', min_value=1, max_value=9, value=9, step=1)
    top_p = st.sidebar.slider(label='Top k', min_value=0.0, max_value=40.0, value=1.0, step=1.0)
    temp = st.sidebar.slider(label='Temperature', min_value=0.1, max_value=1.0, value=1.0, step=0.05)
    st.sidebar.markdown(
        '''
        `Number of Tokens:` number of tokens in generated text\n
        `Number of Samples:` number of samples to return total\n
        `Temperature:` Float value controlling randomness in boltzmann distribution. Lower temperature results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive. Higher temperature results in more random completions.\n
        `Top k:` Integer value controlling diversity. 1 means only 1 word is considered for each step (token), resulting in deterministic completions, while 40 means 40 words are considered at each step. 0 (default) is a special setting meaning no restrictions. 40 generally is a good value.
        ''')

    st.write('## Enter Leetcode Question:')
    sequence = st.text_area("", value='""" Write a function to delete a node in a singly-linked '
                                      'list. You will not be given access to the head of the '
                                      'list, instead you will be given access to the node to be '
                                      'deleted directly. It is guaranteed that the node to be '
                                      'deleted is not a tail node in the list.')
    if st.button("Get Answer"):
        text = modelgpt(sequence, temp, top_p)
        st.code(text.encode().decode('unicode_escape'), language='python')

    st.markdown(
        '''
        This is a demo of a text generation model trained with GPT-2 to generate LeetCode Answers in Python

        *For additional questions and inquiries, please contact Gagan Bhatia via [LinkedIn](
        https://www.linkedin.com/in/gbhatia30/) or [Github](https://github.com/gagan3012).*
        ''')


if __name__ == '__main__':
    display()
