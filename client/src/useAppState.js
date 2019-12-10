import { useEffect, useState, useContext } from 'react'
import createContainer from 'constate'
import { getUser, getData, getReqUser } from "./model/api"

const useApp = () => {
  const [users, setUsers] = useState([])
  const [name, setName] = useState('')
  const [amount, setAmount] = useState('')
  const [algoritm, setAlgoritm] = useState('')
  const [result, setResult] = useState([])
  const [userResult, setUserResult] = useState([])
  const [showUser, setShowUser] = useState(false)


  return {
    users,
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
    setUserResult
  }
}

const { Context, Provider } = createContainer(useApp)

export const useAppState = () => {
  const state = useContext(Context)
  return state
}

export { Provider }
