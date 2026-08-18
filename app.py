import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Configuration ---
st.set_page_config(
    page_title="Sample Management & Audit | AS IS vs TO BE",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom Styling ---
st.markdown("""
<style>
    .metric-card {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 15px;
        border-left: 5px solid #000;
        margin-bottom: 10px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 16px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# --- Title Header ---
st.title("📦 Sample Management & Audit Dashboard")
st.subheader("AS-IS Scenario vs. TO-BE Scenario (On 3.0 SS28 / SS29 Framework)")
st.markdown("---")

# --- Key Metric Highlights ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="STS PO Seasonal Savings", value="$206,677", delta="-35.8% Cost", delta_color="normal")
with col2:
    st.metric(label="Liability Cost Reduction", value="$108,375", delta="-36% Waste", delta_color="normal")
with col3:
    st.metric(label="Dev Sample Savings", value="$40,144", delta="-39.3% Cost", delta_color="normal")
with col4:
    st.metric(label="Execution Phase Compression", value="230 Days", delta="-34 Days vs AS IS", delta_color="normal")

st.markdown("---")

# --- App Tabs ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🗓️ Timeline & Milestones", 
    "📦 6-Cluster Requirements", 
    "⚙️ Operational Governance", 
    "💰 Cost & ROI Analysis",
    "📊 Style & Logic Breakdown"
])

# ==========================================
# TAB 1: TIMELINE & MILESTONES
# ==========================================
with tab1:
    st.header("🗓️ Timeline Integration & Process Evolution")
    st.caption("Comparing current GTM & Creation calendars against On 3.0 (SS28/SS29)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.error("### AS IS Scenario (Legacy)")
        st.markdown("""
        * **Pacing & Execution Phase:** Extended **264-day** execution timeline from FDR to FLR.
        * **Material Commitment:** Late fabric bookings (around LR2) lead to 'blind buying' bulk material for testing/STS before commercial needs are frozen.
        * **STS Delivery Window:** Arrives over a prolonged **2–3 month window**, causing overlap friction across Ecom, Trade, and Campaigns.
        * **Photo Sample Risk:** Marketing shoots unconfirmed STS samples; late updates post-LR2 cause high retouching costs and missed launch dates.
        * **Sample Round Overlaps:** High seasonal overlap causes team burnout and redundant ordering across LR1, LR2, and FLR.
        """)
        
    with col2:
        st.success("### TO BE Scenario (On 3.0 SS28/SS29)")
        st.markdown("""
        * **Compressed Execution:** Compressed to **230 days** with shorter, sharper review cycles.
        * **Decoupled Materials:** Material toolbox locked upfront at **Initial Design Review (IDR)** prior to Brief Sign-Off (BSO).
        * **Streamlined STS Delivery:** Aligned delivery dates tied directly to Buy Ready and Commercial Briefings.
        * **TOP/PPS Shooting Strategy:** Shift Ecom and Campaign shoots away from unconfirmed STS samples to **Top of Production (TOP) / Pre-Production Samples** for 100% accuracy.
        * **Brief Sign-Off = Contract to Execute:** Reduces late-stage changes and rework loops downstream.
        """)

    st.markdown("### 📅 SS28 Creation Calendar Key Dates")
    timeline_data = {
        "Milestone": ["Brand Week", "Brief Sign-Off (BSO)", "Initial Design Review (IDR)", "Final Design Review (FDR)", "Line Review 1 (LR1)", "Line Review 2 (LR2)", "Final Line Review (FLR)"],
        "AS IS Target (SS27)": ["June 13th", "Jan 16th", "Feb 6th", "March 12th", "May 28th", "Sept 11th", "Dec 1st"],
        "TO BE Target (SS28)": ["Jan 12-16th", "May 6th", "May 27th", "June 24th", "Sept 16th", "Dec 2nd", "Feb 10th"],
        "Focus / Key Deliverable": [
            "Aligned vision & goals",
            "Contract & accountability locked",
            "Seasonal material library frozen",
            "Designs locked & handed to creation",
            "P1 validated - prove it works",
            "P2 validated - fit & colors confirmed, STS ordered",
            "Adopt or Drop decision locked"
        ]
    }
    st.table(pd.DataFrame(timeline_data))

# ==========================================
# TAB 2: 6-CLUSTER REQUIREMENTS
# ==========================================
with tab2:
    st.header("📦 Sample Requirements Consolidation")
    st.markdown("Transitioning from **19 scattered sample requirements** into **6 core functional clusters**.")
    
    clusters = {
        "Cluster 1: Vision / Range Assessment": {
            "Scope": "LR1 & Previews",
            "Owner": "Product Strategy & Merch",
            "Purpose": "Initial functional prototypes, high-level feasibility, early key account feedback."
        },
        "Cluster 2: Refinement / Feedback": {
            "Scope": "LR2 & Prelines",
            "Owner": "Product Creation & Regional Merch",
            "Purpose": "Fit refinement, material/color confirmation, commercial readiness review."
        },
        "Cluster 3: Adoption / Early Content": {
            "Scope": "FLR & Range Alignments",
            "Owner": "Product Strategy & GTM",
            "Purpose": "Final collection adoption, range freezing, lookbook teasers."
        },
        "Cluster 4: Commercial / Marketing Assets": {
            "Scope": "Tim Lookbook & GTM Content Pack",
            "Owner": "Design & Marketing Ops",
            "Purpose": "Sell-in assets, commercial education, showtime thumbnails. *(Merged with Cluster 3 effective SS29)*"
        },
        "Cluster 5: IP / Archive": {
            "Scope": "IP, Heritage, CFM & Swiss Engineering",
            "Owner": "Archive Team (Meret Horn)",
            "Purpose": "Permanent storage, legal IP protection, design history."
        },
        "Cluster 6: Marketing / Campaigns": {
            "Scope": "Events, Seeding, Campaigns, Editorials, Ecom, Athlete Shoots",
            "Owner": "Marketing PMs & Studio Teams",
            "Purpose": "Consumer-facing assets, campaign activation, PR."
        }
    }
    
    selected_cluster = st.selectbox("Select a Cluster to Inspect:", list(clusters.keys()))
    info = clusters[selected_cluster]
    
    c1, c2, c3 = st.columns(3)
    c1.info(f"**Scope:** {info['Scope']}")
    c2.warning(f"**Primary Owner:** {info['Owner']}")
    c3.success(f"**Purpose:** {info['Purpose']}")

    st.markdown("---")
    st.subheader("🔄 Sample Ordering Logic Strategy")
    st.write("Shifting from reactive 'blind ordering' to standardized rules based on style type:")
    st.markdown("""
    * **Totally New (TN) & Style Updates (SU):** Order 1 proto sample per style/stage (shared across teams). New colorways and graphics move to **Digital Twins**.
    * **Carry Over (CO):** Physical sample ordering drastically reduced; showcase via digital assets or existing library items.
    * **Size-Set Samples:** Shift to **Digital Pattern Approvals** for existing silhouettes/patterns.
    """)

# ==========================================
# TAB 3: OPERATIONAL GOVERNANCE
# ==========================================
with tab3:
    st.header("⚙️ Central Sample Governance Hub & Operational Feasibility")
    
    col1, col2 = st.columns(2)
    with col1:
        st.error("### AS IS Friction Points")
        st.markdown("""
        * **Zero Accountability:** Samples go missing ('have legs'); unreleased IP worn publicly before launch.
        * **Storage Issues:** Secure storage lacking in regional offices (e.g., London using bike locks on doors; no washing capabilities).
        * **Manual Processing:** Unpacking and sorting 3,500+ seasonal samples requires CHF 60k/year in freelance support.
        * **Data Flow Barriers:** RFID integration assessed as **not feasible** without ERP master data flowing first and placing formal POs.
        """)
        
    with col2:
        st.success("### TO BE Governance Hub Solution")
        st.markdown("""
        * **Core Rule:** *"Move People to the Product, Not Product to the People."*
        * **Secure Access:** Badge-access locked room managed by a dedicated **Archive Manager**.
        * **Barcode Tagging (OnCode):** Feasible barcode scanning system implemented at factory origin for check-in/out tracking.
        * **Library Ecosystem:** Digital catalog search first. Physical check-outs generate automated liability flags for overdue items.
        * **Consolidated Ops:** Unified sample hub servicing Marketing, Commercial, VM, and Design out of one central space.
        """)

# ==========================================
# TAB 4: COST & ROI ANALYSIS
# ==========================================
with tab4:
    st.header("💰 Financial Impact & Savings Projections")
    st.markdown("Quantified savings per season achieved by deploying digital tools and updated ordering logic.")
    
    # Financial Comparison Chart
    cost_data = pd.DataFrame({
        "Category": ["STS PO Amount", "STS Material Liabilities", "Development Samples"],
        "AS IS Cost ($)": [576721, 250000, 102195],
        "TO BE Projected ($)": [370044, 141625, 62051]
    })
    cost_data["Savings ($)"] = cost_data["AS IS Cost ($)"] - cost_data["TO BE Projected ($)"]
    
    fig = px.bar(
        cost_data, 
        x="Category", 
        y=["AS IS Cost ($)", "TO BE Projected ($)"],
        barmode="group",
        title="Cost Comparison by Category (per Season in USD)",
        color_discrete_sequence=["#e74c3c", "#2ecc71"]
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Summary Table of Savings")
    st.dataframe(cost_data.style.format({
        "AS IS Cost ($)": "${:,.2f}",
        "TO BE Projected ($)": "${:,.2f}",
        "Savings ($)": "${:,.2f}"
    }), use_container_width=True)

# ==========================================
# TAB 5: STYLE BREAKDOWN
# ==========================================
with tab5:
    st.header("📊 Development Footprint & Style Type Ratio")
    st.caption("Distribution based on 2027SP Apparel sample data analysis")
    
    style_df = pd.DataFrame({
        "Style Type": ["Style Update (SU)", "Totally New (TN)", "Carry Over (CO)", "Concept (CN)", "Design Update (DU)", "Material Update (MU)"],
        "Percentage": [48.74, 37.80, 6.48, 4.08, 2.66, 0.24]
    })
    
    fig_pie = px.pie(
        style_df, 
        values="Percentage", 
        names="Style Type", 
        title="Seasonal Style Type Distribution (%)",
        hole=0.4,
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.plotly_chart(fig_pie, use_container_width=True)
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
        **Key Takeaways:**
        * **48.7%** of styles are updates (SU) where physical sample counts can be minimized via digital twins.
        * **6.5%** are Carry Overs (CO), which can be almost entirely handled digitally or via existing archive sets.
        * Focusing physical samples strictly on **Totally New (37.8%)** yields immediate cost and space relief.
        """)
