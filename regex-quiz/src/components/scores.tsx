import { useState } from "react";
import "./layouts/scores.css";
import Button from "./button";

export default function Scores() {
	const [scores] = useState([
		// removed setScores
		"1 minute: 4",
		"3 minutes: 8",
		"5 minutes: 12",
	]);
	const [showPopup, setShowPopup] = useState(false);

	function togglePopup() {
		setShowPopup(!showPopup);
	}

	return (
		<div className="popup-container">
			<Button onClick={togglePopup}>High Scores</Button>
			{showPopup && (
				<div className="popup">
					<div className="popup-content">
						<h2>High Scores</h2>
						{scores.map((score, index) => (
							<div key={index}>{score}</div>
						))}
						<button className="close-btn" onClick={togglePopup}>
							X
						</button>
					</div>
				</div>
			)}
		</div>
	);
}
