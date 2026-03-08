import React from 'react'
import './styles/App.css'

function App() {
  return (
    <div className="app">
      <header className="header">
        <h1>🛒 Grocery Bud</h1>
        <p>Your simple grocery list tracker</p>
      </header>
      
      <main className="container">
        <div className="card">
          <h2>Welcome to Grocery Bud!</h2>
          <p>React frontend is ready to connect to Django API</p>
          
          <div className="status">
            <div className="status-item">
              <span className="status-dot green"></span>
              <span>✅ React running on port 5173</span>
            </div>
            <div className="status-item">
              <span className="status-dot yellow"></span>
              <span>⏳ Waiting for Django API on port 8000</span>
            </div>
            <div className="status-item">
              <span className="status-dot blue"></span>
              <span>📦 Ready to fetch grocery items</span>
            </div>
          </div>

          <div className="next-steps">
            <h3>Next Steps:</h3>
            <ul>
              <li>Start Django server: <code>cd ../backend & python manage.py runserver</code></li>
              <li>Connect to API and display grocery items</li>
              <li>Add, update, and delete items</li>
            </ul>
          </div>
        </div>
      </main>
    </div>
  )
}

export default App