import Header from "./components/header";
import Prompt from "./components/prompt";
import { useEffect, useState } from "react";
import api from "./api/api";

export default function App() {
	const [prompt, setPrompt] = useState("example Prompt");

	const getPrompt = async () => {
		try {
			const response = await api.get("/prompt");
			setPrompt(response.data.prompt);
		} catch (error) {
			console.error("Error fetching prompt", error);
		}
	};

	// useEffect(() => {
	// 	getPrompt();
	// }, []);

	return (
		<div>
			<Header></Header>
			<Prompt promptText={prompt}></Prompt>
		</div>
	);
}
