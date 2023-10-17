import streamlit as st


st.title("Recommended articles")
st.markdown(
    "Here are some recommended articles for reading to enhance your understanding on saving energy.")

tab1, tab2, tab3 = st.tabs(
    ["Top 5 energy-saving tips", "Global Warming From Fossil Fuels", "Save energy when you freeze food"])

with tab1:
    st.subheader("Top 5 energy-saving tips")
    st.image("https://ricova.com/wp-content/uploads/elementor/thumbs/Journee-mondiale-de-lenvironnement-q789hjckb19kjixj2dhohim2v4i797uxgz9bc4qhfs.jpg")

    st.markdown(
        "#### 1. Switch off lights and electrical appliances when not using them")
    st.write("""
    To save the most energy, switch off the power points rather than leaving appliances on standby.
    Turn off your heaters, cooling units, and appliances when you go to bed or leave the house.
    Switch off your computer and equipment such as printers or Wi-Fi routers overnight or when you're away. Most computers have energy-saving settings that will turn the computer and screen off after a period of inactivity.
    """)

    st.markdown("#### 2. Switch to energy-saving LED light globes")
    st.write("""
    Energy-efficient globes could save up to 80% off your lighting costs. This is because LED bulbs use less power and last longer. That means you spend less money and time replacing them.
    """)

    st.markdown("#### 3. Shut doors and close curtains")
    st.write("""
    Shut doors to areas you're not using, and only cool or heat the rooms where you spend the most time.
    In cooler months, make sure your curtains or blinds seal your windows properly.
    Stop cool air leaking out by blocking draughts around doors and windows.
    In warmer months, keep your curtains closed during the day.
    External blinds or canvas awnings will also help keep your house cooler.
    """)

    st.markdown("#### 4. Save energy in how you wash and dry clothes")
    st.write("""
    Wait until your machine is full before starting a washing cycle.
    Washing clothes in cold water can save around $115 per year.
    You can also save by selecting the shortest appropriate washing cycle.
    Clothes dryers use lots of energy. Hang clothes outside to dry or use a fan to help dry them indoors.
    """) 

    st.markdown("#### 5. Understand and improve your home's energy use")
    st.write("""
    The Residential Efficiency Scorecard is available across Australia. In the same way as a fridge or washing machine has a star rating, a Scorecard rating shows how much energy is used throughout your home.

    Whether selling or renovating, renting, or just worried about high energy bills, a home energy assessment can help you save energy and money on bills by identifying your home's features that contribute to high energy bills and the improvements you can make.
    """)


with tab2:
    st.subheader("Global Warming From Fossil Fuels")
    st.image("https://u4d2z7k9.rocketcdn.me/wp-content/uploads/2021/06/ND46979-Roy-Mangersnes-1536x864.jpg.webp")
    st.markdown("""As of May 2023, CO2 PPM (parts per million) is at 420.00 and the global temperature rise is 1.15C compared to pre-industrial levels. This is undoubtedly one of the biggest environmental problems of our lifetime: as greenhouse gas emissions blanket the Earth, they trap the sun’s heat, leading to global warming.

The last time carbon dioxide levels on our planet were as high as today was more than 4 million years ago. Increased emissions of greenhouse gases have led to a rapid and steady increase in global temperatures, which in turn is causing catastrophic events all over the world – from Australia and the US experiencing some of the most devastating bushfire seasons ever recorded, locusts swarming across parts of Africa, the Middle East and Asia, decimating crops, and a heatwave in Antarctica that saw temperatures rise above 20C for the first time. Scientists are constantly warning that the planet has crossed a series of tipping points that could have catastrophic consequences, such as advancing permafrost melt in Arctic regions, the Greenland ice sheet melting at an unprecedented rate, accelerating sixth mass extinction, and increasing deforestation in the Amazon rainforest, just to name a few.

The climate crisis is causing tropical storms and other weather events such as hurricanes, heatwaves and flooding to be more intense and frequent than seen before. However, even if all greenhouse gas emissions were halted immediately, global temperatures would continue to rise in the coming years. That is why it is absolutely imperative that we start now to drastically reduce greenhouse gas emissions, invest in renewable energy sources, and phase our fossil fuels as fast as possible.
""", unsafe_allow_html=True)
    st.markdown("[Read more](https://earth.org/the-biggest-environmental-problems-of-our-lifetime/)")

with tab3:
    st.header("Top five tips to save energy in the kitchen")
    st.image("https://smartenergy.com/wp-content/uploads/2020/04/GettyImages-902908928-opt-min.jpg")

    st.markdown("#### 1. Choose energy efficient products")
    st.markdown("""
One major step is to ensure we choose energy efficient appliances. The 2011 Powering the Nation report studied energy use in homes across the UK. At the time of the study, the households studied owned an average of 41 different electrical appliances – with some owning up to 85. Entertainment appliances such as iPads, TVs or laptops do not usually have energy labels but white goods, such as dishwashers, fridges and ovens, must display their energy efficiency rating by law.

The highest possible rating is A+++, the lowest for certain appliances will be F or G, with a considerable energy saving difference between them. In many cases, appliances such as cookers will all be rated A+ or higher. But older appliances are likely to be considerably less energy efficient. Watch our video for more information:

The Energy Saving Trust Register is an extensive database of energy efficient appliances. You can also check TopTen UK, which is a consumer platform that assesses the most energy-efficient products on the market.
""")
    
    st.markdown("#### 2. Use the right size of appliance for your needs")
    st.markdown("""
Kitchen appliances such as washing machines, dishwashers, fridges, kettles and cookers have become more energy efficient over the years, with the best models using less energy than 10 years ago. However, increases in size of the average fridge, fridge-freezer and washing machine drum have cancelled out some of the possible energy savings.

If all you keep in your fridge is a bottle of champagne and a lemon (yes, I’m looking at you) do you really need a full size fridge-freezer?
""")
    
    st.markdown("#### 3. Don’t leave appliances on standby")
    st.markdown("""
While fridges, fridge-freezers, upright and chest freezers are traditionally the largest single consumers of electricity in the home because they’re always on – you can save energy by turning off other electronic appliances.

Your dishwasher, microwave, washing machine, tumble dryer and electric oven will all eat up electricity when left on standby. Try to get into the habit of turning them off at the plug to save energy.
""")
    
    st.markdown("#### 4. Save energy when you cook")
    st.markdown("Obviously you need to ensure your food preparation methods don’t affect the quality of your meal, but there are some simple ways to save energy when cooking.")

    st.markdown("#### 5. Save energy when you freeze food")
    st.markdown("""In addition to using an appropriately sized fridge or freezer, you can save energy by ensuring it works effectively.""")

    st.markdown("[Read more](https://www.energysavingtrust.org.uk/advice/top-five-tips-save-energy-kitchen)")