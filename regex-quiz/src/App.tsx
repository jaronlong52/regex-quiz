import Header from "./components/header";
import Prompt from "./components/prompt";
import Info from "./components/info";
import { useState } from "react";

export default function App() {
	const [isStarted, setIsStarted] = useState(false);
	const [isEnded, setIsEnded] = useState(false);

	function handleStart() {
		setIsStarted(true);
		setIsEnded(false);
	}

	function handleEnd() {
		setIsEnded(true);
		setIsStarted(false);
	}

	return (
		<div>
			<Header />
			<Info onStartClick={handleStart} onEndClick={handleEnd} />
			<Prompt started={isStarted} ended={isEnded} />
		</div>
	);
}
