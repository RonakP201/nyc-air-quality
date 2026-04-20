import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="NYC Air Quality Dashboard", page_icon="🌫️")

df = pd.read_csv("data/cleaned_air_quality.csv")
df["Year"] = pd.to_datetime(df["Start_Date"]).dt.year

st.sidebar.title("🌇 Filters")
locations = st.sidebar.multiselect("📍 Location", sorted(df["Location"].unique()))
pollutants = st.sidebar.multiselect("🧪 Pollutant", sorted(df["Pollutant"].unique()))
year_range = st.sidebar.slider("📅 Year Range", int(df["Year"].min()), int(df["Year"].max()), (2010, 2020))


filtered_df = df[
    (df["Year"] >= year_range[0]) & (df["Year"] <= year_range[1])
]
if locations:
    filtered_df = filtered_df[filtered_df["Location"].isin(locations)]
if pollutants:
    filtered_df = filtered_df[filtered_df["Pollutant"].isin(pollutants)]

st.sidebar.markdown("---")
st.sidebar.subheader("📊 Quick Stats")
if not filtered_df.empty:
    avg_value = filtered_df["Value"].mean()
    max_row = filtered_df.loc[filtered_df["Value"].idxmax()]
    st.sidebar.metric("📈 Avg Level", f"{avg_value:.2f}")
    st.sidebar.metric("🚨 Highest Level", f"{max_row['Value']:.2f}")
    st.sidebar.write(f"📌 Location: {max_row['Location']}")
    st.sidebar.write(f"🧪 Pollutant: {max_row['Pollutant']}")
else:
    st.sidebar.warning("No data available for selected filters.")

st.title("🌫️ NYC Air Quality Dashboard")
st.markdown("This dashboard helps explore air pollutant trends across New York City using interactive filters and charts.")

kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("📂 Total Records", len(filtered_df))
kpi2.metric("📍 Unique Locations", filtered_df["Location"].nunique())
kpi3.metric("🧪 Pollutants Tracked", filtered_df["Pollutant"].nunique())

st.markdown("---")


col1, col2 = st.columns(2)

if not filtered_df.empty:
    # Line chart
    yearly_df = filtered_df.groupby(["Year", "Pollutant"])["Value"].mean().reset_index()
    fig1 = px.line(yearly_df, x="Year", y="Value", color="Pollutant", markers=True,
                   title="📉 Yearly Average Pollutant Levels")
    fig1.update_layout(legend_title="Pollutant", plot_bgcolor="#F5F5F5")
    col1.plotly_chart(fig1, use_container_width=True)

    # Bar chart - Top 10 Locations
    top_locations = filtered_df.groupby("Location")["Value"].mean().nlargest(10).reset_index()
    fig2 = px.bar(top_locations, x="Location", y="Value", color="Value", title="🏙️ Top 10 Polluted Locations",
                  color_continuous_scale="Reds")
    fig2.update_layout(xaxis_tickangle=45, plot_bgcolor="#F5F5F5")
    col2.plotly_chart(fig2, use_container_width=True)
else:
    st.warning("No charts to display. Adjust the filters to load data.")
