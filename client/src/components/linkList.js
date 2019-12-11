import React, { useEffect } from 'react'
import history from '../config/history'

import { makeStyles } from '@material-ui/core/styles'
import { useAppState } from '../useAppState'
import Table from '@material-ui/core/Table'
import TableBody from '@material-ui/core/TableBody'
import TableCell from '@material-ui/core/TableCell'
import TableHead from '@material-ui/core/TableHead'
import TableRow from '@material-ui/core/TableRow'
import Paper from '@material-ui/core/Paper'
import ListItem from '@material-ui/core/ListItem'
import ListItemText from '@material-ui/core/ListItemText'
const useStyles = makeStyles({
  root: {
    width: '100%'
  },
  paper: {
    width: '100%',
    overflowX: 'auto'
  },
  table: {
    minWidth: 650
  }
})

export default function DenseTable () {
  const classes = useStyles()
  const { result } = useAppState()
  const { pages } = useAppState()
  const handleClick = (name, i) => {
    history.push(`${'/wiki/' + name.replace(/_/g, ' ') + '/' + pages[i]}`)
  }

  const renderHeader = () => {
    if (result.length > 0) {
      return (
        <TableHead>
          <TableRow>
            <TableCell>Name</TableCell>
            <TableCell align='right'>Category</TableCell>
            <TableCell align='right'>Score</TableCell>
            <TableCell align='right'>Content</TableCell>
            <TableCell align='right'>Location</TableCell>
            <TableCell align='right'>Page rank</TableCell>
          </TableRow>
        </TableHead>
      )
    }
  }
  console.log(result)
  return (
    <div className={classes.root}>
      <Paper className={classes.paper}>
        {typeof result === 'string' ? <ListItem>
          <ListItemText
            key={result}
            primary={result}
          />
        </ListItem>
          : <div>
            {typeof result !== 'string' && result !== undefined
              ? <Table className={classes.table} size='small' aria-label='a dense table'>
                {renderHeader()}
                <TableBody>
                  {result.map((row, i) => (
                    <TableRow key={row.name}>
                      <TableCell component='th' scope='row' onClick={() => handleClick(row.name, i)}>
                        {row.name}
                      </TableCell>
                      <TableCell align='right'>{row.category}</TableCell>
                      <TableCell align='right'>{row.score}</TableCell>
                      <TableCell align='right'>{row.content}</TableCell>
                      <TableCell align='right'>{row.location}</TableCell>
                      <TableCell align='right'>{row.page_rank}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>

              </Table> : null}
          </div>}
      </Paper>
    </div>
  )
}

// return (
// console.log(result)
//     <div className={classes.root}>
//         <Grid container spacing={2}>
//             <Grid item xs={12} md={6}>
//                 <div className={classes.demo}>
//                     <List >
//                         {result !== undefined ?
//                             typeof result === 'string' ? <ListItem>
//                                 <ListItemText
//                                     key={result}
//                                     primary={result}
//                                 />
//                             </ListItem> :
//                                 result.map(link => (
//                                     <ListItem>
//                                         <ListItemText
//                                             key={link.name}
//                                             primary={link.name}
//                                             secondary={link.content}
//                                         />
//                                     </ListItem>
//                                 ))
//                             : null}
//                     </List>
//                 </div>
//             </Grid>

//         </Grid>

//     </div>
