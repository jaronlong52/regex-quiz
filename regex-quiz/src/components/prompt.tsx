import React, { useState } from "react";
import "./layouts/prompt.css";

interface PromptProps {
	promptText: string;
}

const Prompt: React.FC<PromptProps> = ({ promptText }) => {
	const [inputValue, setInputValue] = useState("");

	const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
		setInputValue(event.target.value);
	};

	return (
		<div className="prompt-container">
			<h2>{promptText}</h2>
			<input
				type="text"
				value={inputValue}
				onChange={handleInputChange}
				className="prompt-input blinking-cursor"
			/>
		</div>
	);
};

export default Prompt;
