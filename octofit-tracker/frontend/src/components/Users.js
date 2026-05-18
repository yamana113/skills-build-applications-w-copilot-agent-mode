import React, { useEffect, useState } from 'react';

const resourceName = 'users';

function Users() {
  const [items, setItems] = useState([]);
  const [error, setError] = useState(null);

  const apiBase = process.env.REACT_APP_CODESPACE_NAME
    ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api`
    : '/api';
  const endpoint = `${apiBase}/${resourceName}/`;

  useEffect(() => {
    console.log(`Users endpoint: ${endpoint}`);
    fetch(endpoint)
      .then((res) => res.json())
      .then((data) => {
        console.log('Users fetched data:', data);
        const payload = Array.isArray(data) ? data : data?.results ?? [];
        setItems(payload);
      })
      .catch((fetchError) => {
        console.error('Users fetch error:', fetchError);
        setError(fetchError);
      });
  }, [endpoint]);

  return (
    <div>
      <h2>Users</h2>
      {error && <div className="alert alert-danger">Failed to load users.</div>}
      {!error && items.length === 0 && <p>Loading users...</p>}
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

export default Users;
