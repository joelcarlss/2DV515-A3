import React from 'react'
import { Router, Route, Switch } from 'react-router-dom'
// import Table from './components/DenseTable'
// import SimpleSelect from './components/SimpleSelect'
import history from './config/history'
import { Provider } from './useAppState'
import Main from './pages/Main'
import wiki from './components/wiki'

function App () {
  return (
    <Router history={history}>
      <div className='App'>
        <header className='App-header'>

          <Switch>
            <Route exact path='/' component={Main} />
            <Route exact path='/wiki/:title/:id' component={wiki} />
          </Switch>
        </header>

      </div>
    </Router>
  )
}

export default () => <Provider><App /></Provider>
