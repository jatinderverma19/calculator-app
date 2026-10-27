import datetime
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="All-in-One Multi-Calculator Hub",
    page_icon="🧮",
    layout="wide",
)

st.title("🧮 All-in-One Universal Utility & Business Calculator")
st.markdown(
    "A single platform for all your daily calculations—Business, Age, Math,"
    " Conversions, Health, and Finance!"
)
st.markdown("---")

# Sidebar for Tool Selection
st.sidebar.header("🛠️ Select Calculator")
tool_choice = st.sidebar.selectbox(
    "Choose a tool:",
    [
        "📊 Profit & Loss Calculator",
        "🎂 Age & Date Calculator",
        "💯 Percentage & Discount",
        "🔄 Unit Converter",
        "💪 BMI & Health Calculator",
        "💰 Loan & EMI Calculator",
    ],
)

# ----------------- 1. PROFIT & LOSS CALCULATOR -----------------
if tool_choice == "📊 Profit & Loss Calculator":
  st.header("📊 Business Profit & Loss Calculator")
  st.markdown("Calculate your exact profit, loss, and margin easily.")

  col1, col2 = st.columns(2)
  with col1:
    qty = st.number_input("Quantity / Units", min_value=0.01, value=1.0)
    buy_price = st.number_input("Buy Price (per unit)", min_value=0.0, value=0.0)
  with col2:
    sell_price = st.number_input(
        "Sell / Current Price (per unit)", min_value=0.0, value=0.0
    )

  if st.button("Calculate P&L"):
    total_buy = qty * buy_price
    total_sell = qty * sell_price
    net_pl = total_sell - total_buy
    pl_percentage = (net_pl / total_buy * 100) if total_buy > 0 else 0.0

    st.markdown("### 📌 Results:")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Investment", f"₹ {total_buy:,.2f}")
    c2.metric("Total Return", f"₹ {total_sell:,.2f}")
    c3.metric(
        "Net Profit / Loss",
        f"₹ {net_pl:,.2f}",
        delta=f"{pl_percentage:.2f}%",
    )

# ----------------- 2. AGE & DATE CALCULATOR -----------------
elif tool_choice == "🎂 Age & Date Calculator":
  st.header("🎂 Age & Date Difference Calculator")

  birth_date = st.date_input(
      "Select Date of Birth / Start Date", datetime.date(2000, 1, 1)
  )
  target_date = st.date_input(
      "Select Target Date / End Date", datetime.date.today()
  )

  if st.button("Calculate Age"):
    if target_date >= birth_date:
      days_diff = (target_date - birth_date).days
      years = days_diff // 365
      months = (days_diff % 365) // 30
      days = (days_diff % 365) % 30

      st.markdown("### 📌 Results:")
      st.success(
          f"✨ **{years} Years, {months} Months, and {days} Days** (Total ~"
          f" {days_diff:,} Days)"
      )
    else:
      st.error("Target date cannot be earlier than birth date!")

# ----------------- 3. PERCENTAGE & DISCOUNT CALCULATOR -----------------
elif tool_choice == "💯 Percentage & Discount":
  st.header("💯 Percentage & Shopping Discount Calculator")

  calc_type = st.radio(
      "Select Calculation Type",
      ["Find Percentage of a Number", "Calculate Discount Price"],
  )

  if calc_type == "Find Percentage of a Number":
    col1, col2 = st.columns(2)
    with col1:
      num = st.number_input("Enter Total Value", value=100.0)
    with col2:
      pct = st.number_input("Enter Percentage (%)", value=10.0)

    if st.button("Calculate %"):
      result = (num * pct) / 100
      st.info(f"👉 **{pct}% of {num} is: {result:,.2f}**")

  else:
    col1, col2 = st.columns(2)
    with col1:
      original_price = st.number_input("Original Price", value=1000.0)
    with col2:
      discount_pct = st.number_input("Discount Percentage (%)", value=20.0)

    if st.button("Calculate Discount"):
      saved_amount = (original_price * discount_pct) / 100
      final_price = original_price - saved_amount
      st.markdown("### 📌 Results:")
      c1, c2 = st.columns(2)
      c1.metric("You Save", f"₹ {saved_amount:,.2f}")
      c2.metric("Final Price to Pay", f"₹ {final_price:,.2f}")

