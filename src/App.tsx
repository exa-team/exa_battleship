import Home from './pages/home';
import Room from './pages/room';

import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";

function App() {
  return (
    <Router>
       <Switch>
          <Route path="/about">
            {/* <About /> */}
          </Route>
          <Route path="/room/:salaId">
            <Room />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
    </Router>
  );
}

export default App;
