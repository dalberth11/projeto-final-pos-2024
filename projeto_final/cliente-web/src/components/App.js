import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';
import ApiData from './components/ApiData';

function App() {
  const [apiData, setApiData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fazendo a requisição à API
  useEffect(() => {
    axios.get('http://localhost:5000/api/dados') // substitua pelo endpoint correto da sua API
      .then((response) => {
        setApiData(response.data);
        setLoading(false);
      })
      .catch((error) => {
        setError(error);
        setLoading(false);
      });
  }, []);

  return (
    <div className="App">
      <h1>Dados da API</h1>
      {loading && <p>Carregando...</p>}
      {error && <p>Erro ao carregar dados: {error.message}</p>}
      <ApiData data={apiData} />
    </div>
  );
}

export default App;
