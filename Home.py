

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dailyData = pd.read_csv('dailyData.csv')
dailyData2 = pd.read_csv('dailyData2.csv')
monthlyData = pd.read_csv('monthlyData.csv')
monthlyData2 = pd.read_csv('monthlyData2.csv')


monthlyData.dropna(inplace=True)
monthlyData2.dropna(inplace=True)


    
# Custom CSS for increasing font size
custom_css = """
<style>
.report-box {
    font-size: 24px;  /* Adjust the font size as needed */
}

.header {
    text-decoration-line: underline;
    padding-bottom: 30px;
}

hr {
    border-top: 2px dotted white;
    width:100%;
}

.reco {
padding-top:80px;
}
</style>
"""


st.markdown(custom_css, unsafe_allow_html=True)
print(monthlyData)
print(sum(monthlyData['power_usage1']))

labels = ['Water Heater', 'Air-Conditioner', 'Kitchen Appliance', 'Laundry Appliances', 'Home Office Equipment', 'Others (Low-Energy Consumption Devices)']
# sizes_house1 = [
#         sum(monthlyData['power_usage1']), sum(monthlyData['power_usage2']), sum(monthlyData['power_usage3']),
#         sum(monthlyData['power_usage4']), sum(monthlyData['power_usage5']), sum(monthlyData['power_usage6'])
#         ]

# sizes_house2 = [
#         sum(monthlyData2['power_usage1']), sum(monthlyData2['power_usage2']), sum(monthlyData2['power_usage3']),
#         sum(monthlyData2['power_usage4']), sum(monthlyData2['power_usage5']), sum(monthlyData2['power_usage6'])
#         ]

# # total_sum = sum(sizes)




custom_palette = sns.color_palette("husl", len(labels))

colors = ["#fd7f6f", "#7eb0d5", "#b2e061", "#bd7ebe", "#ffb55a", "#ffee65"]

house1_data = pd.read_csv('dailyData.csv')
house2_data = pd.read_csv('dailyData2.csv')
st.markdown('<div class="header"><h1 style="font-size: 48px">Monitoring Energy Consumption</h1></div>', unsafe_allow_html=True)

st.sidebar.header("Add a House (Daily)")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file (Daily)", type=["csv"] , key = "daily")

st.sidebar.header("Add a House (Monthly)")
uploaded_file2 = st.sidebar.file_uploader("Upload a CSV file(Monthly)", type=["csv"], key = "monthly")

# Check if a CSV file is uploaded
if uploaded_file is not None:
    st.sidebar.markdown("CSV file uploaded successfully!")

    # Load the uploaded CSV file
    new_house_data = pd.read_csv(uploaded_file)

    # You can now perform any operations with the new house data
    st.markdown("<h3>Daily Report for House 3</h3>", unsafe_allow_html=True)
    st.write(new_house_data)  

if uploaded_file2 is not None:
    st.sidebar.markdown("CSV file uploaded successfully!")

    # Load the uploaded CSV file
    new_house_data = pd.read_csv(uploaded_file2)

    # You can now perform any operations with the new house data
    st.markdown("<h3>Monthly Report for House 3</h3>", unsafe_allow_html=True)
    st.write(new_house_data)   



# Create a selectbox to choose the house
dailyChart = st.selectbox(
    'Choose House',
    ('House 1', 'House 2')
)   

def update_data_and_chart(data):

# Group data by 'timestamp' and calculate the sum of 'power_usage1' to 'power_usage6'
    grouped_data = data.groupby('timestamp').agg({
    'power_usage1': 'sum',
    'power_usage2': 'sum',
    'power_usage3': 'sum',
    'power_usage4': 'sum',
    'power_usage5': 'sum',
    'power_usage6': 'sum'
}).reset_index()

# Set the device names for the y-axis labels
    device_names = {
    'power_usage1': 'Water Heater',
    'power_usage2': 'Air-Conditioner',
    'power_usage3': 'Kitchen Appliance',
    'power_usage4': 'Laundry Appliances',
    'power_usage5': 'Home Office Equipment',
    'power_usage6': 'Others (Low-Energy Consumption Devices)'
}

    total_power_usage = grouped_data[['power_usage1', 'power_usage2', 'power_usage3', 'power_usage4', 'power_usage5', 'power_usage6']].sum(axis=1)

    grouped_data.rename(columns=device_names, inplace=True)






    st.markdown('<div class="report-box"><h3 style="font-size: 36px">Daily Report<sub>(watt)</sub></h3></div>', unsafe_allow_html=True)

    st.bar_chart(grouped_data, x='timestamp', y=list(device_names.values()))
if dailyChart == 'House 1':
    update_data_and_chart(house1_data)
else:
    update_data_and_chart(house2_data)



st.markdown("<hr>", unsafe_allow_html=True)


