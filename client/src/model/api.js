export const getUser = async () => {
  try {
    let data
    const result = await window.fetch('http://127.0.0.1:5002/users')
    if (result.status === 200) {
      data = await result.json()
    }
    return data.res
  } catch (e) {
    return undefined
  }
}

export const getData = async (id, amount, algoritm) => {
  try {
    let data
    const result = await window.fetch(`http://127.0.0.1:5002/find/movies/${algoritm}/${id}/${amount}`)
    if (result.status === 200) {
      data = await result.json()
    }
    console.log(data.res)
    return data.res
  } catch (e) {
    console.log(e)
    return undefined
  }
}

export const getReqUser = async (id, amount, algoritm) => {
  try {
    let data
    const result = await window.fetch(`http://127.0.0.1:5002/find/users/${algoritm}/${id}/${amount}`)
    if (result.status === 200) {
      data = await result.json()
    }
    console.log(data.res)
    return data.res
  } catch (e) {
    console.log(e)
    return undefined
  }
}
export const getCluster = async () => {
  try {
    let data
    const result = await window.fetch('http://127.0.0.1:5002/clusters')
    if (result.status === 200) {
      data = await result.json()
    }
    return data.res
  } catch (e) {
    console.log(e)
    return undefined
  }
}

export const getResult = async (data) => {
  try {
    let res
    const result = await window.fetch(`${'http://127.0.0.1:5002/q/' + data}`)
    if (result.status === 200) {
      res = await result.json()
    }
    return res.res
  } catch (e) {
    console.log(e)
    return undefined
  }
}

export const getPage = async (category, name) => {
  try {
    let data
    const result = await window.fetch(`${'http://127.0.0.1:5002/page/' + category + '+' + name}`)
    if (result.status === 200) {
      data = await result.json()
    }
    return data.res
  } catch (e) {
    console.log(e)
    return undefined
  }
}
