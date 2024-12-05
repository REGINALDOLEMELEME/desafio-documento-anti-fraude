import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analize_credit_card

def configure_interface():
    st.title("Upload file - Challenge 1 - Azure - Fake Docs")
    upload_file = st.file_uploader("Choice one file", type=["png","jpg","jpeg"])

    if upload_file is not None:
        fileName = upload_file.name
        blob_url = upload_blob(upload_file,fileName)
        if blob_url:
            st.write(f"File{fileName} send with success to Azure Blob Storage")
            credit_card_info = analize_credit_card(blob_url)
            show_image_and_validation(blob_url,credit_card_info)
        else:
            st.write(f"Error sending  file {fileName} to Azure Blob Storage")

def show_image_and_validation(blob_url,credit_card_info):
    st.image(blob_url, caption="Image sent", use_column_width = True)
    st.write("Validation of Results")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color: green;'>Valid Card </h1>", unsafe_allow_html=True)
        st.write(f"Cardholder Name: {credit_card_info['card_name']}")
        st.write(f"Issuing bank: {credit_card_info['bank_name']}")
        st.write(f"Expiration date: {credit_card_info['expiry_date']}")
    else:
        st.markdown(f"<h1 style='color: red;'>Invalid Card </h1>", unsafe_allow_html=True)
        st.write(f"This is not a valid credit card")

if __name__ == "__main__":
    configure_interface()