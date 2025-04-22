import React from "react";
import "./layouts/button.css";

interface ButtonProps {
	onClick: () => void;
	children: React.ReactNode;
	disabled?: boolean;
}

export default function Button({
	onClick,
	children,
	disabled = false,
}: ButtonProps) {
	return (
		<button onClick={onClick} disabled={disabled} className="button">
			{children}
		</button>
	);
}
