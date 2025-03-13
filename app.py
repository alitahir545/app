import streamlit as st
import numpy as np


def validate_marks(obtained, total):
    """Validate the marks input."""
    if obtained > total:
        return False, "Obtained marks cannot be greater than total marks"
    if obtained < 0 or total <= 0:
        return False, "Marks cannot be negative and total marks must be greater than 0"
    return True, ""


def calculate_score(obtained, total, factor):
    """Calculate score based on formula."""
    if total == 0:
        return 0
    return (obtained / total) * factor


st.set_page_config(page_title="Academic Score Calculator - KPESE",
                   page_icon="📚",
                   layout="wide")

st.title("Academic Score Calculator")
st.markdown("Calculate your academic score based on the KPESE formula")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    # SSC
    st.subheader("SSC")
    ssc_obtained = st.number_input("Obtained Marks (SSC)",
                                   min_value=0.0,
                                   max_value=1050.0,
                                   step=0.1,
                                   key="ssc_obtained")
    ssc_total = st.number_input("Total Marks (SSC)",
                                min_value=1.0,
                                value=1050.0,
                                step=0.1,
                                key="ssc_total")

    # HSSC
    st.subheader("HSSC")
    hssc_obtained = st.number_input("Obtained Marks (HSSC)",
                                    min_value=0.0,
                                    max_value=1100.0,
                                    step=0.1,
                                    key="hssc_obtained")
    hssc_total = st.number_input("Total Marks (HSSC)",
                                 min_value=1.0,
                                 value=1100.0,
                                 step=0.1,
                                 key="hssc_total")

    # BA/B.Sc
    st.subheader("BA/B.Sc")
    ba_obtained = st.number_input("Obtained Marks (BA/B.Sc)",
                                  min_value=0.0,
                                  max_value=1000.0,
                                  step=0.1,
                                  key="ba_obtained")
    ba_total = st.number_input("Total Marks (BA/B.Sc)",
                               min_value=1.0,
                               value=550.0,
                               step=0.1,
                               key="ba_total")

    # MA/M.Sc
    st.subheader("MA/M.Sc")
    ma_obtained = st.number_input("Obtained Marks (MA/M.Sc)",
                                  min_value=0.0,
                                  max_value=1100.0,
                                  step=0.1,
                                  key="ma_obtained")
    ma_total = st.number_input("Total Marks (MA/M.Sc)",
                               min_value=1.0,
                               value=1100.0,
                               step=0.1,
                               key="ma_total")

    # BS
    st.subheader("BS")
    bs_obtained = st.number_input("Obtained Marks (BS)",
                                  min_value=0.0,
                                  max_value=4400.0,
                                  step=0.1,
                                  key="bs_obtained")
    bs_total = st.number_input("Total Marks (BS)",
                               min_value=1.0,
                               value=4400.0,
                               step=0.1,
                               key="bs_total")

with col2:
    # B.ed/ADE/Shahadul Almia/Qari Sanad
    st.subheader("B.ed/ADE/Shahadul Almia/Qari Sanad")
    bed_obtained = st.number_input("Obtained Marks",
                                   min_value=0.0,
                                   max_value=1800.0,
                                   step=0.1,
                                   key="bed_obtained")
    bed_total = st.number_input("Total Marks",
                                min_value=1.0,
                                value=1800.0,
                                step=0.1,
                                key="bed_total")

    # M.ed
    st.subheader("M.ed")
    med_obtained = st.number_input("Obtained Marks (M.ed)",
                                   min_value=0.0,
                                   max_value=2000.0,
                                   step=0.1,
                                   key="med_obtained")
    med_total = st.number_input("Total Marks (M.ed)",
                                min_value=1.0,
                                value=2000.0,
                                step=0.1,
                                key="med_total")

    # BS/MA Education
    st.subheader("BS/MA Education")
    bsma_obtained = st.number_input("Obtained Marks (BS/MA Education)",
                                    min_value=0.0,
                                    max_value=4000.0,
                                    step=0.1,
                                    key="bsma_obtained")
    bsma_total = st.number_input("Total Marks (BS/MA Education)",
                                 min_value=1.0,
                                 value=4000.0,
                                 step=0.1,
                                 key="bsma_total")

    # MS/M.Phil
    st.subheader("MS/M.Phil")
    ms_obtained = st.number_input("Obtained Marks (MS/M.Phil)",
                                  min_value=0.0,
                                  max_value=1800.0,
                                  step=0.1,
                                  key="ms_obtained")
    ms_total = st.number_input("Total Marks (MS/M.Phil)",
                               min_value=1.0,
                               value=1800.0,
                               step=0.1,
                               key="ms_total")

    # Ph.D
    st.subheader("Ph.D")
    phd_obtained = st.number_input("Obtained Marks (Ph.D)",
                                   min_value=0.0,
                                   max_value=2000.0,
                                   step=0.1,
                                   key="phd_obtained")
    phd_total = st.number_input("Total Marks (Ph.D)",
                                min_value=1.0,
                                value=2000.0,
                                step=0.1,
                                key="phd_total")