st.markdown('<div class="report-box"><h3 style="font-size: 36px ; margin-top: 50px ; ">Monthly Report<sub>(watt)</sub></h3></div>', unsafe_allow_html=True)


selected_house = st.radio("Select House", ("House 1", "House 2"))

# Determine the selected sizes
if selected_house == "House 1":
    sizes = [
        sum(monthlyData['power_usage1']), sum(monthlyData['power_usage2']), sum(monthlyData['power_usage3']),
        sum(monthlyData['power_usage4']), sum(monthlyData['power_usage5']), sum(monthlyData['power_usage6'])
    ]
else:
    sizes = [
        sum(monthlyData2['power_usage1']), sum(monthlyData2['power_usage2']), sum(monthlyData2['power_usage3']),
        sum(monthlyData2['power_usage4']), sum(monthlyData2['power_usage5']), sum(monthlyData2['power_usage6'])
    ]

total_sum = sum(sizes)

# Create a pie chart
fig, ax = plt.subplots()
fig.set_facecolor('#0E1117') 
ax.pie(sizes, colors=colors, startangle=90)
ax.axis('equal')

legend_labels = ['{} - {:.1f}%'.format(label, (size / total_sum) * 100) for label, size in zip(labels, sizes)]
ax.legend(legend_labels, loc='upper left', bbox_to_anchor=(0.85, 1))

st.pyplot(fig)




if st.button("Give Me Recommendations"):
    custom_style = """
<style>
.custom-box {
    border: 2px solid white;
    background: #FFFFFF;
    padding: 10px;
    font-weight: 600px;
    font-size: 24px;
    color:#000000;
    border-radius: 10px;
}

h4 {
    color:#000000;
}
</style>
"""

# Apply the custom style
    st.markdown(custom_style, unsafe_allow_html=True)

