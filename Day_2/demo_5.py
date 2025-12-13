import streamlit as st

if 'messages' not in st.session_state:
    st.session_state.messages=[]

st.title("My ChatBot")

with st.sidebar:
    st.header("Settings")
    choices=["Upper","Lower","Toggle"]
    mode=st.selectbox("Select mode",choices)
    count=st.slider("Messege count",1,10,5,1)

    st.subheader("Configuration")
    st.json({"Mode":mode,"Messege count":count})

msg=st.chat_input("Prompt here ...")

if msg:
    outmsg=msg 
    if mode=="Upper":
        outmsg=msg.upper()
    elif mode=="Lower":
        outmsg=msg.lower()
    elif mode=="Toggle":
        outmsg=msg.swapcase()
    
    st.session_state.messages.append(msg)
    st.session_state.messages.append(outmsg)

    msglist=st.session_state.messages
    for idx , message in enumerate(msglist):
        role="Human" if idx%2==0 else "AI"
        with st.chat_message(role):
            st.write(message)