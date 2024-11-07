# Amazon Product Scraper with React & Flask

## Overview
This project is a simple **Amazon Product Scraper** built using **React** for the frontend and **Flask** for the backend. The application allows users to scrape Amazon products (such as product names, prices, ratings, and sellers) from a specific Amazon category or search page. The data is then displayed on the React frontend and can also be saved to a CSV file.

## Approach

The goal of this project was to showcase the ability to integrate **React** and **Flask** in a full-stack application. By using React for the frontend and Flask for the backend, I demonstrated the ability to build a scalable web application, where React handles the user interface and Flask manages the backend processing, including data scraping and serving APIs.

### Why React-Flask Connection?

1. **Frontend and Backend Integration**: 
   - **React** is used for building a dynamic user interface. It allows users to interact with the scraper by providing an interface to input the Amazon URL and view the results in an intuitive format.
   - **Flask** acts as the backend framework where the core business logic of the scraper resides. It handles incoming requests, runs the scraper, and returns the scraped data to the frontend in a structured format (JSON).

2. **Showcasing Full-Stack Development Skills**:
   - By combining React and Flask, I wanted to showcase my readiness to work on both frontend and backend technologies and integrate them seamlessly in a real-world application.
   - This setup also emphasizes the ability to connect and interact with **APIs** effectively, enabling communication between different technologies.

3. **Separation of Concerns**:
   - **React** handles the **UI** and **user interactions**, ensuring that the frontend is responsive and easy to use.
   - **Flask** handles the **data processing** and **scraping** logic, ensuring that the application is modular and scalable. Flask's ability to manage APIs and data scraping makes it a great choice for backend services.

## How the Scraper Works

### 1. **User Input**:
   - The frontend (built with React) allows users to enter an **Amazon search URL** or category link (e.g., for electronics or fashion).
   - The user then clicks on the "Fetch Products" button to initiate the scraping process.

### 2. **Backend Scraping**:
   - When the user clicks the "Fetch Products" button, the React frontend makes a **POST request** to the Flask backend (`/scrape` endpoint) with the provided Amazon URL.
   - The Flask backend uses **Selenium** to scrape product data from Amazon.
     - **Selenium** simulates a real browser interaction, enabling the backend to open multiple Amazon pages, extract the required product details, and move through pagination to scrape more items.
   
### 3. **Extracting Data**:
   - The scraper extracts details for each product, including:
     - **Product Name**
     - **Price**
     - **Rating**
     - **Seller Name**
   - The product data is collected in a **list of dictionaries**, where each dictionary represents a product and its details.

### 4. **Returning Data**:
   - After the data is collected, Flask processes it and returns it as a **JSON response** to the frontend.
   - The React frontend receives the product data and displays it in a grid format using **cards**, showing the relevant product details.

### 5. **CSV Export**:
   - The scraper also saves the scraped product data to a **CSV file** (`amazon_products.csv`), making it easy to download or analyze later.
   
### 6. **Pagination**:
   - The scraper can handle multiple pages of Amazon search results by iterating through page numbers in the URL (e.g., `&page=1`, `&page=2`).
   - This allows the scraper to collect data across several pages of results, increasing the number of products scraped.

## Project Structure

```
├── backend/
│   ├── app.py                   # Flask backend for scraping
│   ├── requirements.txt         # Python dependencies
│   └── amazon_products.csv      # Saved product data
└── frontend/
    ├── src/
    │   ├── App.js               # React main component
    │   ├── App.css              # CSS for styling
    │   └── index.js             # React entry point
    ├── public/
    │   └── index.html           # HTML file
    ├── package.json             # React dependencies
    └── node_modules/            # React node modules
```

### Backend (`app.py`)
- **Flask** handles the server-side logic of accepting requests, running the scraper, and sending back the scraped data to the frontend.
- Uses **Selenium** to interact with Amazon pages and extract product data.

### Frontend (`App.js`)
- Built using **React**, this part handles the user interface, including input fields, buttons, and displaying the results.
- Sends a request to the backend API and processes the response to display the products.

## How to Run

### Prerequisites:
- Python 3.x
- Node.js and npm
- Chrome browser (Selenium WebDriver needs it)

### Steps to Run:

1. **Install Backend Dependencies**:
   - Navigate to the `backend` directory and install Python dependencies using `pip`:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run Flask Backend**:
   - Start the Flask backend server:
     ```bash
     python app.py
     ```

3. **Install Frontend Dependencies**:
   - Navigate to the `frontend` directory and install React dependencies:
     ```bash
     npm install
     ```

4. **Run React Frontend**:
   - Start the React development server:
     ```bash
     npm start
     ```

5. **Visit the Application**:
   - Open your browser and go to `http://localhost:3000` to interact with the scraper and view the product details.

