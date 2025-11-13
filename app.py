import streamlit as st

st.title("🇧🇼 Botswana Solar Off-Grid System Design Tool")
st.write("Estimate your solar system size based on location and energy usage.")

irradiance = {
    "Gaborone": 5.7,
    "Francistown": 5.9,
    "Maun": 6.3,
    "Kasane": 6.1,
    "Kang": 6.5,
}

location = st.selectbox("Select your location", list(irradiance.keys()))
daily_load = st.number_input("Daily energy use (Wh)", min_value=100, max_value=50000, value=5000)
autonomy = st.number_input("Backup days", min_value=1, max_value=7, value=2)

if st.button("Calculate System Size"):
    irr = irradiance[location]
    loss_factor = 0.8
    system_voltage = 48
    dod = 0.8
    pv_kwp = daily_load / (irr * 1000 * loss_factor)
    battery_ah = (daily_load * autonomy) / (system_voltage * dod)
    inverter_kw = daily_load / (24 * 1000)

    st.success("✅ Solar System Design Results:")
    st.write(f"☀️ PV Array Size: {pv_kwp:.2f} kWp")
    st.write(f"🔋 Battery Capacity: {battery_ah:.1f} Ah @ 48 V")
    st.write(f"⚡ Inverter Size: {inverter_kw:.2f} kW")
