import Header from "./components/header";
import Prompt from "./components/prompt";

export default function App() {
	return (
		<div>
			<Header></Header>
			<Prompt promptText="^.*$"></Prompt>
		</div>
	);
}
