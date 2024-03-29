import random
import time

import streamlit as st
import s3fs


def store_guess(guess):
    st.session_state.guess = guess
    st.session_state.counter += 1


def image_url(image_type, image_number):
    if image_type == "real":
        url = f"s3://innova-conicet-examples/eagle_galrand_64x64/img{image_number:08d}.png"
    else:
        url = f"s3://innova-conicet-examples/00010-stylegan3-r-eagle-64x64-gpus2-batch32-gamma0.5/seed{image_number:04d}.png"

    return url


def main():

    st.set_page_config(
        page_title="Is this galaxy real?",
        page_icon=":telescope:"
    )
    st.title(":telescope: Is this galaxy real or fake?")

    if 'counter' not in st.session_state:
        st.session_state.counter = 0
        st.session_state.correct_answers = 0

    image_type = random.choice(["real", "fake"])
    image_number = random.randint(0, 45578)

    url = image_url(image_type, image_number)

    left, right = st.columns(2)
    image_placeholder = left.empty()

    with right:
        real_button = st.empty()
        real_button.button("Real", on_click=store_guess, args=["real"],disabled=True,
                           key="real_disabled")
        fake_button = st.empty()
        fake_button.button("Fake", on_click=store_guess, args=["fake"],disabled=True,
                           key="fake_disabled")
        metric_placeholder = st.empty()
        msg_placeholder = st.empty()

    text = """The image depicts either a **real** galaxy extracted from the [EAGLE 
    simulation](https://icc.dur.ac.uk/Eagle/) or a **fake** galaxy generated by a 
    generative adversarial neural network trained to mimic the EAGLE galaxies. Can 
    you guess which is which?"""
    st.markdown(text)

    with image_placeholder:
        with st.spinner('Loading image...'):
            pass

    fs = s3fs.S3FileSystem(anon=False)
    f = fs.open(url, 'rb')

    image_placeholder.image(f.read(), use_column_width=True)
    real_button.button("Real", on_click=store_guess, args=["real"], disabled=False)
    fake_button.button("Fake", on_click=store_guess, args=["fake"], disabled=False)

    if 'guess' in st.session_state:
        if st.session_state.guess == st.session_state.image_type:
            st.session_state.correct_answers += 1
            # msg_placeholder.success("You were right")
            msg_placeholder.markdown(":heavy_check_mark: Correct!")
        else:
            msg_placeholder.markdown(":x: Wrong!")

        score = 100 * st.session_state.correct_answers / st.session_state.counter
        metric_placeholder.metric("Your score", f"{score:.1f} %")
    else:
        metric_placeholder.metric("Your score", "----")

    st.session_state.image_type = image_type


if __name__ == "__main__":
    main()
