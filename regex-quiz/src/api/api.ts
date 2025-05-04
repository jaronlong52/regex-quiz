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
		`https://regex-api-541139680351.us-central1.run.app/generate/${difficulty}?quantity=${quantity}`
	);
	if (!res.ok) {
		const errorData = await res.json();
		throw new Error(errorData.error || "Failed to fetch prompt");
	}

	const data = await res.json();
	return data;
}

export async function testRegex(
	pattern: string,
	strings: string[]
): Promise<{ result: boolean; error?: string }> {
	const res = await fetch(
		"https://regex-api-541139680351.us-central1.run.app/test",
		{
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({ pattern, strings }),
		}
	);

	if (!res.ok) {
		const errorData = await res.json();
		return { result: false, error: errorData.error || "Failed to test regex" };
	}

	const data = await res.json();
	return data;
}
