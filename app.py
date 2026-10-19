from __future__ import annotations

import streamlit as st


def calculate_powers(value: int) -> dict[str, int]:
    """Calculate the square, cube, and fifth power of an integer."""
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("value must be an integer")
    return {"square": value**2, "cube": value**3, "fifth_power": value**5}


def main() -> None:
    st.set_page_config(page_title="Power Calculator", page_icon="🔢")
    st.title("Power Calculator")
    st.write("Enter an integer to calculate its square, cube, and fifth power.")
    value = st.number_input("Integer", value=1, step=1)
    results = calculate_powers(int(value))
    st.metric("Square", results["square"])
    st.metric("Cube", results["cube"])
    st.metric("Fifth power", results["fifth_power"])


if __name__ == "__main__":
    main()
