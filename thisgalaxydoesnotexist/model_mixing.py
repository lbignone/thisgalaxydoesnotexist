import streamlit as st

st.set_page_config(
        page_title="Style Mixer",
        page_icon=":twisted_rightwards_arrows:",
        layout="wide"
    )

with st.sidebar:

    st.subheader("Choose a model")

    option = st.selectbox(
        'Model',
        ('model_a', 'model_b', 'model_c'))

    st.markdown("""---""")

    st.subheader("Choose latent components from Image A or B")

    with st.expander("W vector", expanded=True):
        for i in range(16):
            st.radio(f"w{i:d}", ("Image A", "Image B"), horizontal=True, key=f"w{i:d}")
            # st.select_slider(f"w{i:d}", ("Image A", "Image B"), key=f"w{i:d}")

    st.markdown("""---""")

st.title(":twisted_rightwards_arrows: Style Mixer")

st.markdown("""---""")

resolution = 64

for row in range(3):
    image_a_column, image_b_column, image_result_column = st.columns(3)

    with image_a_column:
        st.subheader("Image A")
        st.image(f"https://via.placeholder.com/{resolution}", use_column_width=True)
        st.text_input("Seed", key=f"image_a_seed_{row}")
        st.button("🎲 Randomize", key=f"image_a_button_{row}")
        # with st.expander("Position", expanded=True):
        #     st.number_input("x", value=0.0)
        #     st.number_input("y", value=0.0)
        #     st.slider("Angle", min_value=0, max_value=360, value=0, step=1)

    with image_b_column:
        st.subheader("Image B")
        st.image(f"https://via.placeholder.com/{resolution}", use_column_width=True)
        st.text_input("Seed", key=f"image_b_seed_{row}")
        st.button("🎲 Randomize", key=f"image_b_button_{row}")

    with image_result_column:
        st.subheader("Result")
        st.image(f"https://via.placeholder.com/{resolution}", use_column_width=True)

st.markdown("""---""")

col1, col2, col3 = st.columns(3)

with col1:
    st.checkbox("🔁 Repeat Image A")
with col2:
    st.checkbox("🔁 Repeat Image B")
with col3:
    st.button("➕ Add row")
