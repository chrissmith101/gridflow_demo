import streamlit as st
from datetime import datetime

st.set_page_config(page_title="GridFlow Decision Validator", layout="centered")

st.title("GridFlow™ — Operations Decision Validation")
st.caption("Safety • Commercial • Lean Operations Support")

st.divider()

st.subheader("Unit Context")
line_id = st.text_input("Line / Area ID", "1")
previous_product = st.text_input("Previous Product", "ULSD")
target_product = st.text_input("Target Product / Spec", "Jet A")

st.divider()

st.subheader("Current Operating Conditions")
alarm_rate = st.radio("Alarm rate elevated?", ["No", "Yes"])
instrument_health = st.radio("Instrument health concern?", ["No", "Yes"])
staffing = st.radio("Operations staffing tight?", ["No", "Yes"])
recent_upset = st.radio("Recent upset in last 24h?", ["No", "Yes"])

st.divider()

st.subheader("Proposed Action")
action = st.text_area(
    "One-sentence description of the proposed action",
    "Proceed with cutpoint adjustment under enhanced monitoring"
)

if st.button("Run Decision Validation"):
    risk_score = 0

    if alarm_rate == "Yes":
        risk_score += 1
    if instrument_health == "Yes":
        risk_score += 1
    if staffing == "Yes":
        risk_score += 1
    if recent_upset == "Yes":
        risk_score += 1

    st.divider()
    st.subheader("Result")

    if risk_score <= 1:
        recommendation = "PROCEED"
        color = "green"
        rationale = "Low operational risk. Conditions acceptable."
    elif risk_score == 2:
        recommendation = "PROCEED WITH CONTROLS"
        color = "orange"
        rationale = "Moderate risk. Additional monitoring required."
    else:
        recommendation = "DO NOT PROCEED"
        color = "red"
        rationale = "Elevated risk. Stabilize conditions first."

    st.markdown(
        f"""
        **Risk Score:** {risk_score} / 4  
        **Recommendation:** :{color}[{recommendation}]  
        **Rationale:** {rationale}
        """
    )

    st.divider()
    st.caption(
        f"Decision logged — {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}"
    )
