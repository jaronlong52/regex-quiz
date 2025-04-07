import { useState, useEffect } from "react";
import "./layouts/info.css";
import Scores from "./scores";

export default function Info() {
	const [timer, setTimer] = useState(60);
	const [selectedTime, setSelectedTime] = useState(60); // Default selected time is 1 minute
	const [isStarted, setIsStarted] = useState(false);

	const items = [
		{ label: "1 minute", value: 60 },
		{ label: "3 minutes", value: 180 },
		{ label: "5 minutes", value: 300 },
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

	const handleStart = () => {
		setIsStarted(true);
	};

	const handleEnd = () => {
		setIsStarted(false);
		setTimer(selectedTime);
	};

	return (
		<div className="main-info">
			<h2 className="timer">Timer: {timer} seconds</h2>
			<div className="info-container">
				<Scores />
				<select value={selectedTime} onChange={handleTimeChange}>
					{items.map((item, index) => (
						<option key={index} value={item.value}>
							{item.label}
						</option>
					))}
				</select>
				<div>
					<button onClick={handleStart}>Start</button>
					<button onClick={handleEnd}>End</button>
				</div>
			</div>
			{/* <div className="info-divider"></div> */}
		</div>
	);
}
