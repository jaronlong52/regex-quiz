import Header from "./components/header";
import Prompt from "./components/prompt";
import Info from "./components/info";
import { useState } from "react";

export default function App() {
	const [isStarted, setIsStarted] = useState(false);
	const [isEnded, setIsEnded] = useState(false);
	const [difficulty, setDifficulty] = useState(0);

	function handleStart() {
		setIsStarted(true);
		setIsEnded(false);
	}

	function handleEnd() {
		setIsEnded(true);
		setIsStarted(false);
	}

	function handleDifficultyChange(newDifficulty: number) {
		setDifficulty(newDifficulty);
	}

	return (
		<div>
			<Header />
			<Info
				onStartClick={handleStart}
				onEndClick={handleEnd}
				setDifficulty={handleDifficultyChange}
			/>
			<Prompt started={isStarted} ended={isEnded} difficulty={difficulty} />
		</div>
	);
}
