import React from 'react'
import { makeStyles } from '@material-ui/core/styles'
import List from '@material-ui/core/List'
import ListItem from '@material-ui/core/ListItem'
import ListItemAvatar from '@material-ui/core/ListItemAvatar'
import ListItemIcon from '@material-ui/core/ListItemIcon'
import ListItemSecondaryAction from '@material-ui/core/ListItemSecondaryAction'
import ListItemText from '@material-ui/core/ListItemText'
import Avatar from '@material-ui/core/Avatar'
import IconButton from '@material-ui/core/IconButton'
import FormGroup from '@material-ui/core/FormGroup'
import FormControlLabel from '@material-ui/core/FormControlLabel'
import Checkbox from '@material-ui/core/Checkbox'
import Grid from '@material-ui/core/Grid'
import Typography from '@material-ui/core/Typography'
import FolderIcon from '@material-ui/icons/Folder'
import DeleteIcon from '@material-ui/icons/Delete'
import { useAppState } from '../useAppState'

const useStyles = makeStyles(theme => ({
    root: {
        flexGrow: 1,
        maxWidth: 752,
    },
    demo: {
        backgroundColor: '#282c34',
    },
    title: {
        margin: theme.spacing(4, 0, 2),
    },
}))

export default function InteractiveList() {
    const classes = useStyles()
    const [dense, setDense] = React.useState(false)
    const [secondary, setSecondary] = React.useState(false)
    const { result, setResult } = useAppState()
    console.log(result)
    return (
        <div className={classes.root}>
            <Grid container spacing={2}>
                <Grid item xs={12} md={6}>
                    <div className={classes.demo}>
                        <List >
                            {result !== undefined ?
                                typeof result === 'string' ? <ListItem>
                                    <ListItemText
                                        key={result}
                                        primary={result}
                                    />
                                </ListItem> :
                                    result.map(link => (
                                        <ListItem>
                                            <ListItemText
                                                key={link.name}
                                                primary={link.name}
                                                secondary={link.content}
                                            />
                                        </ListItem>
                                    ))
                                : null}
                        </List>
                    </div>
                </Grid>

            </Grid>

        </div>
    )
}
