import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Dashboard",layout="wide")
st.title("Professional Student Dashboard")

d=pd.read_csv("stu.csv")
st.sidebar.header("Filter")
lowm=st.sidebar.slider("Minimum marks",0,100,50)
fd=d[d["Marks"]>=lowm]

st.metric("Total Students",len(d))
st.metric("Average ",round(d["Marks"].mean(),2))
st.metric("Max",d["Marks"].max())

st.subheader("Bar chart")
st.bar_chart(fd.set_index("Name")["Marks"])

pas=len(d[d["Result"]=="Pass"])
fail=len(d[d["Result"]=="Fail"])

pie_chart=pd.DataFrame({
    "status":["pass","Fail"],
    "count":[pas,fail]
})
st.subheader("Pass vs Fail")
st.bar_chart(pie_chart.set_index("status"))
st.metric("Pass_count",pas)
st.metric("Fail_count",fail)
st.subheader("Student data")
st.dataframe(fd)
st.write("AOA My dear brother that for you ")
