const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

// Proxy para redirigir las solicitudes al endpoint de registrar usuario
app.use('/api/v1/users', createProxyMiddleware({ target: 'http://user-registration-service:5000', changeOrigin: true }));
app.use('/ping', createProxyMiddleware({ target: 'http://user-registration-service:5000', changeOrigin: true }));

// devulve hola mundo en una ruta nueva
app.get('/ping', (req, res) => {
  res.send('pong');
});

// Escucha en un puerto específico
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`API Gateway running on port ${PORT}`);
});
