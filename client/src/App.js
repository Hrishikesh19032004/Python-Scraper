import axios from 'axios';
import React, { useState } from 'react';
import './App.css';  

function App() {
  const [products, setProducts] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [productsPerPage] = useState(30);
  const [loading, setLoading] = useState(false);

  // Fetch products from the backend API
  const fetchProducts = async () => {
    setLoading(true);
    const url = "https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar";
    try {
      const response = await axios.post('http://localhost:5000/scrape', { url });
      setProducts(response.data);
      setCurrentPage(1); 
    } catch (error) {
      console.error("Error fetching products:", error);
    }
    setLoading(false);
  };

  // Pagination Logic
  const indexOfLastProduct = currentPage * productsPerPage;
  const indexOfFirstProduct = indexOfLastProduct - productsPerPage;
  const currentProducts = products.slice(indexOfFirstProduct, indexOfLastProduct);

  const totalPages = Math.ceil(products.length / productsPerPage);

  const handleNextPage = () => {
    if (currentPage < totalPages) setCurrentPage(currentPage + 1);
  };

  const handlePrevPage = () => {
    if (currentPage > 1) setCurrentPage(currentPage - 1);
  };

  return (
    <div className="app-container">
      <h1>Python Scraper</h1>
      <button onClick={fetchProducts} disabled={loading} className="fetch-button">
        {loading ? 'Loading...' : 'Fetch Products'}
      </button>

      <div className="product-grid">
        {currentProducts.map((product, index) => (
          <div key={index} className="product-card">
            <h3>{product["Product Name"]}</h3>
            <p>Price: {product.Price}</p>
            <p>Rating: {product.Rating}</p>
            <p>Qty Sold: {product["Seller Name"]}</p>
          </div>
        ))}
      </div>

      {/* Pagination */}
      <div className="pagination">
        <button onClick={handlePrevPage} disabled={currentPage === 1} className="pagination-button">
          Previous
        </button>
        <span>Page {currentPage} of {totalPages}</span>
        <button onClick={handleNextPage} disabled={currentPage === totalPages} className="pagination-button">
          Next
        </button>
      </div>
    </div>
  );
}

export default App;