import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps

# Load the trained model
model = tf.keras.models.load_model('mnist_model.h5')

st.title("MNIST Digit Recognition")
st.write("Upload a black digit on white background. The model will predict the digit from 0 to 9.")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("L")  # Convert to grayscale
    image = ImageOps.invert(image)                  # Invert to match MNIST format
    image = ImageOps.fit(image, (28, 28), method=Image.Resampling.LANCZOS)  # Resize + center

    st.image(image, caption="Processed Image", width=150)

    img_array = np.array(image).astype("float32") / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)

    st.subheader(f"Predicted Digit: {predicted_class}")


