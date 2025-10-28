import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Box, CssBaseline, Container } from "@mui/material";
import ProductList from "./components/Products/ProductList";
import Navbar from "./components/Common/Navbar";
import "./App.css";

function App() {
  return (
    <Router>
      <CssBaseline />
      <Box sx={{ display: "flex", flexDirection: "column", minHeight: "100vh" }}>
        <Navbar />
        <Container component="main" sx={{ flex: 1, py: 3 }}>
          <Routes>
            <Route path="/" element={<ProductList />} />
            <Route path="/products" element={<ProductList />} />
          </Routes>
        </Container>
      </Box>
    </Router>
  );
}

export default App;
