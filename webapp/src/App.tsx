import './App.css'
import { AppProviders } from './config/AppProvider'
import { Outlet } from 'react-router'

function App() {
  return (
    <AppProviders>
      <Outlet />
    </AppProviders>
  )
}

export default App
