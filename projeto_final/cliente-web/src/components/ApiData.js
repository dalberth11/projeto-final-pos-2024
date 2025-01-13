import React from 'react';

function ApiData({ data }) {
  return (
    <div className="api-data">
      {data && data.length > 0 ? (
        <ul>
          {data.map((item, index) => (
            <li key={index}>
              <strong>{item.name}</strong> - {item.description}
            </li>
          ))}
        </ul>
      ) : (
        <p>Nenhum dado disponível.</p>
      )}
    </div>
  );
}

export default ApiData;
