import os
import csv
import streamlit as st
import pandas as pd
import altair as alt


def draw_chart(data, num, csv_file):
    # 计算每日差值
    diff = int(data[-1][num]) - int(data[-2][num])
    if diff == 0:
        domain_more = int(data[-1][num]) + 30
        domain_less = int(data[-1][num]) - 30
    else:
        domain_more = int(data[-1][num]) + diff * 10
        domain_less = int(data[-1][num]) - diff * 10

    chart = alt.Chart(csv_file).mark_line().configure_axisX(labelAngle=0).encode(
        x="时间",
        y=alt.Y(data[0][num], scale=alt.Scale(domain=[domain_less, domain_more])))
    st.altair_chart(chart, use_container_width=True)


def draw_metric(data, num):
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("本日新增", str(int(data[-1][num]) - int(data[-2][num])))
        with col2:
            st.metric("本周新增", str(int(data[-1][num]) - int(data[-2][num])))  # 暂不可用
        with col3:
            st.metric("每日均增", str(int(data[-1][num]) - int(data[-2][num])))  # 暂不可用
        with col4:
            st.metric("总计", data[-1][num])
    st.write("")


def draw_task(name, csv_name):
    st.subheader(name)

    # 转换csv_path
    current_path = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_path, "data", csv_name)

    # pd读取csv，并转换时间格式
    csv_file = pd.read_csv(csv_path).tail(7)
    csv_file["时间"] = pd.to_datetime(csv_file["时间"]).dt.strftime("%m-%d")

    # 读取csv
    with open(csv_path, 'r', newline='') as file:
        data = list(csv.reader(file))

    # 导航条
    if len(data[0]) == 2:
        tab1, tab2 = st.tabs([data[0][1], "原始数据"])
        with tab1:
            draw_metric(data, 1)
            draw_chart(data, 1, csv_file)
        with tab2:
            st.dataframe(csv_file, use_container_width=True)
    else:
        tab1, tab2, tab3 = st.tabs([data[0][1], data[0][2], "原始数据"])
        with tab1:
            draw_metric(data, 1)
            draw_chart(data, 1, csv_file)
        with tab2:
            draw_metric(data, 2)
            draw_chart(data, 2, csv_file)
        with tab3:
            st.dataframe(csv_file, use_container_width=True)


if __name__ == '__main__':
    st.set_page_config(page_title="Auto-sign Dashboard", layout="wide")

    # visit

    st.header("forum-visit", divider="gray")
    st.write("")

    visit1, visit2 = st.columns(2)
    with visit1:
        draw_task(name="Chiphell", csv_name="chiphell.csv")
    with visit2:
        draw_task(name="VCB", csv_name="vcb.csv")

    # sign

    st.header("forum-sign", divider="gray")
    st.write("")

    sign1, sign2 = st.columns(2)
    with sign1:
        draw_task(name="TSDM", csv_name="tsdm.csv")
    with sign2:
        draw_task(name="sayhuahuo", csv_name="sayhuahuo.csv")

    sign3, sign4 = st.columns(2)
    with sign3:
        draw_task(name="4KSJ", csv_name="sksj.csv")
    with sign4:
        st.empty()

    # download

    st.header("forum-download", divider="gray")
    st.write("")

    download1, download2 = st.columns(2)
    with download1:
        draw_task(name="天雪", csv_name="skyey.csv")
    with download2:
        st.empty()
