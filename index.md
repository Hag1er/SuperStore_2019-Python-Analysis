<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Superstore Sales Performance Analysis</title>

    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-color: #1A365D;
            --secondary-color: #2B6CB0;
            --bg-color: #F7FAFC;
            --text-color: #2D3748;
            --card-bg: #FFFFFF;
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }

        header {
            text-align: center;
            padding: 40px 0;
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            border-radius: 12px;
            margin-bottom: 40px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }

        header h1 {
            font-size: 2.2rem;
            margin: 0 0 10px 0;
            font-weight: 700;
        }

        header p {
            font-size: 1.1rem;
            opacity: 0.9;
            margin: 0;
        }

        .card {
            background: var(--card-bg);
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            margin-bottom: 30px;
        }

        h2 {
            color: var(--primary-color);
            border-bottom: 2px solid #E2E8F0;
            padding-bottom: 10px;
            margin-top: 0;
        }
        .workflow-steps {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .step {
            background: #EDF2F7;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid var(--secondary-color);
        }

        .step h3 {
            margin-top: 0;
            font-size: 1.1rem;
            color: var(--primary-color);
        }

        /* Dashboard Iframe Container */
        
        .dashboard-container {
            position: relative;
            width: 100%;
            height: 850px;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 16px rgba(0,0,0,0.08);
        }

        iframe {
            width: 100%;
            height: 100%;
            border: none;
        }

        footer {
            text-align: center;
            padding: 20px;
            color: #A0AEC0;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>

    <div class="container">
        <header>
            <h1>Superstore Sales Performance Analysis in United States Stores</h1>
            <p>End-to-End Data Analysis, Business Insights & Interactive Dashboard</p>
        </header>

        <div class="card">
            <h2>📊 Dataset Overview</h2>
            <p>
                This project analyzes sales data from a Superstore operating across the United States. The dataset includes order details across 
                product categories (Technology, Office Supplies, and Furniture), regional performance, customer segments, sales volume, discounts, 
                and net profitability.
            </p>
        </div>

        <div class="card">
            <h2>⚙️ Project Workflow</h2>
            <div class="workflow-steps">
                <div class="step">
                    <h3>1. Data Cleaning & Preprocessing</h3>
                    <p>Handling missing values, standardizing datetime fields, and feature engineering (calculating Profit Margins and YearMonth aggregations).</p>
                </div>
                <div class="step">
                    <h3>2. Exploratory Data Analysis (EDA)</h3>
                    <p>Analyzing key sales drivers, regional performance, discount impact on profitability, and monthly trend seasonality using Python.</p>
                </div>
                <div class="step">
                    <h3>3. Interactive Dashboard Development</h3>
                    <p>Building a dynamic Streamlit application integrated with Plotly visualizations for multi-dimensional filtering and drill-down analysis.</p>
                </div>
            </div>
        </div>

        <div class="card">
            <h2>🚀 Interactive Dashboard & Executive Insights</h2>
            <p>Explore the live interactive dashboard below to filter by Region, Category, and Segment in real time.</p>
            
            <div class="dashboard-container">
                <iframe 
    src=https://superstore2019-dashboard.streamlit.app/?embed=true&embed_options=show_toolbar" 
    width="100%" 
    height="850px" 
    style="border: none; border-radius: 8px;"
    allow="cross-origin-isolated">
    ## 📊 Interactive Dashboard

            </div>
        </div>

        <footer>
            <p>Superstore Analysis Portfolio Project | Developed by Hagar Gamal</p>
        </footer>
    </div>
## 📊 Interactive Dashboard

If the embedded dashboard does not load directly, click the button below to view it in full screen:

<a href="https://your-app-name.streamlit.app" target="_blank" style="padding: 10px 20px; background-color: #ff4b4b; color: white; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block; margin-bottom: 15px;">🚀 Open Dashboard in Full Screen</a>

<iframe src="https://your-app-name.streamlit.app/?embed=true" width="100%" height="800px" frameborder="0" allowfullscreen></iframe>
</body>
</html>