if st.button("Calculate Score", type="primary"):
    # Validate all inputs
    all_inputs_valid = True
    error_messages = []

    input_pairs = [(ssc_obtained, ssc_total), (hssc_obtained, hssc_total),
                   (ba_obtained, ba_total), (ma_obtained, ma_total),
                   (bs_obtained, bs_total), (bed_obtained, bed_total),
                   (med_obtained, med_total), (bsma_obtained, bsma_total),
                   (ms_obtained, ms_total), (phd_obtained, phd_total)]

    for obtained, total in input_pairs:
        valid, message = validate_marks(obtained, total)
        if not valid:
            all_inputs_valid = False
            error_messages.append(message)

    if all_inputs_valid:
        # Calculate individual scores
        ssc_score = calculate_score(ssc_obtained, ssc_total, 15)
        hssc_score = calculate_score(hssc_obtained, hssc_total, 20)
        ba_score = calculate_score(ba_obtained, ba_total, 20)
        ma_score = calculate_score(ma_obtained, ma_total, 15)
        bs_score = calculate_score(bs_obtained, bs_total, 35)
        bed_score = calculate_score(bed_obtained, bed_total, 15)
        med_score = calculate_score(med_obtained, med_total, 5)
        bsma_score = calculate_score(bsma_obtained, bsma_total, 20)
        ms_score = calculate_score(ms_obtained, ms_total, 5)
        phd_score = calculate_score(phd_obtained, phd_total, 5)

        # Calculate total score
        total_score = sum([
            ssc_score, hssc_score, ba_score, ma_score, bs_score, bed_score,
            med_score, bsma_score, ms_score, phd_score
        ])

        # Display results
        st.success("Scores calculated successfully!")

        st.markdown("### Individual Scores")
        col3, col4 = st.columns(2)

        with col3:
            st.write("SSC Score:", f"{ssc_score:.2f}")
            st.write("HSSC Score:", f"{hssc_score:.2f}")
            st.write("BA/B.Sc Score:", f"{ba_score:.2f}")
            st.write("MA/M.Sc Score:", f"{ma_score:.2f}")
            st.write("BS Score:", f"{bs_score:.2f}")

        with col4:
            st.write("B.ed/ADE Score:", f"{bed_score:.2f}")
            st.write("M.ed Score:", f"{med_score:.2f}")
            st.write("BS/MA Education Score:", f"{bsma_score:.2f}")
            st.write("MS/M.Phil Score:", f"{ms_score:.2f}")
            st.write("Ph.D Score:", f"{phd_score:.2f}")

        st.markdown("### Total Academic Score")
        st.markdown(f"## {total_score:.2f}")

    else:
        for message in error_messages:
            st.error(message)

# Display important notes
st.markdown("---")
st.markdown("### Important Notes:")
st.markdown("""
- One professional degree will be counting from both ADE and B.ed
- One professional degree will be counting from MA.Ed/BS. Ed/B.ed/M.ed
- In case of CGPA you must bring marks equivalence certificate from concern university.
""")
