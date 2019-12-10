import React, { useState, useEffect } from 'react'
import { makeStyles } from '@material-ui/core/styles'
import TextField from '@material-ui/core/TextField'
import cButton from './button'
import { getResult } from '../model/api'
import Search from '@material-ui/icons/Search';
import Fab from '@material-ui/core/Fab'
import { useAppState } from '../useAppState'
const useStyles = makeStyles(theme => ({
    root: {
        display: 'flex',
        flexWrap: 'wrap',
    },
    textField: {
        // marginLeft: theme.spacing(1),
        // marginRight: theme.spacing(1),
        width: 200,
        backgroundColor: 'white'
    },
    root2: {
        '& > *': {
            margin: theme.spacing(1),
        },
    },
    extendedIcon: {
        marginRight: theme.spacing(1),
    },
}));

export default function LayoutTextFields() {
    const classes = useStyles();
    const [input, setInput] = useState('')
    const { result, setResult } = useAppState()

    const handleChange = prop => event => {
        setInput(event.target.value)
    }
    const handleClick = async () => {
        let arr = await getResult(createSearch())
        setResult(arr)
    }
    const createSearch = () => {
        return input.replace(/\s/g, '+');
    }
    return (
        <div className={classes.root}>
            <div style={{ display: 'flex', paddingRight: '0' }}>
                <div className='rotate'>
                    <h1 >G</h1>
                </div>
                <TextField style={{ backgroundColor: 'white' }}
                    id="outlined-full-width"
                    style={{ margin: 0 }}
                    helperText="I have luck"
                    fullWidth
                    InputLabelProps={{
                        shrink: true,
                    }}
                    onChange={handleChange()}
                    variant="outlined"
                />
                <div className={classes.root2}>
                    <cButton variant="contained" color="secondary" onClick={() => handleClick()}>
                        <Fab color="primary" aria-label="add" size="small">
                            <Search />
                        </Fab>
                    </cButton>
                </div>
            </div>

        </div>
    )
}
