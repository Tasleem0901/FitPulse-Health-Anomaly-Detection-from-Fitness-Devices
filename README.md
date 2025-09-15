# FitPulse-Health-Anomaly-Detection-from-Fitness-Devices
FitPulse: Health Anomaly Detection from Fitness Devices

FitPulse is a data science project focused on detecting anomalies in fitness device data (heart rate, steps, sleep patterns).
It combines data preprocessing, feature extraction, time-series modeling, clustering, and anomaly detection into an interactive Streamlit dashboard.
Data Collection & Preprocessing

Import heart rate, steps, and sleep data from CSV/JSON.

Clean timestamps, fix missing values, and align time intervals.

2️⃣ Feature Extraction & Modeling

Extract statistical features using TSFresh.

Model seasonal patterns with Facebook Prophet.

Apply clustering (KMeans, DBSCAN) to group similar behaviors.

3️⃣ Anomaly Detection & Visualization

Rule-based detection: Threshold anomalies (e.g., sudden spikes).

Model-based detection: Residuals from Prophet, clustering outliers.

Visualizations with Matplotlib & Plotly.

4️⃣ Dashboard for Insights

Build an interactive Streamlit UI.

Upload data files, run anomaly detection, and display results.

Export reports in PDF/CSV format.

🔹 Tools & Technologies

Python – core programming language

Libraries: Pandas, NumPy, Matplotlib, Plotly, Scikit-learn

TSFresh – feature extraction from time-series data

Facebook Prophet – trend & seasonality modeling

Clustering: KMeans, DBSCAN for behavior grouping

Streamlit – interactive web dashboard

Data Formats: CSV, JSON (from fitness trackers)

🧩 Types of Anomalies

Point Anomaly: Single unusual data point

Example: Heart rate spikes to 180 bpm while sitting.

Contextual Anomaly: Normal in one context, abnormal in another

Example: High heart rate while running is fine, but abnormal while sleeping.

Collective Anomaly: Group of unusual points together

Example: Sleep < 3 hours for 7 consecutive days.

❓ Why Detect Anomalies?

Healthcare: Detect irregularities early → prevent diseases.

Finance: Detect fraud in transactions.

Cybersecurity: Identify hacking attempts.

Manufacturing: Spot machine faults before failures.
