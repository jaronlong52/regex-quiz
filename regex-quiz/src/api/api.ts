import axios from "axios";

const api = axios.create({
	// Use environment variable for the base URL
	baseURL: process.env.REACT_APP_API_URL || "http://localhost:3000",
});

export default api;
