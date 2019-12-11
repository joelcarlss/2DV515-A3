import React from 'react'
import { makeStyles } from '@material-ui/core/styles'
import Paper from '@material-ui/core/Paper'
import Typography from '@material-ui/core/Typography'
import { useAppState } from '../useAppState'

import Button from '@material-ui/core/Button'
import Fab from '@material-ui/core/Fab'
import IconButton from '@material-ui/core/IconButton'
import AddIcon from '@material-ui/icons/Add'
import DeleteIcon from '@material-ui/icons/Delete'
import NavigationIcon from '@material-ui/icons/Navigation'
import ArrowLeftIcon from '@material-ui/icons/ArrowLeft'

import {
  useParams,
  useHistory
} from 'react-router-dom'

const useStyles = makeStyles(theme => ({
  root: {
    padding: theme.spacing(3, 2),
    backgroundColor: '#282c34'
  },
  margin: {
    color: 'white',
    margin: theme.spacing(1)
  },
  left: {
    display: 'flex',
    flexGrow: 1,
    alignItems: 'start'
  }

}))

export default function Wiki () {
  const classes = useStyles()
  let { title, id } = useParams()
  const history = useHistory()
  // const { result } = useAppState()
  console.log(id)
  return (
    <div>
      <div className={classes.left}>
        <IconButton onClick={() => history.goBack()} aria-label='delete' className={classes.margin} size='large'>
          <ArrowLeftIcon fontSize='inherit' />
          Go Back
        </IconButton>
      </div>
      <Paper className={classes.root}>
        <Typography style={{ color: 'white' }} variant='h5' component='h3'>
          {title}
        </Typography>
        <Typography style={{ color: 'white' }} component='p'>
          {id}
        </Typography>
      </Paper>
    </div>
  )
}
