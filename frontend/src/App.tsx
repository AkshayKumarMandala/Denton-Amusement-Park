import React from 'react';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import AdminDashboard from './pages/AdminDashboard';
import VisitorDashboard from './pages/VisitorDashboard';
import FeedbackForm from './components/FeedbackForm';
import AdminFeedbacks from './components/AdminFeedbacks';
import Services from './pages/Services';

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/services" element={<Services />} />
        <Route path="/admin" element={<AdminDashboard />} />
        <Route path="/admin/feedbacks" element={<AdminFeedbacks />} />
        <Route path="/feedback" element={<FeedbackForm />} />
      </Routes>
    </Router>
  );
};

export default App;
