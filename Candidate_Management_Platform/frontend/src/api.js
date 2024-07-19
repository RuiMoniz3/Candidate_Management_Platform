// api.js

import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/';

axios.defaults.baseURL = API_URL;

axios.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access_token');
        if (token) {
            config.headers['Authorization'] = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export default axios;
