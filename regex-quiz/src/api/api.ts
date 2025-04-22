export interface RegexPrompt {
	// Adjust the type according to the actual shape returned by prompt.to_dict()
	difficulty: number;
	pattern: string;
	strings: string[];
}

export async function fetchPrompt(
	difficulty: number,
	quantity = 3
): Promise<RegexPrompt> {
	const res = await fetch(
		`http://localhost:8080/generate/${difficulty}?quantity=${quantity}`
	);
	if (!res.ok) {
		const errorData = await res.json();
		throw new Error(errorData.error || "Failed to fetch prompt");
	}

	const data = await res.json();
	return data;
}