# ----------------- 4. UNIT CONVERTER -----------------
elif tool_choice == "🔄 Unit Converter":
  st.header("🔄 Universal Unit Converter")

  unit_type = st.selectbox(
      "Select Conversion Category",
      [
          "Length (cm to inch)",
          "Weight (kg to pound)",
          "Temperature (°C to °F)",
      ],
  )

  if unit_type == "Length (cm to inch)":
    cm = st.number_input("Enter Centimeters (cm)", value=10.0)
    if st.button("Convert"):
      inches = cm / 2.54
      st.success(f"👉 {cm} cm = **{inches:.2f} inches**")

  elif unit_type == "Weight (kg to pound)":
    kg = st.number_input("Enter Kilograms (kg)", value=1.0)
    if st.button("Convert"):
      pounds = kg * 2.20462
      st.success(f"👉 {kg} kg = **{pounds:.2f} lbs (pounds)**")

  elif unit_type == "Temperature (°C to °F)":
    celsius = st.number_input("Enter Celsius (°C)", value=25.0)
    if st.button("Convert"):
      fahrenheit = (celsius * 9 / 5) + 32
      st.success(f"👉 {celsius}°C = **{fahrenheit:.2f}°F**")

# ----------------- 5. BMI & HEALTH CALCULATOR -----------------
elif tool_choice == "💪 BMI & Health Calculator":
  st.header("💪 Body Mass Index (BMI) & Health Calculator")

  col1, col2 = st.columns(2)
  with col1:
    weight = st.number_input(
        "Weight (in kg)", min_value=1.0, value=70.0, format="%.1f"
    )
  with col2:
    height_cm = st.number_input(
        "Height (in cm)", min_value=10.0, value=170.0, format="%.1f"
    )

  if st.button("Calculate BMI"):
    if height_cm > 0:
      height_m = height_cm / 100.0
      bmi = weight / (height_m**2)

      if bmi < 18.5:
        category = "Underweight (Vajan kam hai)"
        color_box = st.warning
      elif 18.5 <= bmi < 25:
        category = "Normal Weight (Ekdum fit!)"
        color_box = st.success
      elif 25 <= bmi < 30:
        category = "Overweight (Vajan thoda zyada hai)"
        color_box = st.info
      else:
        category = "Obese (Motapa)"
        color_box = st.error

      st.markdown("### 📌 Results:")
      st.metric("Your BMI Score", f"{bmi:.2f}")
      color_box(f"Category: **{category}**")

# ----------------- 6. LOAN & EMI CALCULATOR -----------------
elif tool_choice == "💰 Loan & EMI Calculator":
  st.header("💰 Loan & Monthly EMI Calculator")

  col1, col2, col3 = st.columns(3)
  with col1:
    loan_amount = st.number_input(
        "Loan Amount (₹)", min_value=1000.0, value=500000.0, step=10000.0
    )
  with col2:
    interest_rate = st.number_input(
        "Annual Interest Rate (%)", min_value=0.1, value=8.5, step=0.1
    )
  with col3:
    tenure_years = st.number_input(
        "Loan Tenure (in Years)", min_value=1, max_value=30, value=5
    )

  if st.button("Calculate EMI"):
    monthly_rate = interest_rate / (12 * 100)
    months = tenure_years * 12

    if monthly_rate > 0:
      emi = (
          loan_amount
          * monthly_rate
          * (1 + monthly_rate) ** months
          / ((1 + monthly_rate) ** months - 1)
      )
    else:
      emi = loan_amount / months

    total_payment = emi * months
    total_interest = total_payment - loan_amount

    st.markdown("### 📌 Results:")
    c1, c2, c3 = st.columns(3)
    c1.metric("Monthly EMI", f"₹ {emi:,.2f}")
    c2.metric("Total Interest", f"₹ {total_interest:,.2f}")
    c3.metric("Total Payment", f"₹ {total_payment:,.2f}")
