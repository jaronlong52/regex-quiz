import Header from "./components/header";
import Prompt from "./components/prompt";
// import { useEffect, useState } from "react";
// import api from "./api/api";
import Info from "./components/info";

export default function App() {
	// const [prompt, setPrompt] = useState("example Prompt");

	// const getPrompt = async () => {
	// 	try {
	// 		const response = await api.get("/prompt");
	// 		setPrompt(response.data.prompt);
	// 	} catch (error) {
	// 		console.error("Error fetching prompt", error);
	// 	}
	// };

	// useEffect(() => {
	// 	getPrompt();
	// }, []);

	return (
		<div>
			<Header></Header>
			<Info />
			<Prompt promptText={"example"}></Prompt>
		</div>
	);
}
