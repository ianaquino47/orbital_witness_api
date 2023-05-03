import "./App.css";
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Title from "./components/Title";
import MainPage from "./components/MainPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<MainPage />} />
        <Route path="/titles/:id" element={<Title />} />
      </Routes>
    </Router>
  );
}

export default App;
