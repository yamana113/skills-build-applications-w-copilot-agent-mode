import React, { useEffect, useState } from 'react';

const resourceName = 'workouts';

function Workouts() {
  const [items, setItems] = useState([]);
  const [error, setError] = useState(null);

  const apiBase = process.env.REACT_APP_CODESPACE_NAME
    ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api`
    : '/api';
  const endpoint = `${apiBase}/${resourceName}/`;

  useEffect(() => {
    console.log(`Workouts endpoint: ${endpoint}`);
    fetch(endpoint)
      .then((res) => res.json())
      .then((data) => {
        console.log('Workouts fetched data:', data);
        const payload = Array.isArray(data) ? data : data?.results ?? [];
        setItems(payload);
      })
      .catch((fetchError) => {
        console.error('Workouts fetch error:', fetchError);
        setError(fetchError);
      });
  }, [endpoint]);

  return (
    <div>
      <h2>Workouts</h2>
      {error && <div className="alert alert-danger">Failed to load workouts.</div>}
      {!error && items.length === 0 && <p>Loading workouts...</p>}
      {items.length > 0 && (
        <div className="list-group">
          {items.map((item, idx) => (
            <pre key={idx} className="list-group-item">{JSON.stringify(item, null, 2)}</pre>
          ))}
        </div>
      )}
    </div>
  );
}

export default Workouts;
