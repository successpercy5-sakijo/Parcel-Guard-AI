import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

## Page Heading
st.set_page_config(page_title="Box Damage Detector", page_icon="📦", layout="centered")
st.title("📦 Box Damage Detector")
st.write("Upload a photo or take one with your camera to check if a box is damaged or intact.")

## Load model once and cache it
@st.cache_resource
def get_model():
    return load_model("box_damage_classifier_mobilenet.keras")

classifier = get_model()

IMG_SIZE = (160, 160)


def predict(pil_image: Image.Image):
    img = pil_image.convert("RGB").resize(IMG_SIZE)
    arr = image.img_to_array(img) / 255.0
    arr = np.expand_dims(arr, axis=0)
    val = classifier.predict(arr, verbose=0)[0][0]
    label = "Intact" if val >= 0.5 else "Damaged"
    confidence = val if label == "Intact" else 1 - val
    return label, confidence


## Upload and camera menu
tab1, tab2 = st.tabs(["📁 Upload Image", "📷 Camera"])

with tab1:
    uploaded_file = st.file_uploader("Choose a box image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded image", use_container_width=True)

        label, confidence = predict(img)
        if label == "Damaged":
            st.error(f"🔴 Prediction: **{label}**  (confidence: {confidence:.1%})")
        else:
            st.success(f"🟢 Prediction: **{label}**  (confidence: {confidence:.1%})")

with tab2:
    camera_photo = st.camera_input("Take a photo of the box")
    if camera_photo is not None:
        img = Image.open(camera_photo)

        label, confidence = predict(img)
        if label == "Damaged":
            st.error(f"🔴 Prediction: **{label}**  (confidence: {confidence:.1%})")
        else:
            st.success(f"🟢 Prediction: **{label}**  (confidence: {confidence:.1%})")

st.markdown("---")
st.caption("Model: MobileNetV2 transfer learning · Trained on box_damage_detector dataset")