import streamlit as st
import os

def get_module():
    module = st.session_state.module
    return module

def get_PATH():
    return os.getcwd()


#def get_data_path() -> str:
    #data_path = os.path.join(get_PATH(),'data','raw', st.session_state.get(['Institute'].copy))
    #return data_path
#    pass
def get_modules():
    with open('module.txt', 'r') as f:
        return f.read().splitlines()


def reload():
    st.session_state.reload_trigger = True
    
reload()
def get_data_path():
        PATH = f'{get_PATH()}' +'/data/raw/' + st.session_state.institute +'/' + get_module() +'/'
        return PATH
def read_pdf(file_name):
    with open(file_name, "rb") as pdf_file:
        return pdf_file.read()

def does_file_exist(bytes_data , name):
    for file in os.listdir(get_data_path()):
        if upload_data.name != file:
            fc = open(get_data_path() + file, "rb")
            if fc.read() == bytes_data:
                return False, fc
    f = open(get_data_path() +  name, "wb")
    return True ,f 
# Create a download button for the PDF file


if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

FILE_PATH = os.getcwd() + '/data/raw/' + st.session_state.institute +'/'

button_css = """
<style>
div[data-testid="stButton"] button {
    font-size: 20px !important;
    padding: 10px 40px !important;
    border-radius: 15px !important
}
div[data-testid="stFileUploader"] button {
    font-size: 20px !important;
    border-radius: 15px !important
}
div[data-testid="]


p {
    padding: 8px 20px !important;
}
</style>
"""
st.markdown(button_css, unsafe_allow_html=True)
st.markdown(
    "<h1 style='text-align: center;'>Modules</h1>",
    unsafe_allow_html=True
)
st.write(get_data_path())
with open('modules.txt', 'r') as f:
    modules = f.read().splitlines()
st.divider()

with st.container():
    
    for module in modules:
        if st.session_state.logged_in:  
            if st.button(module):
                st.session_state.module = module
        else:
            col1 ,col2 = st.columns(2)
            with col1:
                if st.button(module):
                    st.session_state.module = module
            with col2:
                st.markdown("<p style='margin-top: 10px; margin-left: 12%; margin-right: 1px;'>Login to upload data<p>",unsafe_allow_html=True)
                            
if st.session_state.logged_in: 
    files = os.listdir("data/raw/"+ st.session_state.institute +'/' +get_module() +'/') 
    with st.expander(get_module() + ' Files', expanded=False, icon=':material/arrow_drop_down:'):
                col1 ,col2 = st.columns(2)
                if len(files) == 0:
                    st.write("No files found for " + get_module())
                else:
                    for file in files:
                        with col1:
                            st.write(file)
                        with col2:
                            st.download_button(
                            label="Download"+file,
                            data=read_pdf("data/raw/"+ st.session_state.institute +'/' +get_module() +'/' + file),
                            file_name=file
                    )
            
    upload_data = st.file_uploader(f'Upload PDF for {get_module()}', type=['pdf']) 
    if upload_data is not None:
        if not os.path.isfile("data/raw/"+ st.session_state.institute +'/' +get_module() +'/' + upload_data.name):
            with st.status("Analyzing your document..."):
            #ORC to find alike documents
            #meaure by binary size and store extra info if new one extentds other
                bytes_data = upload_data.read()
            not_exists, filename = does_file_exist(bytes_data, upload_data.name)
            if not_exists: 
                st.success("File uploaded successfully")
                st.switch_page('views/2Modules.py')
            else:
                st.info('File already exists but thanks for trying! ')   
            

                

            
            #loader = PyPDFLoader("files/"+get_current_Module() +'/' + uploaded_file.name+".pdf")     #+".pdf"
            #data = loader.load()

            # Initialize text splitter
            #text_splitter = RecursiveCharacterTextSplitter(
            #    chunk_size=1500,
            #    chunk_overlap=200,
            #    length_function=len
            #)
            #all_splits = text_splitter.split_documents(data)

            # Create and persist the vector store
            #st.session_state.vectorstore = Chroma.from_documents(
            #    documents=all_splits,
            #    embedding=OllamaEmbeddings(model="mistral")
            #)
            #st.session_state.vectorstore.persist()    


