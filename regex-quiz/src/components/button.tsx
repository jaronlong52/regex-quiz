import React from "react";
import "./layouts/button.css";

interface ButtonProps {
	onClick: () => void;
	children: React.ReactNode;
}

export default function Button({ onClick, children }: ButtonProps) {
	return (
		<button onClick={onClick} className="button">
			{children}
		</button>
	);
}
