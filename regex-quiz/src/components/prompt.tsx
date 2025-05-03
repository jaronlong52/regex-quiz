import React, { useEffect, useRef, useState } from "react";
import "./layouts/prompt.css";
import { fetchPrompt, RegexPrompt } from "../api/api";

interface PromptProps {
	started: boolean;
	ended: boolean;
	difficulty: number;
}

const Prompt: React.FC<PromptProps> = ({ started, ended, difficulty }) => {
	const inputRef = useRef<HTMLInputElement>(null);
	const [prompt, setPrompt] = useState<RegexPrompt | null>(null);
	const [pattern, setPattern] = useState<string>("");
	const [promptIsRegex, setPromptIsRegex] = useState<boolean>(false);
	const myMapRef = useRef<Map<string, { input: string; correct: boolean }>>(
		new Map()
	);

	const checkInput = () => {
		const currentValue = inputRef.current?.value || "";
		if (!prompt) return;

		// Only check if minimum length is met for string match
		if (!promptIsRegex && currentValue.length < pattern.length) {
			return;
		}

		if (!promptIsRegex) {
			if (currentValue === pattern) {
				handleCorrect(currentValue);
			}
		} else {
			try {
				const regex = new RegExp(pattern);
				if (regex.test(currentValue)) {
					handleCorrect(currentValue);
				}
			} catch (error) {
				console.log("Invalid regex in pattern:", error);
			}
		}
	};

	const handleKeyUp = (event: React.KeyboardEvent<HTMLInputElement>) => {
		if (event.key === "Enter") {
			const value = inputRef.current?.value || "";
			// Check if it wasn't already marked correct (avoid overwriting correct entries)
			if (!myMapRef.current.has(pattern)) {
				myMapRef.current.set(pattern, { input: value, correct: false });
			}
			handleFetch();
		}
	};

	const handleCorrect = (value: string) => {
		myMapRef.current.set(pattern, { input: value, correct: true });
		handleFetch();
	};

	const handleFetch = async () => {
		const newPrompt = await fetchPrompt(difficulty);
		setPromptIsRegex(Math.random() < 0.5);
		setPrompt(newPrompt);
		setPattern(newPrompt.pattern);
		if (inputRef.current) inputRef.current.value = "";
		console.log(newPrompt);
	};

	useEffect(() => {
		if (started) {
			myMapRef.current.clear();
			handleFetch();
			inputRef.current?.focus();
		}
	}, [started]);

	useEffect(() => {
		if (ended) {
			setPrompt(null);
			if (inputRef.current) inputRef.current.value = "";
			console.log("User inputs collected:", myMapRef.current);
		}
	}, [ended]);

	return (
		<div className="prompt-container">
			<h2>
				{promptIsRegex
					? pattern
					: prompt?.strings.map((str, idx) => (
							<span key={idx}>
								{`"${str}"`}
								{idx < prompt.strings.length - 1 ? ", " : ""}
							</span>
					  ))}
			</h2>
			<input
				type="text"
				ref={inputRef}
				className="prompt-input"
				disabled={!started || ended}
				onKeyUp={handleKeyUp}
				onChange={checkInput}
			/>
			{!ended && <div>*press enter to skip</div>}
			{ended && (
				<div className="results-container">
					<h3 style={{ textAlign: "center" }}>Results</h3>
					<ul>
						{Array.from(myMapRef.current.entries()).map(
							([key, result], idx) => (
								<li key={idx} style={{ marginBottom: "1rem" }}>
									<strong>Pattern:</strong> {key} <br />
									<strong>Your Input:</strong> {result.input} <br />
									<strong>Status:</strong> {result.correct ? "✅" : "❌"}
								</li>
							)
						)}
					</ul>
				</div>
			)}
		</div>
	);
};

export default Prompt;
