import streamlit as st
from groq import Groq

st.title("✈️ AI Travel Deal Finder")

departure = st.text_input("Departure City")
destination = st.text_input("Destination City")

if st.button("Find Best Deal"):

    if departure == "" or destination == "":
        st.warning("Please fill all fields.")
    else:
        st.info("Searching best deals...")

        client = Groq(api_key=st.secrets["GROQ_API_KEY"])


        query = f"""
        Find the best travel package deal from {departure} to {destination}.
        Include price, itinerary, duration, discounts and booking link.
        """

        response = client.chat.completions.create(
            messages=[{"role": "user", "content": query}],
            model="llama3-8b-8192"
        )

        st.success("Best Deal Found:")
        st.write(response.choices[0].message.content)
