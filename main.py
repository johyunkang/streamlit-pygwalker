import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import pygwalker as pyg
# streamlit run main.py --server.port 8505


st.set_page_config(page_title='PyGWalker App', layout='wide')


def load_data(data):
    return pd.read_csv(data)

def main():
    st.title('PyGWalker App by jo')

    menu = ['PyGWalker', '참조링크']
    menu_selected = st.sidebar.selectbox("Menu", menu)
    if menu_selected == 'PyGWalker':

        with st.form("upload_form"):
            uploaded_file = st.file_uploader("csv 파일을 업로드하세요", type=["csv"])
            submitted = st.form_submit_button('Submit')

            if submitted:
                df_data = load_data(uploaded_file)
                

                # PyGWalker Visualize
                pyg_html = pyg.walk(df_data, return_html=True)
                stc.html(pyg_html, scrolling=True, height=1000)

                st.markdown(' ## 업로드 파일 DataFrame')
                st.dataframe(df_data)
    elif menu_selected == '참조링크':
        st.subheader('PyGWalker 참조 링크')
        st.markdown(' - [PyGWalker 공식 페이지](https://docs.kanaries.net/ko/pygwalker/index)')
        st.markdown(' - [Github](https://github.com/Kanaries/pygwalker) ')
        st.markdown(' - [PyGWalker 와 Streamlit 이용방법](https://docs.kanaries.net/ko/pygwalker/use-pygwalker-with-streamlit)')


if __name__ == "__main__":
    main()
