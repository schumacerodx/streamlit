from streamlit.script_run_context import get_script_run_ctx
from streamlit.server.server import Server
import streamlit as st

session_id = get_script_run_ctx().session_id
session_info = Server.get_current()._get_session_info(session_id)
headers = session_info.ws.request.headers

headers = headers._dict

st.title("Hello Headers!")
st.balloons()
st.write(str(headers))
