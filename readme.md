# Music Data ETL and Reporting Project

## Overview

This project demonstrates an ETL (Extract, Transform, Load) process applied to music streaming data. The workflow includes loading a CSV file into a MySQL database, transforming the data using Python, and generating reports in Tableau.

## Project Workflow

1. **Extract**
    - Load `data.csv` into the `raw_data` table in the `music` database on MySQL server.

2. **Transform**
    - Connect to the MySQL server using Python (SQLAlchemy and mysql.connector).
    - Access data from the `raw_data` table and perform transformations in a Jupyter Notebook.
    - Load the transformed data into the `transformed_data` table in the same database.

3. **Load**
    - The transformed data is now ready and stored in the `transformed_data` table.

4. **Generate Reports**
    - Connect Tableau to the `transformed_data` table in MySQL in query mode.
    - Generate the following reports:
        - Most Streamed Songs
        - Over The Years Trend
        - Artist Popularity

## Project Structure

- `data/` : Contains the CSV file used as the data source.
- `notebooks` : Jupyter Notebooks for data extraction, transformation, and loading processes.
- `log` : Log file capturing the ETL process.
- `report` : PDF file of the generated reports from Tableau.
- `README.md` : Project documentation.

## Prerequisites

- MySQL Server
- Python 3.x
- Jupyter Notebook
- SQLAlchemy
- mysql-connector-python
- Tableau

## Installation and Setup

1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/music-data-etl.git
    cd music-data-etl
    ```

2. **Set up the MySQL Database**
    - Create a database named `music` in your MySQL server.
    - Create a table `raw_data` and `transformed_data` in the `music` database.

3. **Load the CSV data into MySQL**
    - Use a MySQL client or script to load `data/data.csv` into the `raw_data` table.

4. **Set up the Python environment**
    - Install required Python packages
    ```bash
    pip install sqlalchemy mysql-connector-python pandas
    ```

5. **Run the ETL process**
    - Open and run the Jupyter Notebook in `notebooks/` to transform the data and load it into the `transformed_data` table.

6. **Generate Reports in Tableau**
    - Connect Tableau to the `transformed_data` table in MySQL.
    - Generate and save the reports as PDFs in the `reports/` directory.

## Usage

1. **Running the ETL process**
    - Open the Jupyter Notebook in `notebooks/` and execute the cells to perform ETL.

2. **Viewing the Reports**
    - Open the PDF files in the `reports/` directory to view the generated reports.

## Contact

For any queries or issues, please contact [your email address].

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
