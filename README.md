# nyc_air_quality

This project is built to analyze environmental water quality data collected over multiple years from various monitoring sites. The dataset includes key environmental variables such as:

- `WaterTemp_C`: Water Temperature in Celsius  
- `DO_mg_L`: Dissolved Oxygen in mg/L  
- `pH`: Acidity level of the water  
- `Salinity`: Salt concentration in parts per thousand (ppt)  
- `Site_Id`: Site location identifier  
- `Read_Date` and `Year`: Timestamps of the readings  

The data was first cleaned and processed using the `data_wrangling.py` script, which removed missing or inconsistent entries, simplified column names, and parsed date fields. A cleaned dataset was stored for further analysis and modeling.

---

## Modeling Approach

To model and predict water temperature, I used a **Linear Regression** model. This approach was chosen because the target variable (`WaterTemp_C`) is continuous, and linear regression provides a straightforward method to understand how multiple features (such as pH, DO, salinity, and location) influence it.

The model was implemented in the `modeling.py` script. Categorical variables like `Site_Id` were one-hot encoded to allow inclusion in the model. The data was then split into training and testing sets using an 80/20 ratio.

---

## Performance Metrics

To evaluate the model, I used **Root Mean Squared Error (RMSE)** because it is suitable for continuous regression problems and penalizes large errors more than MAE. The final RMSE achieved by the model was:

- **RMSE**: `16.20`

This indicates that the model's average error in predicting water temperature is approximately 16.2°C, which suggests the model may need further tuning or additional features to improve accuracy.

---

## Streamlit Dashboard

An interactive dashboard (`app.py`) was built using Streamlit to visualize and interact with the data. Users can:

- Filter data by `Year` and `Site_Id`  
- View real-time summary metrics (average temp, pH, DO)  
- Visualize trends over time using Plotly charts

---

## 👤 Developer

- **Ronak Prajapati**  
  Student ID: 50127256  

---

## 📌 Task Summary

| Task                                            | Done By           |
|-------------------------------------------------|-------------------|
| Data exploration and feature selection          | Ronak Prajapati   |
| Data cleaning and preprocessing (`data_wrangling.py`) | Ronak Prajapati |
| Streamlit app development (`app.py`)            | Ronak Prajapati   |
| Visualization and plotting (`plots.ipynb`)      | Ronak Prajapati   |
| Machine learning model (`modeling.py`)          | Ronak Prajapati   |
| Documentation and `README.md`                  | Ronak Prajapati   |
| Final testing and integration                   | Ronak Prajapati   |

