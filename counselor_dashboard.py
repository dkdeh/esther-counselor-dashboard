import streamlit as st
import json
import os

st.set_page_config(page_title="Counselor Dashboard", layout="centered")
st.title("👨‍🏫 Counselor Dashboard: Support Esther’s Journey")

profile_path = "data/esther_profile.json"
result_path = "data/esther_ai_results.json"  # optional future AI outputs

if os.path.exists(profile_path):
    with open(profile_path) as f:
        profile = json.load(f)
else:
    st.error("Esther's profile not found. Please ensure the survey has been completed.")
    st.stop()

# Display Summary
st.header("Student Profile Summary")
st.markdown(f"**Name:** {profile.get('name', '')}")
st.markdown(f"**Grade:** {profile.get('grade', '')} — **School:** {profile.get('school_name', '')}")
st.markdown(f"**Career Interest:** {profile.get('career_interest', '')}")
st.markdown(f"**Favorite Subject:** {profile.get('favorite_subject', '')}")

# Academic Planning Tips
st.header("Academic Guidance")
st.markdown("""
Help Esther align her interests with academic goals. Suggestions:
- Encourage courses related to her career interest
- Identify community programs, internships, or mentors
- Connect her with opportunities for summer exploration
""")

# AI-generated guidance (optional future feature)
if os.path.exists(result_path):
    with open(result_path) as f:
        ai_results = json.load(f)
    st.subheader("🔹 AI Recommendations")
    st.success(ai_results.get("counselor_guidance", "No AI guidance available yet."))
else:
    st.info("AI-driven recommendations will appear here once processed.")

# Contact Log (future feature)
st.header("📝 Counselor Notes")
st.text_area("Record your notes or next actions here (manual)", height=200)

st.markdown("---")
st.caption("Counselor Dashboard | Esther AI Journey")
