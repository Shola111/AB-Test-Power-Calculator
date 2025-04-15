# A/B Test Power Simulator 🧪

An interactive tool to simulate and understand A/B testing performance. Designed for product managers, analysts, and data scientists to:

- Estimate statistical power
- Calculate minimum detectable effect (MDE)
- Determine required sample sizes
- Visualize p-values and lift distributions

## 🔧 How It Works
- Choose a baseline conversion rate, target lift, and significance level
- Run simulated experiments to estimate power across sample sizes
- Visualize the tradeoffs and risks in experimental design

## 💻 Stack
- Python (numpy, scipy, matplotlib)
- Streamlit (optional)
- Jupyter Notebooks

## 🚀 Run Locally
```bash
git clone https://github.com/YOURNAME/ab-test-power-simulator.git
cd ab-test-power-simulator
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## 🧠 Next Steps
- Add uplift modeling
- Connect to real marketing/clickstream data
- Deploy online for live use
