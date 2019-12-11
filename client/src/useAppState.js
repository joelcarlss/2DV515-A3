import { useState, useContext } from 'react'
import createContainer from 'constate'

const useApp = () => {
  const [name, setName] = useState('')
  const [amount, setAmount] = useState('')
  const [algoritm, setAlgoritm] = useState('')
  const [result, setResult] = useState([])
  const [userResult, setUserResult] = useState([])
  const [showUser, setShowUser] = useState(false)
  const [pages, setPages] = useState({})
  const [wiki, setWiki] = useState({})

  return {
    name,
    setName,
    amount,
    setAmount,
    algoritm,
    setAlgoritm,
    result,
    setResult,
    showUser,
    setShowUser,
    userResult,
    setUserResult,
    pages,
    setPages,
    wiki,
    setWiki
  }
}

const { Context, Provider } = createContainer(useApp)

export const useAppState = () => {
  const state = useContext(Context)
  return state
}

export { Provider }
