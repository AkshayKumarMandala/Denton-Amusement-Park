import React, { useEffect, useState } from 'react';
import axios from 'axios';

// Define the shape of a service
interface Service {
    id: number;
    name: string;
    description: string;
}

const Services: React.FC = () => {
    // Update the useState to specify the types
    const [services, setServices] = useState<Service[]>([]);
    const [error, setError] = useState<string | null>(null);

    // Fetch services from the backend
    const fetchServices = async () => {
        try {
            const response = await axios.get<Service[]>('http://localhost:5000/api/services'); // Ensure this URL is correct
            setServices(response.data); // Set the services to the response data
        } catch (err) {
            console.error('Failed to fetch services:', err);
            setError('Failed to fetch services: ' + (err instanceof Error ? err.message : 'Unknown error')); // Capture error message for UI
        }
    };

    useEffect(() => {
        fetchServices();
    }, []);

    return (
        <div>
            <h1>Available Services</h1>
            {error && <p>{error}</p>} {/* Display error message if there's an error */}
            {services.length === 0 ? (
                <p>No services available.</p>
            ) : (
                <ul>
                    {services.map(service => (
                        <li key={service.id}>
                            <h2>{service.name}</h2>
                            <p>{service.description}</p>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default Services;
