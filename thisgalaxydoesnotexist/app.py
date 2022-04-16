import random

import streamlit as st


def store_guess(guess):
    st.session_state.guess = guess
    st.session_state.counter += 1


def main():

    st.set_page_config(
        page_title="Is this galaxy real?",
        page_icon=":telescope:"
    )
    st.title("Is this galaxy real or fake?")

    if 'counter' not in st.session_state:
        st.session_state.counter = 0
        st.session_state.correct_answers = 0

    image_type = random.choice(["real", "fake"])
    urls = {
        "real": f"https://random.imagecdn.app/500/500",
        "fake": "https://via.placeholder.com/500"
    }
    url = urls[image_type]

    left, right = st.columns(2)
    left.image(url, use_column_width=True)

    with right:
        st.button("Real", on_click=store_guess, args=["real"])
        st.button("Fake", on_click=store_guess, args=["fake"])
        msg_placeholder = st.empty()
        metric_placeholder = st.empty()

    if 'guess' in st.session_state:
        if st.session_state.guess == st.session_state.image_type:
            st.session_state.correct_answers += 1
            msg_placeholder.success("You were right")
        else:
            msg_placeholder.error("You were wrong")

        score = 100 * st.session_state.correct_answers / st.session_state.counter
        metric_placeholder.metric("Your score", f"{score:.1f} %")

    st.session_state.image_type = image_type


if __name__ == "__main__":
    main()
