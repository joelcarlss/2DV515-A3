import React from 'react'
import SearchEngine from '../components/searchEngine'
// import Table from './components/DenseTable'
// import SimpleSelect from './components/SimpleSelect'
import { Provider } from '../useAppState'
import List from '@material-ui/core/List'
import '../App.css'
import CssBaseline from '@material-ui/core/CssBaseline'
import Container from '@material-ui/core/Container'
import InteractiveList from '../components/linkList'
function Main () {
  return (
    <div>
      <CssBaseline />

      <Container maxWidth='sm' textalign='center' >
        <List style={{ maxHeight: '100%', overflow: 'visible' }} >
          <center style={{ marginLeft: '70px', display: 'flex', flexWrap: 'wrap', padding: '0', margin: '0' }}>
            <h1 style={{ color: 'red' }}>o</h1><h1 style={{ color: 'yellow' }}>o</h1><h1 style={{ color: 'blue' }}>g</h1><h1 style={{ color: 'green' }}>l</h1><h1 style={{ color: 'red' }}>e</h1>
          </center>
          <SearchEngine />
        </List>
      </Container>
      <InteractiveList />
    </div>

  )
}

export default () => <Provider><Main /></Provider>
