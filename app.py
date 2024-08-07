import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


st.set_page_config(
    page_title="FluentData Signature Generator", initial_sidebar_state="collapsed", page_icon="favicon.ico"
)


def create_email_signature(name, role, phone, name_font_size, role_font_size, phone_font_size):
    image = Image.open("signature.png")
    draw = ImageDraw.Draw(image)
    font_name = ImageFont.truetype("./font/Poppins-Bold.ttf", name_font_size)
    font_role = ImageFont.truetype("./font/Poppins-Italic.ttf", role_font_size)
    font_phone = ImageFont.truetype("./font/Poppins-Regular.ttf", phone_font_size)

    # Name
    draw.text((975.2, 63.9), name, font=font_name, fill="white")
    # Role
    draw.text((975.2, 170), role, font=font_role, fill="white")
    # Phone
    draw.text((1068.1, 250), text=phone, font=font_phone, fill="white")

    return image


st.title("We Speak Data Fluently!")
st.subheader("Create your email signature")

signature_form = st.form(key="signature_form")
sidebar = st.sidebar

name = signature_form.text_input("Your name")
role = signature_form.text_input("Your role")
phone = signature_form.text_input("Your phone number")

# Font settings
sidebar.title("Font settings")
# TODO: Changing the sidebar values refreshes the page, which is not ideal
name_font_size = sidebar.slider("Name font size", 0, 100, 80)
role_font_size = sidebar.slider("Role font size", 0, 100, 45)
phone_font_size = sidebar.slider("Phone font size", 0, 100, 45)

submit = signature_form.form_submit_button(label="Create email signature")

if submit:
    st.markdown("### Download your signature")
    st.markdown("Click the button below to download your email signature")

    signature = create_email_signature(name, role, phone, name_font_size, role_font_size, phone_font_size)
    st.image(signature)

    # TODO: Streamlit doesn't accept this?
    # signature_bytes = Image.fromarray(signature).tobytes()

    # Convert to bytes using BytesIO
    # Source: https://stackoverflow.com/a/71669410
    signature_buf = BytesIO()
    signature.save(signature_buf, format="PNG")
    signature_bytes = signature_buf.getvalue()

    st.download_button(
        label="Download",
        data=signature_bytes,
        file_name=f"{name}_{role}_signature.png",
        mime="image/png",
    )
