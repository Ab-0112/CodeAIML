import streamlit as st
import plotly.graph_objects as go

def run():
    st.title("📈 Resume Insights Dashboard")

    match_scores = [45, 58, 62, 70, 75, 85]
    updates = ["v1", "v2", "v3", "v4", "v5", "v6"]

    st.subheader("📊 JD Match Over Resume Versions")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=updates, y=match_scores, mode='lines+markers', name='Match %'))
    fig.update_layout(title="Resume Score Progress", xaxis_title="Resume Version", yaxis_title="Match %")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🧠 Skill Coverage Radar")
    skills = ['Python', 'SQL', 'Machine Learning', 'Excel', 'Communication', 'Leadership']
    coverage = [80, 60, 75, 90, 70, 50]

    radar = go.Figure()
    radar.add_trace(go.Scatterpolar(r=coverage, theta=skills, fill='toself', name='Your Skills'))
    radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False)
    st.plotly_chart(radar, use_container_width=True)

    st.subheader("🚨 Missing Keywords Breakdown")
    st.markdown("""
    - ❌ Docker  
    - ❌ Cloud (AWS/GCP)  
    - ❌ REST APIs  
    - ❌ Agile  
    """)
    st.info("✅ Keep enhancing your resume to close these gaps!")



