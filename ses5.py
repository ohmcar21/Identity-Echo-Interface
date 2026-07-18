from pathlib import Path
from urllib.parse import quote

import requests
import streamlit as st


def build_image_url(prompt: str) -> str:
    encoded_prompt = quote(prompt.strip(), safe="")
    return f"https://image.pollinations.ai/prompt/{encoded_prompt}"


def save_image_bytes(image_bytes: bytes, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("wb") as handle:
        handle.write(image_bytes)


st.set_page_config(page_title="Image Generator", page_icon="🖼️")
st.title("Image Generator")

prompt = st.text_input("Enter a prompt for the image:", placeholder="e.g. a futuristic city at sunset")

if st.button("Generate Image"):
    if not prompt.strip():
        st.warning("Please enter a prompt first.")
    else:
        url = build_image_url(prompt)
        st.info(f"Generating your image for: {prompt}")

        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
        except requests.RequestException as exc:
            st.error(f"Failed to download image: {exc}")
            raise

        output_path = Path("goat.png")
        save_image_bytes(response.content, output_path)
        st.success(f"Image generated successfully and saved as {output_path}")
        st.image(output_path)

        with open(output_path, "rb") as handle:
            st.download_button(
                label="Download image",
                data=handle.read(),
                file_name=output_path.name,
                mime="image/png",
            )