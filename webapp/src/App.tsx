import { AppLayout } from "./components";
import { AppProviders } from "./config/AppProvider";
import { Outlet } from "react-router";

function App() {
  return (
    <AppProviders>
      <AppLayout>
        <Outlet />
      </AppLayout>
    </AppProviders>
  );
}

export default App;
