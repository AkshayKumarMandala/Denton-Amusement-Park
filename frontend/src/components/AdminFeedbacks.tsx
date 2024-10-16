import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface Feedback {
  id: number;
  user_id: number;
  message: string;
}

const AdminFeedbacks: React.FC = () => {
  const [feedbacks, setFeedbacks] = useState<Feedback[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchFeedbacks = async () => {
      try {
        const response = await axios.get('/api/feedback'); // Adjust the endpoint as needed
        setFeedbacks(response.data);
      } catch (err) {
        setError('Failed to fetch feedbacks');
      }
    };

    fetchFeedbacks();
  }, []);

  return (
    <div className="admin-feedbacks">
      <h2>Admin Feedbacks</h2>
      {error && <p className="error">{error}</p>}
      <ul>
        {feedbacks.map(feedback => (
          <li key={feedback.id}>
            <p><strong>User ID:</strong> {feedback.user_id}</p>
            <p><strong>Message:</strong> {feedback.message}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AdminFeedbacks;
