import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.set_page_config(
    page_title="TfL Line Delay Analysis",
    layout="wide"
)

# ------------------
# 1. LOAD + CLEAN DATA
# ------------------

@st.cache_data


def load_data():
    file_path = "C:/Users/sarth/tfl-northern/raw_data/lost-customer-hours.csv"
    df = pd.read_csv(file_path)

    # Selecting key columns
    cols = ["Financial Year", "Period", "Northern", "Central", "Jubilee", "Victoria"]
    df = df[cols].copy()

    # Clean line columns: remove commas, convert to numeric
    for col in ["Northern", "Central", "Jubilee", "Victoria"]:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(",", "")
            .replace(r"^\s*$", np.nan, regex=True)
            .apply(pd.to_numeric, errors="coerce")
        )

    # Fix data types and create combined period label
    df["Financial Year"] = df["Financial Year"].astype(str)

    # Clean and cast Period column
    df["Period"] = (
        df["Period"]
        .astype(str)
        .str.strip()
        .replace(r"^\s*$", np.nan, regex=True)
        .apply(pd.to_numeric, errors="coerce")
        .fillna(0)  # OR dropna()
        .astype(int)
    )

    df["fy_period"] = df["Financial Year"] + " / P" + df["Period"].map("{:02d}".format)

    return df

# --------- LINE CHART ----------
def plot_lost_hours_line_chart(df):
    st.subheader("📉 Lost Customer Hours Over Time")

    line_options = ["Northern", "Central", "Jubilee", "Victoria"]
    selected_lines = st.multiselect("Select Tube Lines", line_options, default=line_options)

    tfl_colours = {
        "Northern": "#000000",
        "Central": "#DC241F",
        "Jubilee": "#868F98",
        "Victoria": "#00A0E2",
    }

    fig, ax = plt.subplots(figsize=(10, 6))

    for line in selected_lines:
        ax.plot(
            df["fy_period"],
            df[line],
            label=line,
            color=tfl_colours.get(line, "#333333"),
            marker="o",
        )

    ax.set_title("Lost Customer Hours by Line")
    ax.set_xlabel("Financial Year / Period")
    ax.set_ylabel("Lost Customer Hours (millions)")
    ax.legend(title="Tube Line")
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True)

    st.pyplot(fig)



def plot_annual_grouped_bar(df):
    import matplotlib.pyplot as plt

    # Group and sum data by year
    annual_df = (
        df.groupby("Financial Year")[["Northern", "Central", "Jubilee", "Victoria"]]
        .sum()
        .reset_index()
    )

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    width = 0.2
    x = np.arange(len(annual_df["Financial Year"]))

    lines = ["Northern", "Central", "Jubilee", "Victoria"]
    colors = {
        "Northern": "#000000",  # black
        "Central": "#DC241F",   # red
        "Jubilee": "#868F98",   # silver
        "Victoria": "#00A0E2",  # blue
    }

    for i, line in enumerate(lines):
        ax.bar(x + i * width, annual_df[line], width, label=line, color=colors[line])

    ax.set_xticks(x + width * (len(lines) - 1) / 2)
    ax.set_xticklabels(annual_df["Financial Year"], rotation=45)
    ax.set_title("Lost Customer Hours per Year — Grouped by Line")
    ax.set_xlabel("Financial Year")
    ax.set_ylabel("Lost Customer Hours (M)")
    ax.legend(title="Line")

    return fig


# --------- MAIN ---------
def main():
    st.title("🚇 TfL Lost Customer Hours Analysis")
    df = load_data()
    plot_lost_hours_line_chart(df)

    with st.expander("📊 Annual Lost Hours — Grouped Bar Chart"):
        st.pyplot(plot_annual_grouped_bar(df))


if __name__ == "__main__":
    main()