# Create a div with the custom style
    st.markdown(f'<div class="custom-box"><h4>Total Energy Consumption This Month:</h4> {total_sum} Watt</div>', unsafe_allow_html=True)
    

    if sum(monthlyData['power_usage1']) <= 250000:
        recommendation = "Your power usage for your water heater are within an acceptable range."

    else:
        recommendation = "Your power usage for water heater are too high. Consider optimizing your energy consumption."
        recommendation += "<ul>"
        recommendation += "<li>Turn down the water heater temperature.</li>"
        recommendation += "<li>Consider using hot water judiciously.</li>"
        recommendation += "<li>Check for any water heater leaks or inefficiencies.</li>"
        recommendation += "</ul>"

    if sum(monthlyData['power_usage2']) <= 163800:
        recommendation2 = "Your power usage for your air-conditioner are within an acceptable range."
    
    else:
        recommendation2 = "Your power usage for air-conditioner are very high. You should take immediate steps to reduce energy consumption."
        recommendation2 += "<ul>"
        recommendation2 += "<li>Check for air conditioner maintenance needs.</li>"
        recommendation2 += "<li>Use temperature settings efficiently.</li>"
        recommendation2 += "<li>Consider using fans to reduce reliance on the air conditioner.</li>"
        recommendation2 += "</ul>"

    if sum(monthlyData['power_usage3']) <= 122000:
        recommendation3 = "Your power usage for your kitchen-appliances are within an acceptable range."
    
    else:
        recommendation3 = "Your power usage for kitchen appliances are very high. You should take immediate steps to reduce energy consumption."
        recommendation3 += "<ul>"
        recommendation3 += "<li>Optimize your cooking time to minimize energy usage.</li>"
        recommendation3 += "<li>Use energy-efficient appliances.</li>"
        recommendation3 += "<li>Avoid preheating the oven for too long.</li>"
        recommendation3 += "</ul>"

    if sum(monthlyData['power_usage4']) <= 140400:
        recommendation4 = "Your power usage for your laundry appliances are within an acceptable range."
    
    else:
        recommendation4 = "Your power usage for laundry appliances are very high. You should take immediate steps to reduce energy consumption."
        recommendation4 += "<ul>"
        recommendation4 += "<li>Use the washing machine with full loads to save energy.</li>"
        recommendation4 += "<li>Opt for cold water washes when possible.</li>"
        recommendation4 += "<li>Clean the dryer's lint filter regularly for efficient drying.</li>"
        recommendation4 += "</ul>"

    if sum(monthlyData['power_usage5']) <= 850:
        recommendation5 = "Your power usage for your home-office equipments are within an acceptable range."
    
    else:
        recommendation5 = "Your power usage for home-office appliances are very high. You should take immediate steps to reduce energy consumption."
        recommendation5 += "<ul>"
        recommendation5 += "<li>Turn off devices when not in use.</li>"
        recommendation5 += "<li>Use power strips to easily switch off multiple devices.</li>"
        recommendation5 += "<li>Enable energy-saving settings on computers and monitors.</li>"
        recommendation5 += "</ul>"
    
    if sum(monthlyData['power_usage6']) <= 3000:
        recommendation6 = "Your power usage for your Others (Low-Energy Consumption Devices) are within an acceptable range."
    
    else:
        recommendation6 = "Your power usage for Others (Low-Energy Consumption Devices) is very high. You should take immediate steps to reduce energy consumption."
        recommendation6 += "<ul>"
        recommendation6 += "<li>Ensure that all devices are turned off when not in use.</li>"
        recommendation6 += "<li>Consider upgrading to more energy-efficient models when replacing devices.</li>"
        recommendation6 += "<li>Implement smart home solutions to automate energy savings.</li>"
        recommendation6 += "</ul>"


    # st.write(f"Total Power Usage (Monthly): {total_wattage} Watts")
    st.markdown("<h2>Recommendations for House 1</h2>", unsafe_allow_html=True)
    st.markdown(recommendation, unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(recommendation2, unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(recommendation3, unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(recommendation4, unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(recommendation5, unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(recommendation6, unsafe_allow_html=True)

    if sum(monthlyData2['power_usage1']) <= 250000:
        recommendations = "Your power usage for your water heater are within an acceptable range."

    else:
        recommendations = "Your power usage for water heater are too high. Consider optimizing your energy consumption."
        recommendations += "<ul>"
        recommendations += "<li>Turn down the water heater temperature.</li>"
        recommendations += "<li>Consider using hot water judiciously.</li>"
        recommendations += "<li>Check for any water heater leaks or inefficiencies.</li>"
        recommendations += "</ul>"

    if sum(monthlyData2['power_usage2']) <= 1638000:
        recommendations2 = "Your power usage for your air-conditioner are within an acceptable range."
    
    else:
        recommendations2 = "Your power usage for air-conditioner are very high. You should take immediate steps to reduce energy consumption."
        recommendations2 += "<ul>"
        recommendations2 += "<li>Check for air conditioner maintenance needs.</li>"
        recommendations2 += "<li>Use temperature settings efficiently.</li>"
        recommendations2 += "<li>Consider using fans to reduce reliance on the air conditioner.</li>"
        recommendations2 += "</ul>"

    if sum(monthlyData2['power_usage3']) <= 122000:
        recommendations3 = "Your power usage for your kitchen-appliances are within an acceptable range."
    
    else:
        recommendations3 = "Your power usage for kitchen appliances are very high. You should take immediate steps to reduce energy consumption."
        recommendations3 += "<ul>"
        recommendations3 += "<li>Optimize your cooking time to minimize energy usage.</li>"
        recommendations3 += "<li>Use energy-efficient appliances.</li>"
        recommendations3 += "<li>Avoid preheating the oven for too long.</li>"
        recommendations3 += "</ul>"

    if sum(monthlyData2['power_usage4']) <= 140400:
        recommendations4 = "Your power usage for your laundry appliances are within an acceptable range."
    
    else:
        recommendations4 = "Your power usage for laundry appliances are very high. You should take immediate steps to reduce energy consumption."
        recommendations4 += "<ul>"
        recommendations4 += "<li>Use the washing machine with full loads to save energy.</li>"
        recommendations4 += "<li>Opt for cold water washes when possible.</li>"
        recommendations4 += "<li>Clean the dryer's lint filter regularly for efficient drying.</li>"
        recommendations4 += "</ul>"

    if sum(monthlyData2['power_usage5']) <= 850:
        recommendations5 = "Your power usage for your home-office equipments are within an acceptable range."
    
    else:
        recommendations5 = "Your power usage for home-office appliances are very high. You should take immediate steps to reduce energy consumption."
        recommendations5 += "<ul>"
        recommendations5 += "<li>Turn off devices when not in use.</li>"
        recommendations5 += "<li>Use power strips to easily switch off multiple devices.</li>"
        recommendations5 += "<li>Enable energy-saving settings on computers and monitors.</li>"
        recommendations5 += "</ul>"
    
    if sum(monthlyData2['power_usage6']) <= 3000:
        recommendations6 = "Your power usage for your Others (Low-Energy Consumption Devices) are within an acceptable range."
    
    else:
        recommendations6 = "Your power usage for Others (Low-Energy Consumption Devices) is very high. You should take immediate steps to reduce energy consumption."
        recommendations6 += "<ul>"
        recommendations6 += "<li>Ensure that all devices are turned off when not in use.</li>"
        recommendations6 += "<li>Consider upgrading to more energy-efficient models when replacing devices.</li>"
        recommendations6 += "<li>Implement smart home solutions to automate energy savings.</li>"
        recommendations6 += "</ul>"


    # st.write(f"Total Power Usage (Monthly): {total_wattage} Watts")

    st.markdown('<div class="reco"><h2>Recommendations for House 2</h2></div>', unsafe_allow_html=True)
    st.markdown(recommendations, unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(recommendations2, unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(recommendations3, unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(recommendations4, unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(recommendations5, unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(recommendations6, unsafe_allow_html=True)







