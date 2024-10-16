import React from 'react';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Map from './components/Map';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Services from './pages/Services';

const App: React.FC = () => {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/services" element={<Services />} />
        </Routes>
        <Map />
        <Footer />
      </div>
    </Router>
  );
};

export default App;
