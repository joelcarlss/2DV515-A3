import React from 'react'
import { makeStyles } from '@material-ui/core/styles'
import Fab from '@material-ui/core/Fab'
import Search from '@material-ui/icons/Search'

const useStyles = makeStyles(theme => ({
  root: {
    '& > *': {
      margin: theme.spacing(1)
    }
  },
  extendedIcon: {
    marginRight: theme.spacing(1)
  }
}))

export default function FloatingActionButtons ({ children }) {
  const classes = useStyles()

  return (
    <div className={classes.root}>
      <Fab children={() => console.log('as')} color='primary' aria-label='add' size='small'>
        <Search />
      </Fab>
    </div>
  )
}
