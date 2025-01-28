import streamlit as st
import pandas as pd
import plotly.express as px

# Read my File
df = pd.read_csv('./data/waf-data.csv') 

# Sidebar for product selection
st.sidebar.header('Select Products to Compare')
selected_products = st.sidebar.multiselect('Products', df['Product'].unique())

# Sidebar for product selection
st.sidebar.header('Select Categories to Include')
unique_categories = df['Category'].unique()
selected_categories = []
for category in unique_categories:
    if st.sidebar.checkbox(category):
        selected_categories.append(category)

# Filter data based on selection

# Create Charts with Firltered Data
charts = []
   

for category in selected_categories:

    filtered_data = df[df['Product'].isin(selected_products) & df['Category'].isin([category])]
    fig = px.bar(filtered_data, y='Feature', x='Value',color='Product', barmode='group')
    fig.update_layout(
        yaxis_title="Feature",
        xaxis_title="Value",
        legend_title="Product",
        template="plotly"
    )
    
    fig.update_layout(
        meta={ "id": category},
        title=f"Category: {category}"
    )

    charts.append(fig)


# Display Charts by Category based in Filtefed Daa



# dispay a section for each section in selected_categories
idx = 0 
for category in selected_categories:
    st.header(f"**{category}**")
    st.plotly_chart(charts[idx])
    idx += 1


    # # Show Gauge Bar with Average Rating in columns
    # # Create columns
    # col1, col2, col3 = st.columns(3)

    # # Chart 1
    # with col1:
    #     st.write("Chart 1")
        
    # # Chart 2
    # with col2:
    #     st.write("Chart 2")
        
    # # Chart 3
    # with col3:
    #     st.write("Chart 3")

    # Plot the data using plotly, use product as Series and Value as the y-axis, use vertical bar chart
    
    # st.plotly_chart(fig)


# # For debugging purposes
# st.markdown("<hr>", unsafe_allow_html=True)
# st.title("Debug Session")
# st.dataframe(df)



    