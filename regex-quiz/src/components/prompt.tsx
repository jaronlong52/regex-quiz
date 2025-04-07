import React, { useEffect, useRef, useState } from "react";
import "./layouts/prompt.css";

interface PromptProps {
	promptText: string;
}

const Prompt: React.FC<PromptProps> = ({ promptText }) => {
	const [inputValue, setInputValue] = useState("");
	const inputRef = useRef<HTMLInputElement>(null);

	const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
		setInputValue(event.target.value);
	};

	useEffect(() => {
		if (inputRef.current) {
			inputRef.current.focus();
		}
	}, []);

	return (
		<div className="prompt-container">
			<h2>{promptText}</h2>
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
