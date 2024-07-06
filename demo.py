
import streamlit as st
import pandas as pd
import datetime as dt
    
st.header("Save AMC")
clientName = st.text_input("Client Name")
amcfms, type = st.columns(2)
amcfms = amcfms.selectbox("AMC/FMS", options=["AMC", "FMS", "AMC+FMS", "SFMS", "WIFI AMC"])
type = type.selectbox("Type", options=["Comprehensive", "Non Comprehensive", "Comprehensive + Non Comprehensive", "AMC", "FMS", "Renewal"])
note = st.text_area("Extra Specification")
totalAmt = st.text_input("Total Amount")
start = st.date_input("Start")
end = st.date_input("End")


billing =st.selectbox("Billing", options=["Yearly", "Half Yearly", "Quarterly", "Monthly"])
uploaded_file =st.file_uploader("Upload File")

if billing == "Yearly":
    data2 = {
        
        "Start date":[(pd.to_datetime(end)-pd.DateOffset(days=5)).date(),
                      (pd.to_datetime(end)-pd.DateOffset(days=4)).date(),
                      (pd.to_datetime(end)-pd.DateOffset(days=3)).date(),
                      (pd.to_datetime(end)-pd.DateOffset(days=2)).date(),
                      (pd.to_datetime(end)-pd.DateOffset(days=1)).date(),
                      pd.to_datetime(end).date(),
                      (pd.to_datetime(end)-pd.DateOffset(days=5)).date(),
                      (pd.to_datetime(end)-pd.DateOffset(days=4)).date(),
                      (pd.to_datetime(end)-pd.DateOffset(days=3)).date(),
                      (pd.to_datetime(end)-pd.DateOffset(days=2)).date(),
                      (pd.to_datetime(end)-pd.DateOffset(days=1)).date(),
                      pd.to_datetime(end).date()]
    }
    
elif billing == "Quarterly":
    
    data2 = {
        "Start date":[(pd.to_datetime(end)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=1)).date(),
        pd.to_datetime(end).date(),(pd.to_datetime(end)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=1)).date(),
        pd.to_datetime(end).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)).date(),(pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)).date(),(pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)).date(),(pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)).date(),
        
        ],
    }
    
else:
    st.text(billing)
    data2 = {
        "Start date":[(pd.to_datetime(end)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=1)).date(),
        pd.to_datetime(end).date(),(pd.to_datetime(end)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(end)-pd.DateOffset(days=1)).date(),
        pd.to_datetime(end).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)).date(),(pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=6)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)).date(),(pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=3)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)).date(),(pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=9)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)).date(),(pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=1)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)).date(),(pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=2)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)).date(),(pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=4)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)).date(),(pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=5)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)).date(),(pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=7)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)).date(),(pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=8)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)).date(),(pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=10)).date(),

        (pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)).date(),(pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=5)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=4)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=3)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=2)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)-pd.DateOffset(days=1)).date(),
        (pd.to_datetime(start)+pd.DateOffset(months=11)).date(),
        
        ],
    }

df2 = pd.DataFrame([data2])  

st.download_button(
   "Press to Download",
   df2.to_csv(index=False).encode('utf-8'),
   "file.csv",
   "text/csv",
   key='download-csv'
)

if st.button("Save"):
    if billing == "Yearly":
        
        data = {
            "Client Name":[clientName],
            "AMC/FMS":[amcfms],
            "Type":[type],
            "Total Amount":[totalAmt],
            "Start":[start],
            "End":[end],
            "Billing":[billing],
            "Note":[note]
        }
        df=pd.DataFrame(data)
        st.dataframe(df)
    elif billing == "Half Yearly":
        
        data = {
            "Client Name":[clientName],
            "AMC/FMS":[amcfms],
            "Type":[type],
            "Total Amount":[totalAmt],
            "Start":[start],
            "End":[end],
            "Billing":[billing],
            "P1 Start":[start],
            "P1 End":[(pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=1)).date()],
            "P2 Start":[(pd.to_datetime(start)+pd.DateOffset(months=6)).date()],
            "P2 End":[end],
            "Note":[note]
        }
        df=pd.DataFrame(data)
        st.dataframe(df)
    elif billing == "Quarterly":
        
        data = {
            "Client Name":[clientName],
            "AMC/FMS":[amcfms],
            "Type":[type],
            "Total Amount":[totalAmt],
            "Start":[start],
            "End":[end],
            "Billing":[billing],
            "Q1 Start":[start],
            "Q1 End":[(pd.to_datetime(start)+pd.DateOffset(months=3)-pd.DateOffset(days=1)).date()],
            "Q2 Start":[(pd.to_datetime(start)+pd.DateOffset(months=3)).date()],
            "Q2 End":[(pd.to_datetime(start)+pd.DateOffset(months=6)-pd.DateOffset(days=1)).date()],
            "Q3 Start":[(pd.to_datetime(start)+pd.DateOffset(months=6)).date()],
            "Q3 End":[(pd.to_datetime(start)+pd.DateOffset(months=9)-pd.DateOffset(days=1)).date()],
            "Q4 Start":[(pd.to_datetime(start)+pd.DateOffset(months=9)+pd.DateOffset(days=1)).date()],
            "Q4 End":[(pd.to_datetime(start)+pd.DateOffset(months=12)-pd.DateOffset(days=1)).date()],
            
            "Note":[note]
        }
        df=pd.DataFrame(data)
        st.dataframe(df)
    else:
        
        data = {
            "Client Name":[clientName],
            "AMC/FMS":[amcfms],
            "Type":[type],
            "Total Amount":[totalAmt],
            "Start":[start],
            "End":[end],
            "Billing":[billing],
            "M1":[start],
            "M2":[(pd.to_datetime(start)+pd.DateOffset(months=1)).date()],
            "M3":[(pd.to_datetime(start)+pd.DateOffset(months=2)).date()],
            "M4":[(pd.to_datetime(start)+pd.DateOffset(months=3)).date()],
            "M5":[(pd.to_datetime(start)+pd.DateOffset(months=4)).date()],
            "M6":[(pd.to_datetime(start)+pd.DateOffset(months=5)).date()],
            "M7":[(pd.to_datetime(start)+pd.DateOffset(months=6)).date()],
            "M8":[(pd.to_datetime(start)+pd.DateOffset(months=7)).date()],
            "M9":[(pd.to_datetime(start)+pd.DateOffset(months=8)).date()],
            "M10":[(pd.to_datetime(start)+pd.DateOffset(months=9)).date()],
            "M11":[(pd.to_datetime(start)+pd.DateOffset(months=10)).date()],
            "M12":[(pd.to_datetime(start)+pd.DateOffset(months=11)).date()],
            "Note":[note]
        }
        df=pd.DataFrame(data)
        st.dataframe(df)
