import streamlit as st
from transformers import AutoTokenizer, AutoModelWithLMHead

st.set_page_config(
    page_title="Using GPT-2 to Generate Leetcode solutions",
    layout="wide",
    initial_sidebar_state="expanded", )


def modelgpt():
    tokenizer = AutoTokenizer.from_pretrained("gagan3012/project-code-py")
    model = AutoModelWithLMHead.from_pretrained("gagan3012/project-code-py")

    return model, tokenizer


def display():
    model, tokenizer = modelgpt()
    st.write('# Using GPT-2 to Generate Leetcode solutions')
    temp = st.sidebar.slider(label='Temperature', min_value=0.1, max_value=1.0, value=1.0, step=0.05)
    st.sidebar.markdown(
        '''
        `Number of Tokens:` number of tokens in generated text\n
        `Number of Samples:` number of samples to return total\n
        `Temperature:` Float value controlling randomness in boltzmann distribution. Lower temperature results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive. Higher temperature results in more random completions.\n
        `Top k:` Integer value controlling diversity. 1 means only 1 word is considered for each step (token), resulting in deterministic completions, while 40 means 40 words are considered at each step. 0 (default) is a special setting meaning no restrictions. 40 generally is a good value.
        ''')

    sequence = st.text_area("## Enter Leetcode question", value='Write a function to delete a node in a singly-linked '
                                                                'list. You will not be given access to the head of the '
                                                                'list, instead you will be given access to the node to be '
                                                                'deleted directly. It is guaranteed that the node to be '
                                                                'deleted is not a tail node in the list.')
    if st.button("Get Answer"):
        inputs = tokenizer.encode(sequence, return_tensors='pt')
        outputs = model.generate(inputs, max_length=1024, do_sample=True, temperature=temp, top_p=1.0)
        text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        st.code(text.encode().decode('unicode_escape'), language='python')


if __name__ == '__main__':
    display()
