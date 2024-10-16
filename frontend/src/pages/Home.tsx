import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/home.css'; // Assuming you're adding styles in Home.css

const Home: React.FC = () => {
  return (
    <div className="home">
      <header className="home-header">
        <h1>Welcome to Denton Amusement Park</h1>
        <img 
          src={`${process.env.PUBLIC_URL}/assets/home.jpg`} 
          alt="Denton Amusement Park Homepage" 
          style={{ maxWidth: '100%', height: 'auto' }} 
        />
        <p>
          Experience the fun, adventure, and inclusivity at Denton Amusement Park, where everyone is welcome! 
          Explore accessible rides, sensory-friendly zones, and family-friendly entertainment for all ages.
        </p>
        <Link to="/services" className="btn btn-primary">
          Explore Services
        </Link>
        <Link to="/admin" className="btn btn-secondary">
          Admin Dashboard
        </Link>
        <Link to="/feedback" className="btn btn-secondary">
          Leave Feedback
        </Link>
      </header>

      <section className="features">
        <h2>Our Highlights</h2>
        <div className="features-grid">
          <div className="feature-item">
            <img src="/assets/wheelchair.png" alt="Wheelchair-friendly paths" className="feature-icon" />
            <h3>Wheelchair-Friendly Pathways</h3>
            <p>Seamless and accessible paths throughout the park to ensure ease of movement.</p>
          </div>
          <div className="feature-item">
            <img src="/assets/sensory.png" alt="Sensory-friendly zones" className="feature-icon" />
            <h3>Sensory-Friendly Zones</h3>
            <p>Quiet and comforting areas designed for visitors with sensory sensitivities.</p>
          </div>
          <div className="feature-item">
            <img src="/assets/rides.png" alt="Inclusive rides" className="feature-icon" />
            <h3>Inclusive Rides</h3>
            <p>Exciting rides built for accessibility, ensuring fun for everyone.</p>
          </div>
        </div>
      </section>

      <section className="cta-section">
        <h2>Plan Your Visit Today!</h2>
        <p>Get ready for an unforgettable experience at Denton Amusement Park.</p>
        <Link to="/visitor" className="btn btn-secondary">
          Visitor Dashboard
        </Link>
      </section>
    </div>
  );
};

export default Home;
