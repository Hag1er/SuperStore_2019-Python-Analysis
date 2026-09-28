# 00. Libraries Importing

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# 01. Page Configuration
st.set_page_config(
    page_title="Superstore Data Analysis Project",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 02. Theme Settings
bg_color = "#FFFFFF"
text_color = "#1E293B"
secondary_text = "#48525F"
card_bg = "#F8FAFC"
border_color = "#E2E8F0"
chart_template = "plotly_white"
header_color = "#1E3A8A"
sales_color = "#3182CE"
profit_color = "#0E67B9"

st.markdown(
    f"""
    <style>
    /* Main Application */
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}

    /* Main Header */
    .main-header {{
        font-size: 30px;
        font-weight: 700;
        color: {header_color};
        margin-bottom: 5px;
    }}

    /* Sub Header */
    .sub-header {{
        font-size: 16px;
        color: {secondary_text};
        margin-bottom: 20px;
    }}

    /* KPI Cards */
    [data-testid="stMetric"] {{
        background-color: {card_bg};
        padding: 16px;
        border-radius: 10px;
        border: 1px solid {border_color};
    }}

    /* KPI Labels */
    [data-testid="stMetricLabel"] {{
        color: {secondary_text};
    }}

    /* KPI Values */
    [data-testid="stMetricValue"] {{
        color: {text_color};
    }}

    /* Sidebar */
    section[data-testid="stSidebar"] {{
        background-color: {card_bg};
    }}

    section[data-testid="stSidebar"] * {{
        color: {text_color};
    }}

    /* Sidebar Divider */
    section[data-testid="stSidebar"] hr {{
        border-color: {border_color};
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# 04. Data Loading & Preprocessing

@st.cache_data
def load_data(file_path):

    xls = pd.ExcelFile(file_path)

    orders = pd.read_excel(xls, "Orders")
    people = pd.read_excel(xls, "People")
    returns = pd.read_excel(xls, "Returns")

    # Rename columns
    orders = orders.rename(
        columns={
            "Sub-Category": "Sub Category",
            "Country/Region": "Country"
        }
    )

    # Postal Code
    orders["Postal Code"] = (
        orders["Postal Code"]
        .fillna("05401")
        .astype(str)
    )

    # Remove duplicate returns
    returns_clean = returns.drop_duplicates()

    # Merge Orders + People
    merged_df = pd.merge(
        orders,
        people,
        on="Region",
        how="left"
    )

    # Merge with Returns
    df = pd.merge(
        merged_df,
        returns_clean,
        on="Order ID",
        how="left"
    )

    # Returned Status
    df["Returned"] = df["Returned"].fillna("No")

    # Discount Percentage
    df["Discount_Percentage"] = (
        df["Discount"] * 100
    ).astype(int)

    # Total Cost
    df["Total Cost"] = (
        df["Sales"] - df["Profit"]
    )

    # Profit Margin
    df["Profit Margin"] = (
        df["Profit"] / df["Sales"]
    ) * 100

    # Shipping Duration
    df["Shipping Duration"] = (
        df["Ship Date"] - df["Order Date"]
    ).dt.days

    # Date Features
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month

    df["YearMonth"] = (
        df["Order Date"]
        .dt.to_period("M")
        .astype(str)
    )

    return df

# 05. Load Dataset
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "Datasets", "Superstore 2019-rawdata.xls")

try:
    df = load_data(file_path)
except Exception as e:

    st.error(f"❌ Error loading dataset: {e}")
    st.stop()

# 06. Sidebar Filters

# st.sidebar.image("C:/Users/uo/DataAnalysis_Projects/Python_Projects/Depi_miniProject/superstore_notebook/docs/Supermarket Photos - Download Free High-Quality Pictures _ Freepik.jfif", width=100)
st.sidebar.title("🛒 Superstore Dashboard")
st.sidebar.markdown("---")

# Year Filter
years = ["All"] + sorted(
    list(df["Year"].unique())
)
selected_year = st.sidebar.selectbox(
    "Choose Year",
    years
)
# Region Filter
regions = ["All"] + list(
    df["Region"].unique()
)
selected_region = st.sidebar.selectbox(
    "Choose Region",
    regions
)
# State Filter
states = ["All"] + list(
    df["State"].unique()
)
selected_state = st.sidebar.selectbox(
    "Choose State",
    states
)
# Category Filter
categories = ["All"] + list(
    df["Category"].unique()
)
selected_category = st.sidebar.selectbox(
    "Choose Category",
    categories
)
# segments Filter
segments = ["All"] + list(
    df["Segment"].unique()
)
selected_segment = st.sidebar.selectbox(
    "Choose Customer-Segment",
    segments
)
# 07. Apply Filters
filtered_df = df.copy()
if selected_year != "All":

    filtered_df = filtered_df[
        filtered_df["Year"] == selected_year
    ]
if selected_region != "All":

    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]
if selected_category != "All":

    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]
if selected_segment != "All":

    filtered_df = filtered_df[
        filtered_df["Segment"] == selected_segment
    ]
if selected_state != "All":

    filtered_df = filtered_df[
        filtered_df["State"] == selected_state
    ]
# 08. Main Header
st.markdown(
    """
    <div class="main-header">
        📊 Superstore Performance Dashboard
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class="sub-header">
        Hover over any chart to inspect detailed business metrics and insights.
    </div>
    """,
    unsafe_allow_html=True
)
# 09. KPI Scorecard
kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

# Total Revenue
kpi1.metric(
    "Total Revenue",
    f"${filtered_df['Sales'].sum():,.0f}"
)
# Net Profit
kpi2.metric(
    "Net Profit",
    f"${filtered_df['Profit'].sum():,.0f}"
)

# Average Profit Margin
kpi3.metric(
    "Avg Profit Margin",
    f"{filtered_df['Profit Margin'].mean():.1f}%"
)

# Total Orders
kpi4.metric(
    "Total Orders",
    f"{filtered_df['Order ID'].nunique():,}"
)
# Returned Orders
kpi5.metric(
    "Total Returned Orders",
    f"{filtered_df[filtered_df['Returned'] == 'Yes']['Order ID'].nunique():,}"
)

st.markdown("---")

# Chart 1: Profit by State
state_map = (
    df.groupby("State", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

fig_map = px.choropleth(
    state_map,
    locations="State",
    locationmode="USA-states",
    color="Profit",
    scope="usa",
    color_continuous_scale=[
        "#DBEAFE",
        "#93C5FD",
        "#60A5FA",
        "#3B82F6",
        "#1D4ED8"
    ],
    hover_data={
        "State": True,
        "Sales": ":,.0f",
        "Profit": ":,.0f"
    },
    labels={
        "Profit": "Total Profit ($)",
        "Sales": "Total Sales ($)"
    },
    title="Profit by State"
)

fig_map.update_layout(
    template=chart_template,
    height=500,
    margin=dict(l=20, r=20, t=60, b=20)
)

st.plotly_chart(
    fig_map,
    use_container_width=True
)

# Chart 2: Sales vs Profit by Category
col_left, col_right = st.columns(2)

with col_left:
    cat_summary = (
        filtered_df
        .groupby("Category")[["Sales", "Profit"]]
        .sum()
        .reset_index()
    )

    cat_summary["Insight"] = cat_summary["Category"].map({

        "Technology":
            "Top revenue & profit driver (15.6% margin).",

        "Office Supplies":
            "High order volume with stable profitability.",

        "Furniture":
            "Low margin (3.8%) due to heavy discounts & shipping costs."
    })
    fig_cat = px.bar(
        cat_summary,
        x="Category",
        y=["Sales", "Profit"],
        barmode="group",
        title="Sales vs. Profit by Product Category",
        labels={
            "value": "USD ($)",
            "variable": "Metric"
        },
        hover_data=["Insight"],
        color_discrete_map={
            "Sales": sales_color,
            "Profit": profit_color
        }
    )

    fig_cat.update_layout(
        template=chart_template,
        height=350,
        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20
        )
    )
    st.plotly_chart(
        fig_cat,
        use_container_width=True
    )

# Chart 2: Monthly Revenue Trend

with col_right:
    monthly_trend = (
        filtered_df
        .groupby("YearMonth")[["Sales", "Profit"]]
        .sum()
        .reset_index()
    )
    monthly_trend["Insight"] = (
        "Q4 seasonal spike driven by holiday sales volume."
    )


    fig_trend = px.line(
        monthly_trend,
        x="YearMonth",
        y="Sales",
        title="Monthly Revenue Trend Over Time",
        markers=True,
        hover_data=[
            "Profit",
            "Insight"
        ],
        color_discrete_sequence=[
            sales_color
        ]
    )

    fig_trend.update_layout(
        template=chart_template,
        height=350,
        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20
        ),
        xaxis_title="Month"
    )
    st.plotly_chart(
        fig_trend,
        use_container_width=True
    )


# Chart 3: Sub-Category Profit Ranking
col_prod, col_geo = st.columns(2)
with col_prod:

    sub_summary = (
        filtered_df
        .groupby("Sub Category")[["Sales", "Profit"]]
        .sum()
        .reset_index()
    )

    top_sub = (
        sub_summary
        .sort_values(
            by="Sales",
            ascending=False
        )
        .head(5)
    )

    bottom_sub = (
        sub_summary
        .sort_values(
            by="Profit",
            ascending=True
        )
        .head(5)
    )
    fig_sub = px.bar(
        sub_summary.sort_values(
            by="Profit",
            ascending=True
        ),
        x="Profit",
        y="Sub Category",
        orientation="h",
        title="Sub-Category Net Profit Ranking",
        color="Profit",
        color_continuous_scale="RdYlGn",
        hover_data=["Sales"]
    )


    fig_sub.update_layout(
        template=chart_template,
        height=380,
        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20
        )
    )
    st.plotly_chart(
        fig_sub,
        use_container_width=True
    )

# Chart 4: Geographic Performance
with col_geo:

    state_summary = (
        filtered_df
        .groupby("State")[["Sales", "Profit"]]
        .sum()
        .reset_index()
    )
    top10_states = (
        state_summary
        .sort_values(
            by="Profit",
            ascending=False
        )
        .head(10)
    )
    top10_states["Insight"] = (
        "California and New York lead profitability nationwide."
    )
    fig_geo = px.bar(
        top10_states,
        x="Profit",
        y="State",
        orientation="h",
        title="Top 10 Most Profitable States",
        color="Sales",
        color_discrete_sequence=[
        "#1D4ED8",
        "#2563EB",
        "#3B82F6",
        "#60A5FA",
        "#7CB8FD",
        "#2563EB",
        "#3B82F6",
        "#60A5FA",
        "#88C0FF",
        "#A8CEFC"
    ],
        hover_data=[
            "Sales",
            "Insight"
        ]
    )
    fig_geo.update_layout(

        template=chart_template,
        height=380,
        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20
        ),
        yaxis=dict(
            autorange="reversed"
        )
    )

    st.plotly_chart(
        fig_geo,
        use_container_width=True
    )



# Chart 5: Shipping Mode Performance
col_ship, col_ret = st.columns(2)
with col_ship:
    ship_summary = (
        filtered_df
        .groupby("Ship Mode")
        .agg(
            Order_Count=(
                "Order ID",
                "nunique"
            ),
            Avg_Days=(
                "Shipping Duration",
                "mean"
            )
        )
        .reset_index()
    )

    # Round average shipping days
    ship_summary["Avg_Days"] = (
        ship_summary["Avg_Days"]
        .round(1)
    )
    # Insights
    ship_summary["Insight"] = (
        ship_summary["Ship Mode"].map({
            "Standard Class":
                "Highest usage with longer delivery time.",
            "Second Class":
                "Moderate usage with faster delivery.",
            "First Class":
                "Fast delivery with shorter transit time.",
            "Same Day":
                "Fastest delivery option."
        })
    )

    # Sort from fastest to slowest
    ship_summary = ship_summary.sort_values(
        by="Avg_Days",
        ascending=True
    )

    # Create Chart
    fig_ship = px.bar(

        ship_summary,
        x="Ship Mode",
        y="Order_Count",
        title="Ship Mode Performance",
        color="Avg_Days",
        color_discrete_sequence=[
    "#64A8FA",
    "#509EF7",
    "#60A5FA",
    "#3B82F6"
],
        labels={
            "Order_Count": "Total Orders",
            "Avg_Days": "Avg Days to Ship"
        }
    )

    # Chart Layout
    fig_ship.update_layout(
        template=chart_template,
        height=350,
        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20
        ),
        xaxis_title="Ship Mode",
        yaxis_title="Total Orders",
        coloraxis_colorbar=dict(
            title="Avg Days"
        )
    )

    st.plotly_chart(
        fig_ship,
        use_container_width=True
    )

# Chart 6: Returns Distribution

with col_ret:
    returned_df = filtered_df[
        filtered_df["Returned"] == "Yes"
    ]
    returns_summary = (
        returned_df
        .groupby("Category")["Order ID"]
        .nunique()
        .reset_index(
            name="Returned_Orders"
        )
    )
    returns_summary["Insight"] = (
        "Office Supplies registers the highest absolute return counts."
    )

    fig_ret = px.pie(
        returns_summary,
        names="Category",
        values="Returned_Orders",
        title="Returned Orders Number by Category",
        hole=0.4,
        hover_data=["Insight"],
        color_discrete_sequence=px.colors.sequential.Blues_r
    )
    fig_ret.update_layout(
        template=chart_template,
        height=350,
        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20
        )
    )
    st.plotly_chart(
        fig_ret,
        use_container_width=True
    )

    