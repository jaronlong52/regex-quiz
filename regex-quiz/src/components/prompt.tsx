import React, { useEffect, useRef, useState } from "react";
import "./layouts/prompt.css";
import { fetchPrompt, RegexPrompt } from "../api/api";

interface PromptProps {
	started: boolean;
	ended: boolean;
}

const Prompt: React.FC<PromptProps> = ({ started, ended }) => {
	const [inputValue, setInputValue] = useState("");
	const inputRef = useRef<HTMLInputElement>(null);
	const [prompt, setPrompt] = useState<RegexPrompt | null>(null);

	const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
		setInputValue(event.target.value);
	};

	function handleFetch() {
		fetchPrompt(3).then((newPrompt) => {
			setPrompt(newPrompt);
			setInputValue(""); // Reset input value when fetching a new prompt
		});
	}

	useEffect(() => {
		if (inputRef.current) {
			inputRef.current.focus();
		}
	}, []);

	useEffect(() => {
		if (started) {
			handleFetch();
		}
	}, [started]);

	useEffect(() => {
		if (ended) {
			setPrompt(null); // Clear prompt when the game ends
			setInputValue(""); // Reset input value when the game ends
		}
	}, [ended]);

	return (
		<div className="prompt-container">
			<h2>{prompt?.strings}</h2>
			<input
				type="text"
				value={inputValue}
				onChange={handleInputChange}
				ref={inputRef}
				className="prompt-input"
			/>
		</div>
	);
};

export default Prompt;
