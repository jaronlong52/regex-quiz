import { useState, useEffect } from "react";
import "./layouts/info.css";
import Button from "./button.tsx";

interface InfoProps {
	onStartClick: () => void;
	onEndClick: () => void;
	setDifficulty: (newDifficulty: number) => void;
}

const Info: React.FC<InfoProps> = ({
	onStartClick,
	onEndClick,
	setDifficulty,
}) => {
	const [timer, setTimer] = useState(60);
	const [selectedTime, setSelectedTime] = useState(60); // Default selected time is 1 minute
	const [isStarted, setIsStarted] = useState(false);
	const [difficultyState, setDifficultyState] = useState(0); // Default difficulty is Easy

	const timeOptions = [
		{ label: "1 minute", value: 60 },
		{ label: "3 minutes", value: 180 },
		{ label: "5 minutes", value: 300 },
	];

	const difficulties = [
		{ label: "Easy", value: 0 },
		{ label: "Medium", value: 1 },
		{ label: "Hard", value: 2 },
		{ label: "Expert", value: 3 },
		{ label: "Master", value: 4 },
	];

	useEffect(() => {
		if (isStarted) {
			const interval = setInterval(() => {
				setTimer((prevTimer) => {
					if (prevTimer > 0) {
						return prevTimer - 1;
					} else {
						clearInterval(interval);
						return 0;
					}
				});
			}, 1000);

			return () => clearInterval(interval);
		}
	}, [isStarted]);

	const handleTimeChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
		const selectedValue = parseInt(event.target.value);
		setSelectedTime(selectedValue);
		setTimer(selectedValue);
	};

	const handleDifficultyChange = (
		event: React.ChangeEvent<HTMLSelectElement>
	) => {
		// Handle difficulty change if needed
		const selectedDifficulty = parseInt(event.target.value);
		setDifficultyState(selectedDifficulty);
		setDifficulty(selectedDifficulty);
	};

	const handleStart = () => {
		setIsStarted(true);
		setTimer(selectedTime);
		onStartClick();
	};

	const handleEnd = () => {
		setIsStarted(false);
		setTimer(selectedTime);
		onEndClick();
	};

	useEffect(() => {
		if (timer === 0) {
			setIsStarted(false);
			onEndClick();
		}
	}, [timer, onEndClick]);

	return (
		<div className="main-info">
			<h2 className="timer">Timer: {timer} seconds</h2>
			<div className="info-container">
				<select
					className="info-dropdown"
					value={selectedTime}
					onChange={handleTimeChange}
					disabled={isStarted}
				>
					{timeOptions.map((item, index) => (
						<option
							className="info-dropdown-options"
							key={index}
							value={item.value}
						>
							{item.label}
						</option>
					))}
				</select>
				<select
					className="info-dropdown"
					value={difficultyState}
					onChange={handleDifficultyChange}
					disabled={isStarted}
				>
					{difficulties.map((item, index) => (
						<option
							className="info-dropdown-options"
							key={index}
							value={item.value}
						>
							{item.label}
						</option>
					))}
				</select>
				<div className="info-buttons">
					<Button onClick={handleStart} disabled={isStarted}>
						Start
					</Button>
					<div className="info-buttons-end">
						<Button onClick={handleEnd}>End</Button>
					</div>
				</div>
			</div>
		</div>
	);
};

export default Info;
