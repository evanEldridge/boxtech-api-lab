# Container Insight Tool

This project is a Python-based tool that integrates with the BoxTech API to retrieve technical specifications for intermodal freight containers—including tare weight, size/type, and maximum gross mass.

Retrieved data is stored in a local SQL database, enabling easy querying, analysis, and reporting. This tool is intended to support workflows in global trade, logistics, and customs brokerage by providing fast access to verified container data.

---

## Features

- 🔗 Connects to the BoxTech API using ISO container numbers (e.g., MSCU1234567)
- 💾 Saves container data to a SQL database for persistent storage
- 🔍 Provides command-line interface for querying container details
- 📊 Supports basic analytics (e.g., average tare weight, container type breakdown)
- ⚠️ Handles API errors, duplicates, and missing data gracefully

---

## Technologies Used

- **Python** – scripting, API interaction, CLI/web interface
- **BoxTech API** – to fetch real-time container specs
- **SQL Server Express** – for storing container records

---

## Use Case Example

A customs brokerage or freight logistics company could use this tool to:

- Validate that container weights and dimensions meet port requirements
- Generate internal reports about container usage over time
- Spot trends in container types by shipper or carrier
- Automate documentation workflows based on container specs

---

## Setup Instructions

1. Clone the repository:
   '''bash
   git clone https://github.com/yourusername/container-insight-tool.git
   cd container-insight-tool

2. Install dependencies
   '''bash
   pip install -r requirements.txt

3. Add your API keey in a .env file:
   '''ini
   BOXTECH_API_KEY=your_api_key_here

4. Run the script to fetch container info:
   '''bash
   python fetch_containers.py MSCU1234567

5. Query the local database for stored container data:
   '''bash
   sqlite3 container_data.db
   SELECT * FROM container_info;

---

## Roadmap Ideas

- Add container batch processing from CSV
- Add interactive dashboard with Flask or Streamlit
- Expand analytics and reporting features
- Automate daily sync with cron/scheduler

---

## License

MIT License

---

## Disclaimer

This tool is intended for educational and demonstration purposes. Always verify container data against official documentation when used for operational decisions.